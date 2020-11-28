from django.utils.translation import ugettext_lazy as _
from django.db import models


def slider_image_directory_path(instance, filename):
    return 'slider_{0}/{1}'.format(instance.id, filename)


class Group(models.Model):
    name = models.CharField(_('Title'), max_length=50)
    slug = models.SlugField(_('Slug'), max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    def __str__(self):
        return self.name


class Slider(models.Model):
    group = models.ForeignKey(Group, verbose_name=_("Group"), related_name='sliders', on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=50)
    btn_text = models.CharField(_('Button text'), max_length=50, blank=True, null=True)
    link = models.URLField(_('Link'), max_length=250, blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to=slider_image_directory_path)
    order = models.PositiveIntegerField(_('Order'), default=1)
    is_visible = models.BooleanField(_('Is visible'), default=True)

    class Meta:
        ordering = ['order']
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')

    def __str__(self):
        return self.title
