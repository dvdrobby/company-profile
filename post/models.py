from django.db import models
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

STATUS_CHOICES=(
    ('draft','Draft'),
    ('published','Published')
)

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Category Name')
    slug =models.SlugField(max_length=150, unique=True, editable=False)
    heading = models.CharField(max_length=50, verbose_name='Heading', default='None')
    caption = models.TextField(verbose_name='Caption', default='None')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(unique=True, editable=False)
    location = models.CharField(max_length=25,verbose_name="Location")
    content = RichTextUploadingField(verbose_name="Content")
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    picture = models.ImageField(upload_to='uploads/%Y/%m/%d', verbose_name='Picture', default='uploads/no-image.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    status=models.CharField(max_length=100, choices=STATUS_CHOICES, default='draft',verbose_name='Status')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self) -> str:
        return self.title

class About(models.Model):
    picture = models.ImageField(upload_to='uploads/about',null=True,blank=True, verbose_name='About Image')
    content = RichTextUploadingField(verbose_name='About', null=True, blank=True)

    def __str__(self):
        return 'About'

class Contact(models.Model):
    company_name=models.CharField(max_length=255, verbose_name='Company Name', default='Arcotama')
    address=models.CharField(max_length=255, verbose_name='Address')
    email=models.CharField(max_length=100, verbose_name='Email', default='sales@arcotama.com')
    phone=models.CharField(max_length=20, verbose_name='Phone', null=True, blank=True)
    mobile_phone=models.CharField(max_length=20, verbose_name='Mobile Phone', default=1234567888)
    site_map_url = models.URLField(max_length=255, verbose_name='Site Map', blank=True, null=True)
    iframe = models.TextField(verbose_name='Iframe', blank=True, null=True)
    facebook_url=models.URLField(max_length=150, verbose_name='Facebook', blank=True, null=True)
    linkedin_url=models.URLField(max_length=150, verbose_name='Linkedin', blank=True, null=True)
    instagram_url=models.URLField(max_length=150, verbose_name='Instagram', blank=True, null=True)

    def __str__(self):
        return 'Contact'


STATUS_MESSAGE=(
    ('read','Read'),
    ('unread','Unread')
)

class Message(models.Model):
    name=models.CharField(max_length=100, verbose_name='Name')
    company=models.CharField(max_length=100, verbose_name='Company')
    email=models.CharField(max_length=100, verbose_name='Email')
    subject=models.CharField(max_length=100, verbose_name='Subject')
    message=models.TextField(verbose_name='Message')
    status_message=models.CharField(max_length=25, choices=STATUS_MESSAGE, default='unread', verbose_name='Status')
    

    def get_absolute_url(self):
        return '/contact'

    def __str__(self):
        return self.email +' | '+ self.subject
    