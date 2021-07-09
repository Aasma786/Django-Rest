from django.db import models


class client(models.Model):
    emp_id=models.IntegerField()
    name=models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone= models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name


catagory_choices=(
    (0,'Sofa'),
    (1,'Chair'),
    (2,'Table'),
    (3,'Dining Table'),
    (4,'Bed'),
    (5,'Not specified'),
)
class product(models.Model):
    name = models.CharField(max_length=50)
    product_id=models.IntegerField()
    catagory = models.IntegerField(choices=catagory_choices)
    description = models.CharField(max_length=250,default='')
    Original_price= models.IntegerField(default=0)
    Discounted_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name