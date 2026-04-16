from django.urls import path
from . import views

urlpatterns=[
    path('',views.main, name="home"),
    path('2',views.stranger_things, name ="stranger_things"),
    path('3',views.breaking_bads, name="breaking_bads"),
    path('4',views.surya, name = "surya"),
    path('5',views.arafta, name="arafta"),
]