from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
        title = models.CharField(max_length=30, null=True)
        text = models.TextField(null=True)
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(null=True, blank=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title
