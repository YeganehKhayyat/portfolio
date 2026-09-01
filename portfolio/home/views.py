from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(requests):
    return render(requests, "home/index.html")

def projects(requests):
    return render(requests, "home/projects.html")

def contact(requests):
    
    return render(requests,"home/contact.html")