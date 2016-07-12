from django.contrib import admin
from .models import Tag,Category,Blog,Comment,Info,MyUser

admin.site.register([Category,Tag,Blog,Comment,Info,MyUser])

# Register your models here.
