from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Model for the categories.
    In this website, the products are categorised by their product type
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """
    Model to categorise the brands for the products
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class HeatLevel(models.Model):
    """
    Model to categorise the heat level for the products
    Set to a choice field so there is a set amount of 5 heat levels
    """

    HEAT_CHOICES = (
        ('mild', 'Mild'),
        ('medium', 'Medium'),
        ('hot', 'Hot'),
        ('extra_hot', 'Extra Hot'),
        ('inferno', 'Inferno'),
    )

    name = models.CharField(max_length=10, choices=HEAT_CHOICES)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for information on the individual products
    """
    categories = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    heat_level = models.ForeignKey('HeatLevel', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name