from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Booking(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name="customer",null=False)
    email= models.EmailField(null= False,blank=False)
    phone = models.IntegerField()
    number_of_guests= models.IntegerField()
    date =models.DateField()
    time= models.TimeField()
    special_request= models.TextField(max_length=200)
    updated_on=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

class Comment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name="client")
    email=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_email")
    post= models.TextField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)
    approved= models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.post} by {self.name}"

