from django.db import models


CATEGORIES = [
    ('Other', 'Other'),
    ('Fashion', 'Fashion'),
    ('Beauty', 'Beauty'),
    ('Home & Garden', 'Home & Garden'),
    ('Toys & Game', 'Toys & Garden'),
    ('Sport & Outdoor', 'Sport & Outdoor'),
    ('Pet Supply', 'Pet Supply'),
    ('Books', 'Books'),
    ('Electronics', 'Electronics'),
    ('Car & Motorbike', 'Car & Motorbike')
    
]


class Category(models.Model):
    name = models.CharField(max_length=50, choices=CATEGORIES, default='Other')
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True, default="")
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE,blank=True, null=True, related_name= 'product')

    def __str__(self):
        return self.name