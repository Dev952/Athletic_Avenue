from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Date_joined = models.DateField()

    def __str__(self):
      return self.Name

class Country(models.Model):
    Name = models.CharField(max_length=40)
    def __str__(self):
     return self.Name

class State(models.Model):
   Country = models.ForeignKey(Country,on_delete=models.CASCADE)
   Name = models.CharField(max_length=40)

   def __str__(self):
       return self.Name

class City(models.Model):
   State = models.ForeignKey(State,on_delete=models.CASCADE)
   Name = models.CharField(max_length=40)

   def __str__(self):
       return self.Name

class UserProfile(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    DOB = models.DateField()
    Address = models.TextField(max_length=300)
    Phone_no = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='userprofilephotos')

    def user_profile(self):
        return mark_safe('<img src="{}" width = "100" />'.format(self.Image.url))


class SportCategory(models.Model):
    Category_name = models.CharField(max_length=40)


    def __str__(self):
      return self.Category_name

class Equipment(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Category = models.ForeignKey(SportCategory,on_delete=models.CASCADE)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Image = models.ImageField(upload_to='equipmentphotos')

    def equipment(self):
        return mark_safe('<img src="{}" width = "100" />'.format(self.Image.url))


class Productcart(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    Price = models.FloatField()
    Quantity = models.IntegerField()




class Order(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Productcart, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Total_price = models.BigIntegerField()
    Order_date = models.DateField()
    Delivery_date = models.DateField()
    Status = models.CharField(max_length=30,choices=[('pending','Pending'),('shipped','Shipped'),
                                       ('delivered','Delivered')],default='Pending')


class Payment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.BigIntegerField()
    Payment_mode = models.CharField(max_length=30,choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'),
                     ('other', 'Other')])


class Feedback(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Rating = models.FloatField()
    Comment = models.CharField(max_length=50)


class Complain(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Subject = models.CharField(max_length=30,choices=[('delivery issues', 'Delivery issues'), ('payment issues', 'Payment issues'),
                     ('other', 'Other')])
    Complaint_date = models.DateTimeField()
