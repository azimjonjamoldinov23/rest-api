from django.db import models

# Create your models here.
class Yonalish(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Students(models.Model):
    kurslari = [('1','1-kurs'), ('2','2-kurs'), ('3','3-kurs'), ('4','4-kurs')]
    name = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    yosh = models.PositiveBigIntegerField()
    kurs = models.CharField(max_length=30, choices=kurslari)
    yonalish = models.ForeignKey(Yonalish , on_delete=models.CASCADE)

