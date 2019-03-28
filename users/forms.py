from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Budget


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class BudgetRegisterForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['Country', 'Income_Per_Year', 'Housing_Cost_Per_Month', 'Debt_Payments_Each_Month', 'Purchasing_A_Home', 'Getting_Married', 'Graduating_College']


class BudgetUpdateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['Country', 'Income_Per_Year', 'Housing_Cost_Per_Month', 'Debt_Payments_Each_Month', 'Purchasing_A_Home', 'Getting_Married', 'Graduating_College']
