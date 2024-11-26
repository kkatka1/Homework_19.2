from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory, modelform_factory
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Version, Category

from django.shortcuts import get_object_or_404, render

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')

#def contacts(request):
#   return render(request, 'contacts.html')


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        active_versions = product.versions.filter(is_current=True)
        context['active_versions'] = active_versions
        return context

class ContactView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        """
        Исключение некоторых слов
        Автоматическая привязка пользователя к продукту
        """
        cleaned_data = form.cleaned_data['name'].lower()
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        for word in forbidden_words:
            if word in cleaned_data:
                form.add_error('name', 'Данное название не подходит.')
                return self.form_invalid(form)


        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        """
        Возвращает форму в зависимости от роли пользователя.
        """
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.change_description')and user.has_perm('catalog.change_category'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')




