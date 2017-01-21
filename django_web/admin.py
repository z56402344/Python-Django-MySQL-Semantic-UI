#coding = utf-8
from django.contrib import admin
from django_web.models import Test
from django_web.models import SuperHero
from django_web.models import Blog
# from django_web.models import Blogs

# Register your models here.
admin.site.register(Test)


class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'added_on')
    search_fields = ["name"]
    ordering = ["name"]

admin.site.register(SuperHero, SuperHeroAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date')
    search_fields = ['title', 'author', 'content']
    list_filter = ('author', 'tags')
    ordering = ('-create_date', '-update_time')
    fields = ('title', 'author', 'tags', 'summary', 'content')

admin.site.register(Blog, BlogAdmin)
#
# class BlogsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'create_date')
#     search_fields = ['title', 'author', 'content']
#     list_filter = ('author', 'tags')
#     ordering = ('-create_date', '-update_time')
#     fields = ('title', 'author', 'tags', 'summary', 'content')
#
# admin.site.register(Blogs, BlogsAdmin)
