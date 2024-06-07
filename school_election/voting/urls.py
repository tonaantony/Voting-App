from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<int:post_id>/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
    path('manage/', views.manage, name='manage'),
]
