from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')

def stranger_things(request):
    return render(request,'stranger_things.html')

def breaking_bads(request):
    return render(request,'breaking_bads.html')

def surya(request):
    return render(request,'surya.html')

def arafta(request):
    return render(request,'arafta.html')


