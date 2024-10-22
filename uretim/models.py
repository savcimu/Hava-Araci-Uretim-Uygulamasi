from django.db import models
from django.contrib.auth.models import User


class Takim(models.Model):
    takim_tipi = models.CharField(max_length=50)

    def __str__(self):
        return self.takim_tipi


class Personel(models.Model):
    user = models.CharField(max_length=50)
    sifre = models.CharField(max_length=128)
    takim = models.ForeignKey(Takim, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
    
class Ucak(models.Model):
    ad = models.CharField(max_length=50)

    def __str__(self):
        return self.ad


class Parca(models.Model):
    PARCA_TIPLERI = [
        ('KANAT', 'Kanat'),
        ('GOVDE', 'Gövde'),
        ('KUYRUK', 'Kuyruk'),
        ('AVIYONIK', 'Aviyonik'),
    ]
    ucak = models.ForeignKey(Ucak, on_delete=models.CASCADE)
    parca_tipi = models.CharField(max_length=50, choices=PARCA_TIPLERI)
    kullanilan_ucak = models.ForeignKey(Ucak, null=True, blank=True, related_name='kullanilan_parcalar', on_delete=models.SET_NULL)
    ureten_personel = models.ForeignKey(Personel, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.ucak.ad} - {self.parca_tipi}"


class UretilenUcak(models.Model):
    ucak_tipi = models.ForeignKey(Ucak, on_delete=models.CASCADE)
    kullanilan_parcalar = models.ManyToManyField(Parca)
    tarih = models.DateTimeField(auto_now_add=True)
    ureten_personel = models.ForeignKey(Personel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.ucak_tipi.ad} - {self.tarih}"
