from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_city', 'user_school', 'user_email', 'user_message')
    ordering = ('user_name',)

admin.site.register(Mood)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)