""" product form"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):
    """form for adding product to the store"""
    class Meta:
        """defines model and fields which will be used"""
        model = Product
        fields = '__all__'

    img = forms.ImageField(
        label='Image', required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # names = [(c.id, c.name()) for c in categories]

        # self.fields['category'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
