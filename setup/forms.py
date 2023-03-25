from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from post.models import Post, Contact, Message, About, Category

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
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        
        model = Post
        fields = ['title', 'location', 'picture', 'content', 'category']

        labels = {
            'picture': 'Picture (800px x 600px) :'
        }


        widgets = {
            'title':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'location':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'picture':forms.FileInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'required':False,
                }),
            'content':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'category':forms.Select(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
        }

class AboutModelForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        
        model = About
        fields = ['content', 'picture']


        widgets = {
            'content':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'picture':forms.FileInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                'required':False,
                }),
        }

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'heading', 'caption']

        labels = {
            'title':'',
            'heading':'',
            'caption':'',
        }

        widgets = {
            'title':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'heading':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
            'caption':forms.TextInput(attrs={
                'class':'p-3 bg-white text-sm font-light rounded-sm w-full placeholder:text-sm placeholder:font-light',
                }),
        }