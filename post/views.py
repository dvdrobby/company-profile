from django.shortcuts import render


def index(request):
    return render(request,'home.html')

def admin(request):
    return render(request,'arcotama_admin.html')

def post(request):
    return render(request,'news.html')

def contact(request):
    return render(request,'contact.html')