from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Model for the categories.
    In this website, the products are categorised by their heat level
    """

    CATEGORY_CHOICES = (
        ('mild', 'Mild'),
        ('medium', 'Medium'),
        ('hot', 'Hot'),
        ('extra_hot', 'Extra Hot'),
        ('inferno', 'Inferno'),
    )

    name = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name



class Product(models.Model):
    """
    Model for information on the individual products
    """
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name