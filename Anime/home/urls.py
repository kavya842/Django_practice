from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index),
    path('one_piece',views.one_piece),
    path('naruto',views.naruto),
]