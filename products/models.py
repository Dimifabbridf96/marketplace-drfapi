from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Products(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='products/', default='../product')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s {self.title}"

