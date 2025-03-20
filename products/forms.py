from django import forms
from .models import Product
class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="Nombre",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Nombre del producto'
        })
    )
    
    description = forms.CharField(
        max_length=300,
        label="Descripción",
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Descripción del producto',
            'rows': 4
        })
    )
    
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=3,
        label="Precio",
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Precio del producto'
        })
    )

    photo = forms.ImageField(
        required=False,
        label="Foto",
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full border px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400'
        })
    )
    
    # Guardar datos en la BD
    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            photo=self.cleaned_data['photo'],
        )
