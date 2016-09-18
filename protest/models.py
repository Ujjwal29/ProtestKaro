from __future__ import unicode_literals
from django import forms
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class UserData(models.Model):
    #auto increment user id which must match with profile id
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    aadhar_no = models.IntegerField()

    def __str__(self):
        return str(self.email) +" - "+ str(self.username)

class Profile(models.Model):
    #auto increment profile id
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    location = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    about_yourself = models.TextField()

    #number of protest a profile has created
    post_count = models.IntegerField()
    #email id fetched from USerData

    registered_on = models.DateField(auto_now_add=True)
    contact_no = models.IntegerField()

    def get_absolute_url(self):
        return reverse('protest:detail_profile', kwargs={'pk': self.pk})

    def __str__(self):
        s = self.first_name+" "+self.last_name
        return s

class Post(models.Model):
    #id auto increment
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()

    support_count = models.IntegerField(default=0)
    against_count = models.IntegerField(default=0)
    neutral_count = models.IntegerField(default=0)

    organizing_committee = models.CharField(max_length=100)
    age_group = models.CharField(max_length=25)
    dateTime = models.DateTimeField(auto_now_add=True)
    incident = models.TextField()
    closed = models.BooleanField(default=1)

    picture = models.CharField(max_length=1000)
    tag = models.CharField(max_length=100)
    concerned_authority = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('protest:detail_post', kwargs={'pk': self.pk})


    def __str__(self):
        s = self.subject+" - " +str(self.support_count)+" - "+str(self.against_count)+" - "+self.organizing_committee+" - "+self.incident+" - "+self.tag+" - "+self.concerned_authority
        return s

class Comment(models.Model):
    #auto increment comment id
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_text = models.TextField()
    agree_count = models.IntegerField()

    #type defines if the comment is in support(0) or against(1)
    type = models.BooleanField()

    def __str__(self):
        s = str(self.comment_text) +" - "+ str(self.post_id)+" - "+str(self.type)+" - "+str(self.agree_count)
        return s

class Follow(models.Model):

    #the person who is following
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #post or profile id
    follow_id = models.IntegerField()

    #defines the type of the follow_id
    type = models.BooleanField()

    def __str__(self):
        s = self.profile_id+" - "+self.type+" - "+self.follow_id
        return s


class Agree(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        s = self.profile_id+" - "+self.comment_id

