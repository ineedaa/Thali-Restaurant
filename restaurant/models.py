from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from django.forms.widgets import DateInput



# Create your models here.
class Booking(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name="customer",null=False)
    email= models.EmailField(null= False,blank=False)
    phone = PhoneNumberField(null=False,blank=False)
    number_of_guests= models.IntegerField()
    date =models.DateField()
    time= models.CharField(max_length=10)
    special_request= models.TextField(max_length=200)
    updated_on=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.name.username}"

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['phone','number_of_guests','date','time','special_request',]
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }






