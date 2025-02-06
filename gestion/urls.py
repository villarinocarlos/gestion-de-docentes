from django.urls import path
from . import views

from django.urls import path
from .views import login_view, pantalla_principal, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('pantalla_principal/', pantalla_principal, name='pantalla_principal'),
]


path('logout/', logout_view, name='logout'),
