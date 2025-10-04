from django import forms
from .models import Product
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id':'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier Price',
            
            }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'eg 1', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'eg Laptop', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'eg ABC123', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'eg 999.99', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'eg 10', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'eg Supplier Name', 'class': 'form-control'}),
            
            }
        
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        # check if passwords match
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data