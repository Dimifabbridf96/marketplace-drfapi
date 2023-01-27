from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s comment"
    


