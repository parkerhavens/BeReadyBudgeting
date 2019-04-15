from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Budget, DetailedBudget


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
        fields = ['Country', 'Income_Per_Year', 'Purchasing_A_Home', 'Getting_Married', 'Graduating_College']


class BudgetUpdateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['Country', 'Income_Per_Year', 'Purchasing_A_Home', 'Getting_Married', 'Graduating_College']


class DetailedBudgetRegisterForm(forms.ModelForm):
    class Meta:
        model = DetailedBudget
        fields = ['Giving', 'Saving', 'Food', 'Utilities', 'Housing', 'Transportation', 'Health', 'Insurance', 'Recreation', 'Personal_Spending', 'Miscellaneous']


class DetailedBudgetUpdateForm(forms.ModelForm):
    class Meta:
        model = DetailedBudget
        fields = ['Giving', 'Saving', 'Food', 'Utilities', 'Housing', 'Transportation', 'Health', 'Insurance', 'Recreation', 'Personal_Spending', 'Miscellaneous']
