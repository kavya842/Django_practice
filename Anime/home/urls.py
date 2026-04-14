from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index),
    path('one_piece',views.one_piece),
    path('naruto',views.naruto),
    path('note',views.note),
    path('don_da_don',views.don_da_don),
]