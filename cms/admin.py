from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe
# Register your models here.
class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title','cms_text','cms_css','get_image')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title','get_image','cms_text','cms_css')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src ="{obj.cms_img.url}" width = "80px">')


admin.site.register(CmsSlider,CmsAdmin)
