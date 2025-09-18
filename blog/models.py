from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publication_date = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title