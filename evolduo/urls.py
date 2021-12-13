from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evolution/<int:evolution_id>/', views.detail, name='detail'),
    path('chromosome/<int:chromosome_id>/', views.chromosome_detail, name='chromosome_detail'),
]