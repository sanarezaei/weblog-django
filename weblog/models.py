from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name


class Weblog(models.Model): 
    title = models.CharField(max_length=200) 
    description = models.TextField()
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers/', blank=True)
    tags = models.ManyToManyField(Tag, related_name="weblogs_tag", blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('weblog_detail', args=[self.id])
