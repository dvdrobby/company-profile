from django import forms
from post.models import Post, Contact, Message

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'company', 'email', 'subject','message', 'status_message']

        widgets={
            'name':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'readonly' : True, 
                }),
            'company':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'readonly' : True, 
                }),
            'email':forms.EmailInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'readonly' : True, 
                }),
            'subject':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'readonly' : True, 
                }),
            'message':forms.Textarea(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light h-48',
                'readonly' : True, 
                }),
            'status_message':forms.Select(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'readonly' : False, 
                }),
        }

class ContactModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['company_name', 'address', 'email', 'phone', 'mobile_phone', 'site_map_url', 'iframe', 'facebook_url', 'linkedin_url', 'instagram_url']

        labels = {
            'title':'',
            'location':'',
            'content':'',
            'picture':'',
            'category':'',
        }

        widgets = {
            'company_name':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'address':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'email':forms.EmailInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'phone':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'mobile_phone':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'site_map_url':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'iframe':forms.Textarea(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light h-48',
                }),
            'facebook_url':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'linkedin_url':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'instagram_url':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
        }

    
class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'location', 'picture', 'content', 'category']

        # labels = {
        #     'title':'',
        #     'location':'',
        #     'content':'',
        #     'picture':'',
        #     'category':'',
        # }

        widgets = {
            'title':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'location':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'picture':forms.FileInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'content':forms.Textarea(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light h-48',
                }),
            'category':forms.Select(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
        }
