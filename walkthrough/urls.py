from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='walkthrough-home'),
    path('about/', views.about, name='walkthrough-about'),
    path('home_purchase/', views.home_purchase, name='walkthrough-home_purchase'),
    path('marriage/', views.marriage, name='walkthrough-marriage'),
    path('graduation/', views.graduation, name='walkthrough-graduation'),
    path('general_one/', views.general_one, name='walkthrough-general_one'),
    path('helpful/', views.helpful, name='walkthrough-helpful'),
]
