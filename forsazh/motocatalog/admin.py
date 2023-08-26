from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
# admin.site.register(Product)

admin.site.register(CoolingSystem)
admin.site.register(Transmission)
admin.site.register(LaunchSystem)
admin.site.register(FrontBrakes)
admin.site.register(RearBrakes)

# admin.site.register(Mototechnics)

admin.site.register(Moped)
admin.site.register(Scooter)
admin.site.register(QuadBike)
admin.site.register(PitBike)
admin.site.register(CrossTechnique)

admin.site.register(Gallery)

class GalleryInline(admin.TabularInline):
    fk_name = 'productftf'
    model = Gallery

class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]