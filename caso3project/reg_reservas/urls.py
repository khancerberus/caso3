from django.urls import path, include
from . import views

app_name = 'reg_reservas'

urlpatterns = [
    path('', views.index, name="index")
]