from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    taste = models.CharField(max_length=50)
    time = models.IntegerField(help_text='調理時間（分）')
    effort = models.CharField(max_length=20)
    memo = models.TextField(blank=True)
    photo = models.ImageField(upload_to='menu_photos/', blank=True, null=True)
    recommended_score = models.FloatField(default=0.0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
