from django import forms
from .models import Getdate

class DataForm(forms.ModelForm):
    
    class Meta:
        model = Getdate
        fields = ['name' , 'user_email' , 'title' , 'description']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': 'Yeganeh Khayyat' , 'rows':1 , 'size' :12}),
            'user_email' : forms.EmailInput(attrs={'class' : 'form-control' ,'placeholder' : 'yeganeh.khayyat@gmail.com' , 'size' :12}),
            'title' : forms.TextInput(attrs={'class' : 'form-control' ,'placeholder' : 'Telegram bots', 'size' :12}),
            'description' : forms.Textarea(attrs={'class' : 'form-control' ,'placeholder' : 'Enter here...'  , 'rows' : 5}),
        }