from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model for the categories.
    In this website, the products are categorised by their product type
    """
    class Meta:
        verbose_name_plural = 'Categories'

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
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    # setting this to apply a numerated heat order,
    # so it is not by ID/alphabetical
    heat_order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for information on the individual products
    """
    category = models.ForeignKey('Category',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand',
                              null=True, blank=True,
                              on_delete=models.SET_NULL)
    heat_level = models.ForeignKey('HeatLevel',
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    average_rating = models.FloatField(default=0)
    ingredients = models.TextField(null=False, blank=False)
    staff_favourite = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """
    A model to handle allowing reviews on products
    https://www.youtube.com/watch?v=8iCqlFyFu2s
    """
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product_reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    reviewer = models.ForeignKey(User,
                                 related_name='product_reviews',
                                 on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
