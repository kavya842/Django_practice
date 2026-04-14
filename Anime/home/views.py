from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')
def one_piece(request):
    return render(request,'one_piece.html')
def naruto(request):
    return render(request,'naruto.html')
def note(request):
    return render(request,'note.html')
def don_da_don(request):
    return render(request,'don_da_don.html')