from django.contrib import admin

from .models import(Category, Tag, Post, About, Contact, Subscriber, Message)

class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('title',)}
    readonly_fields=('slug',)

class TagAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('title',)}
    readonly_fields=('slug',)

class PostAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('title',)}
    readonly_fields=('slug',)
    list_filter= ('tag','status')
    list_display=('title','publish','category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Subscriber)
admin.site.register(Message)
