from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    OTHER = 'Other'
    FASHION = 'Fashion'
    BEAUTY = 'Beauty'
    HOME = 'Home & Garden'
    TOYS = 'Toys & Garden'
    SPORT = 'Sport & Outdoor'
    PET = 'Pet Supply'
    BOOKS = 'Books'
    ELECTRONICS = 'Electronics'
    CAR = 'Car & Motorbike'
    CATEGORIES = [
        (OTHER, 'Other'),
        (FASHION, 'Fashion'),
        (BEAUTY, 'Beauty'),
        (HOME, 'Home & Garden'),
        (TOYS, 'Toys & Garden'),
        (SPORT, 'Sport & Outdoor'),
        (PET, 'Pet Supply'),
        (BOOKS, 'Books'),
        (ELECTRONICS, 'Electronics'),
        (CAR, 'Car & Motorbike')
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='products/', default='../product')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300, blank=True)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=30, choices=CATEGORIES, default=OTHER)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s {self.title}"

