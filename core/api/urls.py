from django.urls import path
from core.api.views import CategoriesList, CategoriesDetails, EquipementsList, EquipementsDetails

urlpatterns = [
  path('categories/list/', CategoriesList.as_view(), name='CategoriesList'),
  path('categories/<int:pk>', CategoriesDetails.as_view(), name='categories-details'),
  path('equipements/list/',EquipementsList.as_view(), name='EquipementsList'),
  path('equipements/<int:pk>', EquipementsDetails.as_view(), name='equipements-details'),
]