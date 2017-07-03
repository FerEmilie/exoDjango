from django.db import models
# Create your models here.
class Gestionrestaurant(models.Model):
    nom= models.CharField(max_length=255)
    adresse= models.CharField(max_length=255)
    # carte = models.ForeignKey('Menu')
    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.nom
