from django.contrib import admin
from.models import *

class AreaAdmin(admin.ModelAdmin):
    list_display = ['area_id','area_name']
    list_filter = ['area_name']
admin.site.register(Area,AreaAdmin)


# from django.utils.safestring import mark_safe
# class StoreAdmin(admin.ModelAdmin):
#     list_display = [
#         'store_id',
#         'store_name',
#         'address',
#         'price',
#         'image',
#    ]
#     def image(self, obj):
#      return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.photo.url))
# admin.site.register(Store,StoreAdmin)


class AreaStoreAdmin(admin.ModelAdmin):
    list_display = [
        'area',
        'store',
    ]

admin.site.register(AreaStore,AreaStoreAdmin)
admin.site.register(Store)
admin.site.register(Tag)
admin.site.register(StoreTag)


