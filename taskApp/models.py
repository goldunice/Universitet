from django.db import models

JINS = [('Erkak', 'Erkak'), ('Ayol', 'Ayol')]


class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Fan(models.Model):
    nom = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField()

    def __str__(self):
        return self.nom


class Ustoz(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(choices=JINS, max_length=6)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=255)



    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism
