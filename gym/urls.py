from django.urls import path
from gym import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('signup', views.signup, name='signup'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
]
