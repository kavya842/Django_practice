from django.shortcuts import render

# Create your views here.
def book_home(request):
    return render(request,"book_home.html")