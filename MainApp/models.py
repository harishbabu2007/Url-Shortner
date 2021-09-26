from django.db import models

# Create your models here.
class Urls(models.Model):
  site_url = models.URLField()
  slug_shortcut = models.CharField(max_length=100)
  slug_url = models.SlugField(unique=True)

  def __str__(self):
    return self.site_url