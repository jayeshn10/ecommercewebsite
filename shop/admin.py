from django.contrib import admin
from .models import contactdata, gallery, blogmod, Shopproduct, order, orderiteminfo

# Register your models here.

admin.site.register(contactdata)
admin.site.register(gallery)
admin.site.register(blogmod)
admin.site.register(Shopproduct)
admin.site.register(order)
admin.site.register(orderiteminfo)

