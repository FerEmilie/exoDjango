from django.db import models

# Create your models here.

class Plat(models.Model):

    nom = models.CharField(max_length=100)

    prix = models.FloatField(max_length=42)

    # image = models.ImageField(upload_to='uploads/')

    categorie = models.ForeignKey('Categorie')


    def __str__(self):


        return self.nom


class Categorie(models.Model):

    nom = models.CharField(max_length=30)


    def __str__(self):

        return self.nom
