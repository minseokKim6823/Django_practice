from django.db import models
# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=200,null=True, blank = True)
    url = models.URLField('url', unique=True)
    
    def __str__(self):
        return self.title
    
