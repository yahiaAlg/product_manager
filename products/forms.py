from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "description": forms.Textarea(attrs={"class": "form-input", "rows": 4}),
            "price": forms.NumberInput(attrs={"class": "form-input", "step": "0.01"}),
            "stock": forms.NumberInput(attrs={"class": "form-input"}),
        }
