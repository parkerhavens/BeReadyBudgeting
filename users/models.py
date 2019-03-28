from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import pycountry


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


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
    Income_Per_Year = models.CharField(max_length=15)
    Housing_Cost_Per_Month = models.CharField(max_length=15)
    Debt_Payments_Each_Month = models.CharField(max_length=15)

    Purchasing_A_Home = models.BooleanField(default=False)
    Getting_Married = models.BooleanField(default=False)
    Graduating_College = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Budget'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
