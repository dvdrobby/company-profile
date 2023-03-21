from django import forms

from captcha.fields import ReCaptchaField

from .models import Message


class MessageForm(forms.ModelForm):
    captcha = ReCaptchaField(label='')
    class Meta:
        model = Message
        fields = ['name', 'company', 'email', 'subject', 'message', 'captcha']

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
