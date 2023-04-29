from restaurant.views import * 
from django.urls import path, include


urlpatterns = [
    path('',index,name='index'),
    path('booking/',booking,name="booking"),
    path('myaccount/',myaccount,name="myaccount"),
    path("accounts/login/", login_view, name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    path("menu/",menu,name="menu"),
    path('edit_booking/<int:booking_id>/',edit_booking,name="edit_booking"),
    path('myaccount/<int:booking_id>/delete/',delete_booking,name="delete_booking"),
]