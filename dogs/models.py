from django.db import models

class Dog(models.Model):
    SIZE_CHOICES = [
        ('small', 'Pequeño'),
        ('medium', 'Mediano'),
        ('large', 'Grande'),
    ]
    GENDER_CHOICES = [
        ('male', 'Macho'),
        ('female', 'Hembra'),
    ]
    ENERGY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
    ]
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    color = models.CharField(max_length=50, blank=True)
    vaccinated = models.BooleanField(default=False)
    adopted = models.BooleanField(default=False)
    energy = models.CharField(max_length=10, choices=ENERGY_CHOICES, default='medium')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.name