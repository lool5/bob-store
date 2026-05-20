from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'discount',   # <-- أضف هذا الحقل
            'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'مثال: 15 (لنسبة 15%)'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control form-control-lg'
            }),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer_phone',
            'customer_address',
            'size'
            # تم إزالة 'discount' نهائياً
        ]
        widgets = {
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Phone Number'
            }),
            'customer_address': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'rows': 3,
                'placeholder': 'Your Address'
            }),
            'size': forms.Select(attrs={
                'class': 'form-select mb-3'
            }),
        }