from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import Group, Slider


register = template.Library()


@register.simple_tag(takes_context=True)
def sliders(context, group, tpl='sliders/sliders.html'):
    tpl_context = {}
    try:
        group = Group.objects.get(slug=group)
        sliders = Slider.objects.filter(is_visible=True, group=group)
    except ObjectDoesNotExist:
        group = False
        sliders = False

    if sliders and group:
        tpl_context['group'] = group
        tpl_context['sliders'] = sliders

    t = template.loader.get_template(tpl)
    return t.render(tpl_context, request=context['request'])
