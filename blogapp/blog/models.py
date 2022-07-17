from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE) #manytoone -> one author many post 
    #body = models.TextField()
    body = RichTextField()
    post_date = models.DateField(auto_now_add=True)
    snippet = models.TextField(max_length=255)

    
    class Meta():
        ordering = ["-post_date"]

    def __str__(self):
        return self.title + ' | ' + str(self.author) #for getting an object name in admin area

    def get_absolute_url(self):
        #return reverse('article-detail,args = [str(self.pk)]')
        return reverse('home')


