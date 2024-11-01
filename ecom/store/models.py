from django.db import models
import datetime
# Create your models here.

#Categories of products
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


#Customer Model
class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    Phone_num=models.CharField(max_length=15)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.Last_name}"


#Products Model
class Product(models.Model):
    Name=models.CharField(max_length=100)
    Price=models.DecimalField(default=0,decimal_places=2,max_digits=10)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    Description=models.CharField(max_length=250,default='',blank=True,null=True)
    Image=models.ImageField(upload_to='uploads/product/')


    def __str__(self):
        return self.Name

#Order Models
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=15,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product

