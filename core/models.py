from django.db import models

from mptt.models import MPTTModel, TreeForeignKey



class Categories(MPTTModel):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField()
  description = models.CharField(max_length=255)
  photo = models.ImageField(blank=True, null=True, upload_to='image/')
  parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

  def __str__(self):
    return self.name
  
  class MPTTMeta:
        order_insertion_by = ['name']
  


class Equipements(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField()
  categories = models.ManyToManyField(Categories, related_name='categories')
  quantity = models.IntegerField()

  def __str__(self):
    return self.name


