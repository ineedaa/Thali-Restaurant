from restaurant.views import * 
from django.urls import path, include


urlpatterns = [
    path('',index,name='index'),
    path('booking/',booking,name="booking"),
    path('accounts/',include('allauth.urls')),
]