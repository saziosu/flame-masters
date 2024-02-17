from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Product, Category, Brand, HeatLevel, ProductReview


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


class ProductReviewForm(forms.ModelForm):
    """
    A form for users to input their product reviews
    """
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(
        label = "Rating",
        choices = RATING_CHOICES,
    )

    class Meta:
        model = ProductReview
        fields = [
            'rating',
            'comment',
        ]
    
    def __init__(self, *args, **kwargs):
        """
        https://django-crispy-forms.readthedocs.io/en/latest/layouts.html
        """
        super(ProductReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('rating'),
            Field('comment'),
            Submit('submit', 'Add my Review!', css_class='btn btn-black rounded-0 text-uppercase mt-5'),
        )
