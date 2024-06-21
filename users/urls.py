from django.contrib import admin
from django.urls import path
from users import views
urlpatterns = [
    path("Staff_Login",views.Staff,name="staff_login")
]
