from django.contrib import admin
from .models import productMainModel,productColourModel,productImageModel
# Register your models here.
mymodels=[productMainModel,productColourModel,productImageModel]

admin.site.register(mymodels)

