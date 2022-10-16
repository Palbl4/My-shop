from django.contrib import admin

# Register your models here.
from authapp.models import ShopUserProfile, ShopUser
from mainapp.models import ListOfProduct, Sex, SizeRange

admin.site.register(ListOfProduct)
admin.site.register(Sex)
admin.site.register(SizeRange)
admin.site.register(ShopUser)
admin.site.register(ShopUserProfile)
