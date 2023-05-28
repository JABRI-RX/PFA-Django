from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category ,related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    creatd_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "Items"
    def __str__(self):
        return f"{self.id}\t\t\t {self.name}"