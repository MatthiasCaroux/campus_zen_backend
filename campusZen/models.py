from django.db import models

# Create your models here.


class Personne(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
