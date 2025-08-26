from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('EL', 'Electronics'),
        ('FD', 'Food'),
        ('CL', 'Clothes'),
    ]

    name = models.CharField(max_length=100, verbose_name="Product Name")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='EL')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available_until = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} (${self.price})"

    class Meta:
        ordering = ['-price']  
