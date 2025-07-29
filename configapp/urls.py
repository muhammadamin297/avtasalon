from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salon/<int:pk>/', views.salon_detail, name='salon_detail'),
    path('salon/<int:pk>/cars/', views.salon_cars, name='salon_cars'),
    path('add-salon/', views.add_salon, name='add_salon'),
    path('add-brend/', views.add_brend, name='add_brend'),
    path('add-car/', views.add_car, name='add_car'),
]
