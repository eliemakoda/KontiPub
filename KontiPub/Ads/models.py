from django.db import models

# Create your models here.
class Administrateur(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField()
    password=models.CharField(max_length=50)
    
class Ads(models.Model):
    productName= models.CharField(max_length=100)
    admin= models.ForeignKey(Administrateur, on_delete=models.CASCADE)
    price= models.IntegerField()
    description=models.CharField(max_length=400)
    # feature= models.CharField(max_length=400)
    address= models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    state= models.CharField(max_length=20, default="cameroun")
    city= models.CharField(max_length=30)
    category= models.CharField(max_length=100)
    date_event=models.DateField()
    avatar=models.ImageField(upload_to='images/')
    added_date=models.DateField(auto_now_add=True)
    hour= models.TimeField()