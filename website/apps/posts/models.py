from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User  


# Create your models here.

class Post(models.Model):
	post_title = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_text = models.TextField()
	post_image = models.ImageField(upload_to='posts/images/')
	likes = models.ManyToManyField(User, related_name='user_post')

	def totallikes(self):
		return self.likes.count()

