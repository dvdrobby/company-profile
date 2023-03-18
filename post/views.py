from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin

from .models import About, Contact,Category, Post
from .forms import MessageForm

def admin(request):
    return render(request,'arcotama_admin.html')

#Post List View
class Product(ListView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, title__icontains = 'product')
        query = Post.objects.filter(category = category)
        return query.order_by('-publish')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category = get_object_or_404(Category, title__icontains = 'product')
        context['category'] = category
        context['contact'] = Contact.objects.all()
        return context


class Project(ListView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, title__icontains = 'project')
        query = Post.objects.filter(category = category)
        return query.order_by('-publish')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category = get_object_or_404(Category, title__icontains = 'project')
        context['category'] = category
        context['contact'] = Contact.objects.all()
        return context


class Event(ListView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, title__icontains = 'event')
        query = Post.objects.filter(category = category)
        return query.order_by('-publish')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category = get_object_or_404(Category, title__icontains = 'event')
        context['category'] = category
        context['contact'] = Contact.objects.all()
        return context


class Index(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, title__icontains = 'product')
        query = Post.objects.filter(category = category)
        return query.order_by('-publish')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        products_category = get_object_or_404(Category, title__icontains = 'product')
        projects_category = get_object_or_404(Category, title__icontains = 'project')
        events_category = get_object_or_404(Category, title__icontains = 'event')

        products = Post.objects.filter(category = products_category).order_by('-publish')
        projects = Post.objects.filter(category = projects_category).order_by('-publish')
        events = Post.objects.filter(category = events_category)

        context['products'] = products[:3]
        context['products_count'] = products.count()
        context['projects'] = projects[:3]
        context['projects_count'] = projects.count()
        context['events'] = events
        context['events_count'] = events.count()
        context['contact'] = Contact.objects.all()
        return context

class About(ListView):
    model = About
    template_name = "about.html"

    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.all()

        return context
    

class ProductDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        products_category = get_object_or_404(Category, title__icontains = kwargs['object'].category)
        related_products = Post.objects.filter(category = products_category).exclude(slug = kwargs['object'].slug)
        context['products'] = related_products
        context['contact'] = Contact.objects.all()
        return context

class ContactView(SuccessMessageMixin, CreateView):
    form_class= MessageForm
    template_name = 'contact.html'
    success_url = '/contact/'
    success_message = 'Your message has been send successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact']=Contact.objects.all()

        return context
    
    