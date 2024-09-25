import os
import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product
PATH = "catalog/catalog_data.json"

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(PATH, encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        with open(PATH, encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "catalog.product"]

    # Здесь мы получаем данные из фикстурв с продуктами


    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        for item in Command.json_read_categories():
            category_data = item["fields"]
            category_for_create.append(Category(id=item["pk"], **category_data))

        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for item in Command.json_read_products():
            product_data = item["fields"]
            category = Category.objects.get(pk=product_data.pop("category"))
            product_for_create.append(
                Product(id=item["pk"], category=category, **product_data))

        Product.objects.bulk_create(product_for_create)

        print ('ok')