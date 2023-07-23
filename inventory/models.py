from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=15)
    floor = models.IntegerField()
    building = models.CharField(max_length=50)
    
    def __str__(self):
        return self.number


class Owner(models.Model):
    
    class OwnerStatus(models.TextChoices):
        MAHASISWA = "MHS", _("Mahasiswa")
        PEGAWAI = "PEG", _("Pegawai")
    
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=OwnerStatus.choices, default=OwnerStatus.MAHASISWA)
    
    def __str__(self):
        return self.name


class Report(models.Model):
    
    class ReportCondition(models.TextChoices):
        BAIK = "BAIK", _("Baik")
        PERBAIKAN = "PERBAIKAN", _("Perbaikan")
        HILANG = "HILANG", _("Hilang")
    
    date = models.DateField()
    condition = models.CharField(max_length=10, choices=ReportCondition.choices, default=ReportCondition.BAIK)
    pic = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pic


class Specification(models.Model):
    name = models.CharField(max_length=50)
    is_computer = models.BooleanField()
    brand = models.CharField(max_length=50)
    ram = models.CharField(max_length=10)
    cpu = models.CharField(max_length=10)
    vga = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Item(models.Model):
    
    class ItemStatus(models.TextChoices):
        LEGACY = "LEG", _("Legacy")
        NEW = "NEW", _("New")
        
    name = models.CharField(max_length=50, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=ItemStatus.choices, default=ItemStatus.LEGACY)
    
    report = models.ManyToManyField(Report)
    specification = models.ManyToManyField(Specification)
    
    def __str__(self):
        return self.name
    
