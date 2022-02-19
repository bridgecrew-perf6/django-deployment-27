from app1 import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'app1'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    path('login/',views.user_login,name="user_login"),
]