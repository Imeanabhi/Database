from django.urls import path
from users import views

urlpatterns = [
    path('Staff_Login',views.Staff_Login,name="Staff_Login")

]