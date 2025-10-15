from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=100, default="no title")
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
