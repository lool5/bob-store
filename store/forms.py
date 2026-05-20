from django import forms
from .models import Product, Order, ProductImage 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount']  # أزلنا 'image' من fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'مثال: 15 (لنسبة 15%)'}),
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'alt_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'وصف الصورة (اختياري)'}),
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