from django.shortcuts import render

def index(request):
    return render(request,'reserv_service/index.html')
