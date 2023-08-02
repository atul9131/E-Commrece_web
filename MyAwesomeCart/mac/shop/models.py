from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_date = models.DateTimeField()
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    product_price = models.FloatField(default=0)
    product_image = models.ImageField(upload_to='shop/images', default="")
    # product_category = models.CharField(max_length=50)
    

    def __str__(self):
        return self.product_name




class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=10,default="")
    desc = models.CharField(max_length=1000, default='')
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name
    

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default=0)
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateTimeField(auto_now_add= True,)

    def __str__(self):
        return self.update_desc[0:7] + "..."

