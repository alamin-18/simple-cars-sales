from django.db import models
from bands.models import Bands

# Create your models here.
class Cars(models.Model):
    model_name = models.CharField(max_length=150)
    band = models.ForeignKey(Bands,on_delete=models.CASCADE)
    des = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.model_name
    
class Comments(models.Model):
    cars = models.ForeignKey(Cars,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    body= models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.name}"