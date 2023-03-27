from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    des=models.TextField(blank=True)
    image=models.ImageField(upload_to='category')
    slug=models.SlugField(max_length=250,unique=True)
    class Meta():
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('shop:product_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    des = models.TextField(blank=True)
    image = models.ImageField(upload_to='product')
    slug = models.SlugField(max_length=250, unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:prodCatDetail',args=[self.category.slug,self.slug])


    class Meta():
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)