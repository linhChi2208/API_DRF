from rest_framework import serializers
from core.models import Categories, Equipements

class CategoriesSerializer(serializers.ModelSerializer):
  class Meta:
      model = Categories
      exclude = ('lft', 'rght', 'tree_id', 'level')



class EquipementsSerializer(serializers.ModelSerializer):
  categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = Equipements
    fields = '__all__'


class EquipementsDetailSerializer(serializers.ModelSerializer):
  categories = CategoriesSerializer(many=True, read_only=True)
  class Meta:
    model = Equipements
    fields = '__all__'