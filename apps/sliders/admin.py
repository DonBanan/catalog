from django.contrib import admin

from .models import Group, Slider


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'group', 'is_visible', 'order']
    list_filter = ['is_visible']
    list_editable = ['group', 'is_visible', 'order']


admin.site.register(Group, GroupAdmin)
admin.site.register(Slider, SliderAdmin)
