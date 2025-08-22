from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AutoSalon, Car
from .forms import AutoSalonForm, BrendForm, CarForm

# PDF va QR kod uchun
import qrcode
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

# ---------------------------------------
# Asosiy CRUD view’lar
# ---------------------------------------

def home(request):
    salons = AutoSalon.objects.all()
    return render(request, 'home.html', {'salons': salons})

def salon_detail(request, pk):
    salon = get_object_or_404(AutoSalon, pk=pk)
    return render(request, 'salon_detail.html', {'salon': salon})

def salon_cars(request, pk):
    salon = get_object_or_404(AutoSalon, pk=pk)
    cars = Car.objects.filter(salon=salon)
    return render(request, 'cars.html', {'salon': salon, 'cars': cars})

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

# ---------------------------------------
# PDF + QR kod view
# ---------------------------------------

def car_qr_pdf(request, pk):
    # 1️⃣ Mashinani olish
    car = get_object_or_404(Car, pk=pk)

    # 2️⃣ QR kod yaratish
    qr_data = request.build_absolute_uri(f"/car/{car.id}/")  # URL uchun
    qr_img = qrcode.make(qr_data)
    qr_io = BytesIO()
    qr_img.save(qr_io, format='PNG')  # formatni aniq belgilash
    qr_io.seek(0)

    # 3️⃣ PDF yaratish
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="car_{car.id}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # 4️⃣ Sarlavha
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 100, f"Mashina ma'lumotlari: {car.model_name}")

    # 5️⃣ Mashina ma’lumotlari
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 130, f"Brend: {car.brend.title}")
    p.drawString(100, height - 150, f"Narx: {car.price}")
    p.drawString(100, height - 170, f"Yil: {car.year}")
    p.drawString(100, height - 190, f"Rangi: {car.color}")

    # 6️⃣ Mashina rasmi (agar bo‘lsa)
    if car.img:
        car_img = ImageReader(car.img.path)
        p.drawImage(car_img, 350, height - 350, width=180, height=120, preserveAspectRatio=True, mask='auto')

    # 7️⃣ QR kodni joylashtirish
    qr_img_reader = ImageReader(qr_io)
    p.drawImage(qr_img_reader, 100, height - 400, width=200, height=200)

    # 8️⃣ PDFni yakunlash
    p.showPage()
    p.save()

    return response
