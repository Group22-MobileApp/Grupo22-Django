from django.db import models

# Create your models here.

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='item_images/', default='item_images/default.jpg')
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    seller = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    is_sold = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item'
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ['name']
        
    def has_perm(self, perm, obj=None):
        return self.is_admin