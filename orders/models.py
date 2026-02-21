from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class Orders(models.Model):

    #atributos
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"order {self.id} by {self.user}"
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return f"order {self.order} - {self.product}"