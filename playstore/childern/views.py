from django.shortcuts import render

# Create your views here.
def child_home(request):
    return render(request,"child_home.html")

def child_c1(request):
    return render(request, "child.html")
