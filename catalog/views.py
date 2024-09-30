from django.shortcuts import get_object_or_404, render

from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'templates/base.html', context)

