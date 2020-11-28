from django.utils.translation import ugettext_lazy as _

from django.db import models


class Category(models.Model):
    name = models.CharField(_('Title'), max_length=150, db_index=True)
    slug = models.SlugField(_('Slug'), max_length=150, unique=True, db_index=True)
    order = models.PositiveIntegerField(_('Order'), default=1)

    class Meta:
        ordering = ['order']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"),
                                 related_name='products', on_delete=models.CASCADE)
    name = models.CharField(_('Title'), max_length=512, db_index=True)
    slug = models.SlugField(_('Slug'), max_length=150, unique=True, db_index=True)
    description = models.TextField(_('Description'))
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    available = models.BooleanField(_('Available'), default=True)
    stock = models.PositiveIntegerField(_('Stock'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name
