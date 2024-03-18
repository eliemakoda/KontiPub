from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import Index, About, Beauty, AdsDetail, Contact, Evenement, Login,Register, Pricing,Restauration, Nuit
urlpatterns = [
    path('', Index, name="index" ),
    path('about', About, name="about" ),
    path('adsdetails/<int:id>', AdsDetail, name="adsdetails" ),
    path('beauty', Beauty, name="beauty" ),
    path('contact', Contact, name="contact" ),
    path('event', Evenement, name="event" ),
    path('login', Login, name="login" ),
    path('register', Register, name="register" ),
    path('pricing', Pricing, name="pricing" ),
    path('restauration', Restauration, name="restauration" ),
    path('night', Nuit, name="night" ),
]
