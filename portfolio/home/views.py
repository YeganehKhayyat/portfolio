from django.shortcuts import render , redirect
from .forms import DataForm
from django.shortcuts import render
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(requests):
    return render(requests, "home/index.html")

def projects(requests):
    return render(requests, "home/projects.html")

def contact(requests):
 
    if requests.POST:
            form = DataForm(requests.POST)
            if form.is_valid():
                contact_form = form.save()                
                email = EmailMessage(
                    subject=f"New message : {contact_form.title}",
                    body=(
                        f"Name: {contact_form.name}\n"
                        f"User email: {contact_form.user_email}\n\n"
                        f"Message: {contact_form.description}"
                    ),
                    from_email=settings.EMAIL_HOST_USER,
                    to = [settings.CONTACT_EMAIL],
                    reply_to=[contact_form.user_email],
                )
                
                email.send(fail_silently=False)
                if email.send:
                    messages.success(requests, "Your request sent successfully")
                    
                return redirect("contact")
                
    else:
        form = DataForm()
        return render(requests , "home/contact.html", {"form" : form})
    