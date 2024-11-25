from django.db import models
from django.db.models import SET_NULL

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True, verbose_name="Описание", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]




class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        blank=True, verbose_name="Описание", help_text="Введите описание товара"
    )
    image = models.ImageField(
        upload_to="products/image/",
        blank=True,
        null=True,
        verbose_name="Изображение (превью)",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберете категорию товара",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Введите цену товара",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    owner = models.ForeignKey(User, verbose_name='владелец', help_text='укажите владельца', on_delete=SET_NULL,
                              blank=True, null=True)

    is_published = models.BooleanField(default=False, verbose_name='статус')

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]
        permissions = [
            ("can_unpublish_product", "can unpublish product"),("change_description", "Can change description"),
                                                                ("change_category", "Can change category")
        ]
class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version_number = models.IntegerField(verbose_name='номер версии')

    version_name = models.CharField(max_length=150, verbose_name='название версии')

    is_current = models.BooleanField(default=False, verbose_name='признак текущей версии')

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["-is_current", "-version_number"]
        constraints = [
            models.UniqueConstraint(fields=['product', 'is_current'],
                                    condition=models.Q(is_current=True),
                                    name='unique_active_version')
        ]

    def __str__(self):
        return f'{self.version_name} - {self.version_number}'




