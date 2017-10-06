from django import forms
from django.contrib.auth.models import User
from base_app.models import UserProfileInfo, ProductInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields =  ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('first_name', 'last_name','address')

class ProductInfoForm(forms.ModelForm):
    class Meta():
        model = ProductInfo
        fields = ('name','price','desc','images')


# class AdminsForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = Admins
#         fields = ('username','password')
