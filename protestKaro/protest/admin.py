from django.contrib import admin

from models import UserData, Profile, Post, Comment, Follow, Agree
# Register your models here.

admin.site.register(UserData)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Agree)
admin.site.register(Follow)
admin.site.register(Profile)