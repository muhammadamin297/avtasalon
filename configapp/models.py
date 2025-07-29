from django.db import models

class AutoSalon(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    img = models.ImageField(upload_to='salon_images/')

    def __str__(self):
        return self.title


class Brend(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Car(models.Model):
    salon = models.ForeignKey(AutoSalon, on_delete=models.CASCADE)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    img = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"{self.model_name} - {self.salon.title}"
