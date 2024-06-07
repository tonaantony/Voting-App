from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote_post, name='start_voting'),
    path('vote/<int:post_id>/', views.vote_post, name='vote_post'),
    path('results/', views.results, name='results'),
    path('manage/', views.manage, name='manage'),
]
