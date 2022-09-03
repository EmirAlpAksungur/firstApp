from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    blog_sahibi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_sahibi')
    baslik = models.CharField(max_length=255)
    aciklama = models.TextField(blank=True, null=True)

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi =  models.DateTimeField(auto_now=True)
    yayın_tarihi = models.DateTimeField()

    def __str__(self):
        return f'{self.blog_sahibi.username}'
