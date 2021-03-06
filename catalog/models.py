from __future__ import print_function
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator

class Category(models.Model):
  name = models.CharField(max_length=200, db_index=True)
  slug = models.SlugField(max_length=200, db_index=True, unique=True)
  image = models.FileField(validators=[FileExtensionValidator(['svg', 'png'])], null=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
    
  def __str__(self) -> str:
    return self.name

  def get_absolute_url(self) -> str:
    return reverse('catalog:category_detail_view', args=[str(self.slug)])


def get_uplaod_file_name(slug) -> str:
  return f'product_images/{slug}'

class Product(models.Model):
  
  def upload_to(self, *args):
    image_path = f'product_images/{self.slug}_/{args[0]}'
    return image_path

  category = models.ForeignKey(
      'Category', on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, db_index=True)

  slug = models.SlugField(max_length=200, db_index=True, unique=True)
  material = models.CharField(max_length=200, null=True)
  width = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  height = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  thickness = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  weight = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  image = models.FileField(blank=True, upload_to=upload_to)
  description = models.CharField(max_length=125, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.PositiveIntegerField()
  available = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created']
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'

  def get_absolute_url(self):
    return reverse('catalog:item_detail_view', args=[str(self.slug)])

  def __str__(self) -> str:
    return self.name

class PostProductImage(models.Model):

  def upload_to(self, *args) -> str:
    image_path = f'product_images/{self.prod.slug}_/{args[0]}'
    return image_path

  prod = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
  images = models.FileField(upload_to=upload_to)

  def __str__(self) -> str:
    return str(self.prod.slug)