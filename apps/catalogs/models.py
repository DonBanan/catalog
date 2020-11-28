from django.utils.translation import ugettext_lazy as _

from django.db import models


class Category(models.Model):
    name = models.CharField(_('Title'), max_length=150, db_index=True)
    slug = models.SlugField(_('Slug'), max_length=150, unique=True, db_index=True)
    order = models.PositiveIntegerField(_('Order'), default=1)

    class Meta:
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
