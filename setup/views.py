from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from datetime import datetime

from post.models import Message, Contact, Post, Category, About
from .forms import PostModelForm, ContactModelForm, MessageModelForm, AboutModelForm, CategoryModelForm


class IndexListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'setup/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        event_category = get_object_or_404(Category, title__icontains='event')
        events = Post.objects.filter(category=event_category)
        return events.order_by('-publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product_category = get_object_or_404(Category, title__icontains='product')
        products = Post.objects.filter(category=product_category)      

        project_category = get_object_or_404(Category, title__icontains='project')
        projects = Post.objects.filter(category=project_category)      
             


        context['title']= 'Dashboard'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']=Contact.objects.all()
        context['abouts']=About.objects.all()

        context['product_count']=products.count()
        context['project_count']=projects.count()

        return context
    

class ContactListView(ListView):
    model = Contact
    template_name = 'arcotama_admin.html'
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model= Contact
    form_class = ContactModelForm
    template_name = 'setup/contact_edit.html'
    success_url = reverse_lazy('setup:index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Edit Contact'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
    
class AboutUpdateView(LoginRequiredMixin, UpdateView):
    model= About
    form_class = AboutModelForm
    template_name = 'setup/about_edit.html'
    success_url = reverse_lazy('setup:index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Edit About'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model= Post
    form_class = PostModelForm
    template_name = 'setup/post_edit.html'
    success_url = reverse_lazy('setup:post')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Edit Post'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'setup/post_list.html'
    context_object_name = 'posts'    
    ordering = '-publish'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Post List'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'setup/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('setup:post')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Post List'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'setup/create_post.html'
    success_url = reverse_lazy('setup:post')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Add Post'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
    
    def form_invalid(self, form) :
        print(form.errors)
        return super().form_invalid(form)
    
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'setup/message_list.html'
    context_object_name = 'messages'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
    
class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageModelForm
    template_name = 'setup/message_update.html'
    success_url = reverse_lazy('setup:messages')


    def get_context_data(self, *args, **kwargs):
        
        context = super().get_context_data(*args, **kwargs)
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
      
    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
           

        data = kwargs['instance'].__dict__

        if data['status_message'] == 'unread':
                kwargs['instance'].__dict__['status_message'] = 'read'

        if hasattr(self, "object"):
            kwargs.update({"instance": self.object})
    
        

        return kwargs
    
    def post(self, request, *args, **kwargs):
        form = super().post(request, *args, **kwargs)

        return form

    def form_valid(self, form):
        return super().form_valid(form)
    
    
    
class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'setup/message_detail.html'
    context_object_name = 'msg'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Add Post'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
    
class CategoryListView(LoginRequiredMixin, ListView):
    model =Category
    template_name = 'setup/cat_list.html'
    context_object_name = 'categories'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Add Post'
        context['message_count'] = Message.objects.filter(status_message ='unread').count()
        context['datetime']= datetime.now().strftime("%A, %d %B %Y ")
        context['contact']= Contact.objects.all()
        context['abouts'] = About.objects.all()

        return context
    
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class= CategoryModelForm
    template_name = 'setup/cat_edit.html'
    success_url = reverse_lazy('setup:category')