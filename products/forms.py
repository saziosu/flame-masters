from django import forms
from .models import Product, Category, Brand, HeatLevel


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # include all fields from the Product model
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set up categories as a choice in form
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        # Set up brands as a choice in form
        brands = Brand.objects.all()
        friendly_names = [(b.id, b.get_friendly_name()) for b in brands]
        self.fields['brand'].choices = friendly_names
        # Set up heat_level as a choice in form
        heat_levels = HeatLevel.objects.all()
        friendly_names = [(h.id, h.get_friendly_name()) for h in heat_levels]
        self.fields['heat_level'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'