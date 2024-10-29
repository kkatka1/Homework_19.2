from django.views.generic import ListView, DetailView, TemplateView

from django.shortcuts import get_object_or_404, render

from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'home.html')

#def contacts(request):
#   return render(request, 'contacts.html')

class ProductListView(ListView):
    model = Product

    #catalog/blog_list.html

class ProductDetailView(DetailView):
    model = Product

class ContactView(TemplateView):
    template_name = "catalog/contacts.html"

#def product_list(request):
#    products = Product.objects.all()
#    context = {"products": products}
#    return render(request, 'blog_list.html', context)

#def product_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
#    context = {"product": product}
#    return render(request, 'product_detail.html', context)

