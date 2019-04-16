from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
import pycountry


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    CAN = "CANADA"
    MEX = "MEXICO"
    USA = "UNITED_STATES"

    COUNTRY_CHOICES = (
        (CAN, "Canada"),
        (MEX, "Mexico"),
        (USA, "United States of America"),
    )

    Country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default=USA)
    Income_Per_Year = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    Purchasing_A_Home = models.BooleanField(default=False)
    Getting_Married = models.BooleanField(default=False)
    Graduating_College = models.BooleanField(default=False)

    def income_per_month(self):
        return round(self.Income_Per_Year / 12, 2)

    def __str__(self):
        return f'{self.user.username} Budget'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class DetailedBudget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Giving = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Saving = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Food = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Utilities = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Housing = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Transportation = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Health = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Insurance = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Recreation = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Personal_Spending = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Miscellaneous = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def get_income(self):
        return self.user.budget.Income_Per_Year

    def food_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Food / Income_Per_Month
        return round(ratio * 100, 2)

    def food_diff(self):
        max = 15

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Food / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def utilities_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Utilities / Income_Per_Month
        return round(ratio * 100, 2)

    def utilities_diff(self):
        max = 10

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Utilities / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def housing_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Housing / Income_Per_Month
        return round(ratio * 100, 2)

    def housing_diff(self):
        max = 25

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Housing / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def transportation_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Transportation / Income_Per_Month
        return round(ratio * 100, 2)

    def transportation_diff(self):
        max = 10

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Transportation / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def health_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Health / Income_Per_Month
        return round(ratio * 100, 2)

    def health_diff(self):
        max = 10

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Health / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def insurance_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Insurance / Income_Per_Month
        return round(ratio * 100, 2)

    def insurance_diff(self):
        max = 15

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Insurance / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def recreation_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Recreation / Income_Per_Month
        return round(ratio * 100, 2)

    def recreation_diff(self):
        max = 10

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Recreation / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def personal_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Personal_Spending / Income_Per_Month
        return round(ratio * 100, 2)

    def personal_diff(self):
        max = 10

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Personal_Spending / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def misc_percent(self):
        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Miscellaneous / Income_Per_Month
        return round(ratio * 100, 2)

    def misc_diff(self):
        max = 10

        Income_Per_Month = self.user.budget.Income_Per_Year / 12
        ratio = self.Miscellaneous / Income_Per_Month
        percent = ratio * 100
        return round(percent - max, 2)

    def __str__(self):
        return f'{self.user.username} Detailed Budget'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
