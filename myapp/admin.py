from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class showuser(admin.ModelAdmin):
    list_display = ['Name','Email','Password','Date_joined']

@admin.register(Country)
class showcountry(admin.ModelAdmin):
    list_display = ['Name']

@admin.register(State)
class showstate(admin.ModelAdmin):
    list_display = ['Country','Name']

@admin.register(City)
class showcity(admin.ModelAdmin):
    list_display = ['State','Name']

@admin.register(UserProfile)
class showuserprofile(admin.ModelAdmin):
    list_display = ['User','DOB','Address','Phone_no','user_profile']

@admin.register(SportCategory)
class showsportcategory(admin.ModelAdmin):
    list_display = ['Category_name']

@admin.register(Equipment)
class showequipment(admin.ModelAdmin):
    list_display = ['User','Category','Price','Quantity','equipment']

@admin.register(Productcart)
class showproductcart(admin.ModelAdmin):
    list_display = ['User','Equipment','Price','Quantity']

@admin.register(Order)
class showorder(admin.ModelAdmin):
    list_display = ['User','Equipment','Quantity','Total_price','Order_date',
                    'Delivery_date','Status']

@admin.register(Payment)
class showpayment(admin.ModelAdmin):
    list_display = ['User','Amount','Payment_mode']

@admin.register(Feedback)
class showfeedback(admin.ModelAdmin):
    list_display = ['User','Rating','Comment']

@admin.register(Complain)
class showcomplain(admin.ModelAdmin):
    list_display = ['Name','Email','Subject','Complaint_date']