from django.db import models

class product(models.Model):
   # product_id = models.AutoField()
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500)
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key="True")
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id=models.AutoField(primary_key="True")
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key="True")
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."


