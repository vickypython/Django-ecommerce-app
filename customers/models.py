from django.db import models

# Create your models here.
#categories model
class Categorie(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField('input your dec')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    categorie=models.ForeignKey(Categorie,related_name='products', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
