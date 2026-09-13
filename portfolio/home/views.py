from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import DataForm

# Create your views here.
def home(requests):
    return render(requests, "home/index.html")

def projects(requests):
    return render(requests, "home/projects.html")

def contact(requests):
    
    if requests.POST:
            form = DataForm(requests.POST)
            if form.is_valid():
                form.save()
                return render(requests, "home/contact.html")
            
            else:
                form = DataForm()
                
                data = {
                'form' : form
                        }
                return render(requests , "home/contact.html", context=data)
            
    else:
        form = DataForm()
        data = {
            'form' : form
                }
        return render(requests , "home/contact.html", context=data)