from django.db import models


class ClinicInfo(models.Model):
    name = models.CharField(max_length=300, unique=True)
    telephonemobile = models.CharField(max_length=50, unique=True, blank=True, null=True)
    telephonemobile2 = models.CharField(max_length=50, unique=True, blank=True, null=True)
    telephone = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        max_length=150, unique=True, verbose_name='email address')
    address = models.TextField()
    vision = models.TextField()
    mission = models.TextField()
    about = models.TextField(null=True, blank=True)
    linkedIn = models.URLField(blank=True, null=True)
    faceBook = models.URLField(blank=True, null=True)
    youTube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    

