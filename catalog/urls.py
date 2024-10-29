from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, home, ContactView

app_name = CatalogConfig.name

urlpatterns = [
    path ('', ProductListView.as_view(), name='product_list'),
    path ('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path("home", home, name="home"),
    path("contacts/", ContactView.as_view(), name="contact"),
]