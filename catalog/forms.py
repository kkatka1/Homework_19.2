from django import forms
from django.forms import BooleanField, ModelForm
from django.views.generic import CreateView, UpdateView

from catalog.models import Product, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция','радар']

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('название продукта не подходит')

        return cleaned_data


    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция','радар']

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('описание продукта не подходит')

        return cleaned_data

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

