from django.urls import path
from betel import views

urlpatterns = [

    path('', views.index, name='index'),

]