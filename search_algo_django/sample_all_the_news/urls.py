from django.urls import path
from . import views

urlpatterns = [
    path('all_the_news_dataset/', views.all_the_news_dataset, name='all_the_news_dataset'),
    path('all_the_news_detail/<slug:pk>', views.all_the_news_detail, name='all_the_news_detail'),
]