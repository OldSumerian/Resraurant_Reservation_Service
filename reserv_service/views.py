from django.shortcuts import render


def index(request):
    return render(request,'reserv_service/index.html')


def about_us(request):
    return render(request,'reserv_service/about_us.html')


def contacts(request):
    return render(request,'reserv_service/contacts.html')
