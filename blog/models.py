from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.
 
 class Post(models.Model):
     author=models.ForeignKey('auth.User')
     title=models.CharField(max_length=255)
     text=models.TxtField()
     create_date=models.DateTimeField(default=timezone.now())
     published_date=models.DateTimeFiled(blank=True,null=True)
     
     def publish(self):
         self.published_date=timezone.now()
         self.save()
         
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def __str__(self):
        return self.title
    
class Comment(model.Model):
    post=models.ForeignKey('blog.Post',related_name='comments')
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approved_comment=models.BooleanField(default=False)
    