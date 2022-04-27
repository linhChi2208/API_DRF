from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from core.models import Categories, Equipements


# class CategoriesAdmin(admin.ModelAdmin):
#   list_display = ['name','parent']




class EquipementsAdmin(admin.ModelAdmin):
  list_display = ['name','quantity']



admin.site.register(Categories, MPTTModelAdmin)
admin.site.register(Equipements, EquipementsAdmin)
