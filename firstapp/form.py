from django import forms
from .models import Category,User,Product,Feedback

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields='__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'