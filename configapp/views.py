from django.shortcuts import render, get_object_or_404, redirect
from .models import AutoSalon, Car
from .forms import AutoSalonForm, BrendForm, CarForm

def home(request):
    salons = AutoSalon.objects.all()
    return render(request, 'home.html', {'salons': salons})

def salon_detail(request, pk):
    salon = get_object_or_404(AutoSalon, pk=pk)
    return render(request, 'salon_detail.html', {'salon': salon})

def salon_cars(request, pk):
    salon = get_object_or_404(AutoSalon, pk=pk)
    cars = Car.objects.filter(salon=salon)
    return render(request, 'salon_cars.html', {'salon': salon, 'cars': cars})

def add_salon(request):
    if request.method == 'POST':
        form = AutoSalonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutoSalonForm()
    return render(request, 'form.html', {'form': form, 'title': "Salon qo‘shish"})

def add_brend(request):
    if request.method == 'POST':
        form = BrendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BrendForm()
    return render(request, 'form.html', {'form': form, 'title': "Brend qo‘shish"})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'form.html', {'form': form, 'title': "Mashina qo‘shish"})
