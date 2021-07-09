from rest_framework import serializers
from .models import client,product


class clientSerializer(serializers.ModelSerializer):

    class Meta:
        model=client
        fields=['emp_id','name','email','phone','address','city']

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model=product
        fields=['name','product_id','catagory','description','Original_price','Discounted_price']
