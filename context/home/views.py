from django.shortcuts import render

# Create your views here.
students=[
    {'name':"Kavya",'age':21,"gender":"female",'phone':8919951981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Mani",'age':20,"gender":"Male",'phone':9652738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Sailaja",'age':20,"gender":"Female",'phone':5692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Ravi",'age':21,"gender":"Male",'phone':7819951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Revathi",'age':21,"gender":"female",'phone':8916651981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Sunny",'age':21,"gender":"Male",'phone':7719951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Srujana",'age':20,"gender":"Female",'phone':8852738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
      {'name':"Srinu",'age':21,"gender":"Male",'phone':8919959981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Bindu",'age':20,"gender":"Female",'phone':7692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Sravan",'age':20,"gender":"Male",'phone':9982738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Pranavi",'age':21,"gender":"Female",'phone':7876951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
    {'name':"Harshith",'age':20,"gender":"Male",'phone':8692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
     {'name':"Kavya",'age':21,"gender":"female",'phone':8919951981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Mani",'age':20,"gender":"Male",'phone':9652738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Sailaja",'age':20,"gender":"Female",'phone':5692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Ravi",'age':21,"gender":"Male",'phone':7819951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Revathi",'age':21,"gender":"female",'phone':8916651981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Sunny",'age':21,"gender":"Male",'phone':7719951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Srujana",'age':20,"gender":"Female",'phone':8852738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
      {'name':"Srinu",'age':21,"gender":"Male",'phone':8919959981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Bindu",'age':20,"gender":"Female",'phone':7692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Sravan",'age':20,"gender":"Male",'phone':9982738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Pranavi",'age':21,"gender":"Female",'phone':7876951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
    {'name':"Harshith",'age':20,"gender":"Male",'phone':8692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
     {'name':"Kavya",'age':21,"gender":"female",'phone':8919951981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Mani",'age':20,"gender":"Male",'phone':9652738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Sailaja",'age':20,"gender":"Female",'phone':5692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Ravi",'age':21,"gender":"Male",'phone':7819951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Revathi",'age':21,"gender":"female",'phone':8916651981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Sunny",'age':21,"gender":"Male",'phone':7719951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Srujana",'age':20,"gender":"Female",'phone':8852738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
      {'name':"Srinu",'age':21,"gender":"Male",'phone':8919959981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Bindu",'age':20,"gender":"Female",'phone':7692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Sravan",'age':20,"gender":"Male",'phone':9982738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Pranavi",'age':21,"gender":"Female",'phone':7876951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
    {'name':"Harshith",'age':20,"gender":"Male",'phone':8692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
     {'name':"Kavya",'age':21,"gender":"female",'phone':8919951981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Mani",'age':20,"gender":"Male",'phone':9652738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Sailaja",'age':20,"gender":"Female",'phone':5692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Ravi",'age':21,"gender":"Male",'phone':7819951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Revathi",'age':21,"gender":"female",'phone':8916651981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Sunny",'age':21,"gender":"Male",'phone':7719951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
     {'name':"Srujana",'age':20,"gender":"Female",'phone':8852738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
      {'name':"Srinu",'age':21,"gender":"Male",'phone':8919959981,'location':"ongole",'cgpa':9.1,'stream':'IT','YOP':2026},
    {'name':"Bindu",'age':20,"gender":"Female",'phone':7692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},
    {'name':"Sravan",'age':20,"gender":"Male",'phone':9982738424,'location':"kamepalli",'cgpa':9.5,'stream':'CSE','YOP':2025},
    {'name':"Pranavi",'age':21,"gender":"Female",'phone':7876951981,'location':"ponnaluru",'cgpa':8.9,'stream':'ECE','YOP':2026},
    {'name':"Harshith",'age':20,"gender":"Male",'phone':8692738424,'location':"kamepalli",'cgpa':9.2,'stream':'AIDS','YOP':2026},

    
]

def index(request):
    context={
        'data':students
    }
    return render(request,'home.html',context)
def cards(request):
    context={
        'data':students
    }
    return render(request,'cards.html',context)