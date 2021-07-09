from django.contrib import admin
from .models import client,product

@admin.register(client)
class clientAdmin(admin.ModelAdmin):
    List_display=['emp_id','name','email','phone','address','city']

@admin.register(product)
class producttAdmin(admin.ModelAdmin):
    List_display=['name','product_id','catagory','description','Original_price','Discounted_price']