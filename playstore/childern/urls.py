from django. urls import path
from . import views

urlpatterns=[
    path('1',views.child_home),
    path('2',views.child_c1)
]