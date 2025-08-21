from django.shortcuts import render, get_object_or_404, redirect
from .models import AutoSalon, Car
from .forms import AutoSalonForm, BrendForm, CarForm


def home(request):
    salons = AutoSalon.objects.all()
    return render(request, 'home.html', {'salons': salons})


def salon_detail(request, pk):
    salon = get_object_or_404(AutoSalon, pk=pk)
    return render(request, 'salaon_dteali.html', {'salon': salon})


def salon_cars(request, pk):
    salon = get_object_or_404(AutoSalon, pk=pk)
    cars = Car.objects.filter(salon=salon)
    return render(request, 'cars.html', {'salon': salon, 'cars': cars})


# 🔹 Yangi salon qo‘shish
def add_salon(request):
    if request.method == "POST":
        form = AutoSalonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutoSalonForm()
    return render(request, 'form_template.html', {'form': form, 'title': "Yangi Salon qo‘shish"})



def add_brend(request):
    if request.method == "POST":
        form = BrendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BrendForm()
    return render(request, 'form_template.html', {'form': form, 'title': "Yangi Brend qo‘shish"})



def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'form_template.html', {'form': form, 'title': "Yangi Mashina qo‘shish"})




import qrcode
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.shortcuts import get_object_or_404
from .models import Car

def car_qr_pdf(request, pk):
    car = get_object_or_404(Car, pk=pk)

    # 1️⃣ QR code yaratamiz
    qr_data = request.build_absolute_uri(car.img.url if car.img else "")
    qr = qrcode.make(f"{request.build_absolute_uri('/')}car/{car.id}/")
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    qr_io.seek(0)

    # 2️⃣ PDF yaratamiz
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="car_{car.id}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # Sarlavha
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 100, f"Mashina ma'lumotlari: {car.model_name}")

    # Mashina haqida ma’lumot
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 130, f"Brend: {car.brend.title}")
    p.drawString(100, height - 150, f"Narx: {car.price}")
    p.drawString(100, height - 170, f"Yil: {car.year}")
    p.drawString(100, height - 190, f"Rangi: {car.color}")

    # QR code ni joylashtirish
    p.drawInlineImage(qr_io, 100, height - 400, 200, 200)

    p.showPage()
    p.save()

    return response


