from django.db import models


# Create your models here.
class productMainModel(models.Model):
    title=models.CharField(max_length=22)
    description=models.TextField()
    price=models.IntegerField()
class productColourModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    colour=models.CharField(max_length=30)

class productImageModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=None)