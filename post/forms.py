from django import forms
from .models import Message, Subscriber

class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email']

        labels = {'email':''}

        widgets = {
            'email':forms.EmailInput(attrs={
                'class':'w-full my-2 rounded-sm p-2 placeholder:text-xs placeholder:font-light placeholder:tracking-wider md:w-2/3',
                'placeholder':'Your email here',
                'required': True,
            })
        }

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['name', 'company', 'email', 'subject', 'message']

        labels = {
            'name':'',
            'company':'',
            'email':'',
            'subject':'',
            'message':'',
        }

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'placeholder':'Your name',
                'required': True,
                }),
            'company':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'placeholder':'Your company',
                'required':True,
                }),
            'email':forms.EmailInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'placeholder':'Your email',
                'required':True,
                }),
            'subject':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'placeholder':'Your subject',
                'required':True,
                }),
            'message':forms.Textarea(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light h-48',
                'placeholder':'Your message',
                'required':True,
                }),
        }
