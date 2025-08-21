from django.contrib import admin

from django.contrib import admin
from .models import AutoSalon, Brend, Car


@admin.register(AutoSalon)
class AutoSalonAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "phone", "address")
    search_fields = ("title", "email", "phone", "address")
    list_filter = ("title",)


@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model_name", "brend", "salon", "price", "year", "color")
    search_fields = ("model_name", "brend__title", "salon__title")
    list_filter = ("year", "brend", "salon", "color")
