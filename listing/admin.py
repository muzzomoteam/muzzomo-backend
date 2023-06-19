from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','feature']

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id','floor']

admin.site.register(Location)
admin.site.register(Feature , FeatureAdmin)
admin.site.register(Product , ProductAdmin)
admin.site.register(AmenitiesAdmin)
admin.site.register(AmenitiesAddListing)
admin.site.register(WishList)
admin.site.register(ProducttRate)
admin.site.register(CustomUser)
admin.site.register(Agent)
admin.site.register(Customer)
admin.site.register(Expert)
admin.site.register(AgentRate)
