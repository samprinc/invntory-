# Step 4: Forms (inventory/forms.py)
from django import forms
from .models import Product, Sale

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity_sold']
#         widgets = {
#             'product': forms.Select(attrs={'class': 'form-control'}),