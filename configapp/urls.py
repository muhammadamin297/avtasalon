from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('salon/add/', add_salon, name='add-salon'),
    path('brend/add/', add_brend, name='add-brend'),
    path('car/add/', add_car, name='add-car'),
    path('salon/<int:pk>/', salon_detail, name='salon_detail'),
    path('salon/<int:pk>/cars/', salon_cars, name='salon_cars'),
    path('car/<int:pk>/qr-pdf/', car_qr_pdf, name='car_qr_pdf'),

]

