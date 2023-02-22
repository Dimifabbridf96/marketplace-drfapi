from django.db import models


class Category(models.Model):
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

    name = models.CharField(max_length=50, choices=CATEGORIES, default=OTHER)
    content = models.TextField(blank=False, default="")

    def __str__(self):
        return self.name