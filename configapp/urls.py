# from django.urls import path
# from .views import *
#
# urlpatterns = [
#     path('', home, name='home'),
#     path('salon/add/', add_salon, name='add-salon'),
#     path('brend/add/', add_brend, name='add-brend'),
#     path('car/add/', add_car, name='add-car'),
#     path('salon/<int:pk>/', salon_detail, name='salon_detail'),
#     path('salon/<int:pk>/cars/', salon_cars, name='salon_cars'),
#     path('car/<int:pk>/qr-pdf/', car_qr_pdf, name='car_qr_pdf'),
#
# ]
#
from django.urls import path
from .views import (
    home,
    add_salon,
    add_brend,
    add_car,
    salon_detail,
    salon_cars,
    car_qr_pdf
)

urlpatterns = [
    # 🏠 Bosh sahifa
    path('', home, name='home'),

    # ➕ Yangi qo‘shish
    path('salon/add/', add_salon, name='add_salon'),
    path('brend/add/', add_brend, name='add_brend'),
    path('car/add/', add_car, name='add_car'),

    # 🔎 Salon va mashinalar
    path('salon/<int:pk>/', salon_detail, name='salon_detail'),
    path('salon/<int:pk>/cars/', salon_cars, name='salon_cars'),

    # 📄 Mashina haqida PDF + QR code yuklab olish
    path('car/<int:pk>/qr-pdf/', car_qr_pdf, name='car_qr_pdf'),
]
