from django.contrib import admin
from .models import Profile, Budget, DetailedBudget

admin.site.register(Profile)
admin.site.register(Budget)
admin.site.register(DetailedBudget)
