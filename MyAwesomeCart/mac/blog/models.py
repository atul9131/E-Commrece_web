from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.TextField(default="")
    head0= models.TextField(default="")
    chead0= models.TextField(default="")
    head1= models.TextField(default="")
    chead1= models.TextField(default="")
    head2= models.TextField(default="")
    chead2= models.TextField(default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.title
    
    