from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='products/', default='../product')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s {self.title}"

