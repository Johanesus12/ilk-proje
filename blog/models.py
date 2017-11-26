from django.db import models
from django.utils import timezone
# Create your models here.
class ogrenciler(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    TC = models.BigIntegerField()

    # verileri oluşturduk.
    # admin panelinde verilerin gözükmesi için
    def __str__(self):
        return '%s %s' % (self.ad, self.soyad)


class ogrenciler2(models.Model):
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    def __unicode__(self):
        return self.adi


class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilma_tarihi = models.DateTimeField(blank=True, null=True)

    def yayinla(self):
        self.yaratilma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik