from django.shortcuts import render , HttpResponse

# Create your views here.
# def index(request):
#     # return HttpResponse("hello world")
#     return HttpResponse("hello kavya")


def display(request):
    return HttpResponse('''
    <nav style="
        background-color:red;display:flex;align-items:center;justify-content:space-between; padding:20px 40px; margin-bottom:2px;font-family:sans-serif
    ">
        <img src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/portal/static-assets/images/swiggy_logo_white.png"
        style="width:150px;height:100%">
        <div style="display:flex; align-items:center; gap:75px;">

            <a href="#" style="color:white; text-decoration:none; font-weight:750;">Swiggy Corporate </a>

            <a href="#" style="color:white; text-decoration:none; font-weight:750;">Partner With Us</a>

            <button style="
                padding:10px 20px;border-radius:8px;border:1px solid white;background-color:red;color:white;font-weight:700; cursor:pointer ">
                Get the App
            </button>

            <button style="
                padding:10px 20px;border-radius:12px;background-color:black;color:white;border:none;font-weight:700;cursor:pointer">
                Sign in
            </button>

        </div>
    </nav>
                        <div style=background-color:red;display:flex;justify-content:space-between;
                        align-items:center;padding:20px 40px;margin-bottom:10px">
                        <img src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/portal/testing/seo-home/Veggies_new.png" 
                        style="width:20%;height:auto;background-color:red;" > 

                         <div style="text-align:center; color:black; margin-top:20px;font-family:sans-serif">
                        <h1 style="color:white;margin-right:370px;margin-top:70px;font-size:50px;font-weight:700">
                       Order food & groceries.<br>
                        Discover best restaurants.<br>
                       Swiggy it!
                         </h1>
                        <div>
                        <img src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/portal/testing/seo-home/Sushi_replace.png" style="width:20%;height:auto;margin-left:1074px;margin-top:-260px;background-color:red;">
                        </div>
                        </div>
                        </div>
    ''')