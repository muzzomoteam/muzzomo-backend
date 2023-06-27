from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','feature']

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id','floor']

admin.site.register(Location)
admin.site.register(AgentMessage)
admin.site.register(ProductPropertyModel)
admin.site.register(ProductAmenitiesModel)
admin.site.register(ProductImageModel)
admin.site.register(WishList)
admin.site.register(ProducttRate)
admin.site.register(CustomUser)
admin.site.register(Agent)
admin.site.register(Customer)
admin.site.register(Expert)
admin.site.register(AgentRate)
