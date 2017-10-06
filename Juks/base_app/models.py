from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=50,blank=True)
    #additional
    #portfolio_site = models.URLField(blank=True)

    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.full_name

class ProductInfo(models.Model):
        name = models.CharField(max_length=50)
        price = models.DecimalField(max_digits=5, decimal_places=2)
        desc = models.TextField()
        images = models.ImageField(upload_to='images')

        def __unicode__(self):
            return self.name


# class Admins(models.Model):
#     username = models.CharField(max_length=50,blank=True)
#     password = models.CharField(max_length=50, blank=True)
#
#     def __str__(self):
#         return self.username
