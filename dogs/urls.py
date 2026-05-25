from django.urls import path
from . import views

urlpatterns = [
    path('', views.dogs_list, name='dogs_list'),
    path('<int:pk>/', views.dog_detail, name='dog_detail'),
    path('breed/<str:breed>/', views.dogs_by_breed, name='dogs_by_breed'),
    path('search/<str:query>/', views.dogs_search, name='dogs_search'),
    path('adoptable/', views.adoptable_dogs, name='adoptable'),
    path('puppies/', views.puppies, name='puppies'),
]