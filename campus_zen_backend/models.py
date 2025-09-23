from django.db import models

class Personne(models.Model):
    idPersonne = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    lastConnection = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idPersonne, self.email, self.role, self.lastConnection
    
class Professionnel(models.Model):
    idProfessionnel = models.AutoField(primary_key=True)
    nomPro = models.CharField(max_length=255)
    prenomPro = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fonctionPro = models.CharField(max_length=255)
    telephonePro = models.CharField(max_length=20)
    adressePro = models.CharField(max_length=255)

    def __str__(self):
        return self.idProfessionnel, self.nomPro, self.prenomPro, self.email, self.fonctionPro, self.telephonePro, self.adressePro
    
class Message(models.Model):
    idMessage = models.AutoField(primary_key=True)
    Message = models.CharField(max_length=10000)

    def __str__(self):
        return self.idMessage, self.Message
    
class Ressource(models.Model):
    idRessource = models.AutoField(primary_key=True)
    typeRessource = models.CharField(max_length=255)
    titreRessource = models.CharField(max_length=255)
    lienRessource = models.CharField(max_length=1000)
    descriptionRessource = models.CharField(max_length=500)

    def __str__(self):
        return self.idRessource, self.typeRessource, self.titreRessource, self.lienRessource, self.descriptionRessource
    
class Avis(models.Model):
    idAvis = models.AutoField(primary_key=True)
    nbEtoile = models.IntegerField()
    messageAvis = models.CharField(max_length=255)
    dateAvis = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idAvis, self.nbEtoile, self.messageAvis, self.dateAvis
    
class Question(models.Model):
    idQuestion = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.idQuestion, self.question
    
class Climat(models.Model):
    idClimat = models.AutoField(primary_key=True)
    nomClimat = models.CharField(max_length=255)

    def __str__(self):
        return self.idClimat, self.nomClimat
    
class Concerne(models.Model):
    idClimat = models.ForeignKey(Climat, on_delete=models.CASCADE)
    idMessage = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.idClimat, self.idMessage
    
class Statut(models.Model):
    idClimat = models.ForeignKey(Climat, on_delete=models.CASCADE)
    idPersonne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    dateStatut = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idClimat, self.idPersonne, self.dateStatut
    

class ConsulteRessource(models.Model):
    idRessource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    idPersonne = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return self.idRessource, self.idPersonne
    
class SoumetAvis(models.Model):
    idAvis = models.ForeignKey(Avis, on_delete=models.CASCADE)
    idPersonne = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return self.idAvis, self.idPersonne
    
class Recu(models.Model):
    idMessage = models.ForeignKey(Message, on_delete=models.CASCADE)
    idPersonne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    dateMessage = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idMessage, self.idPersonne
    
class ConsultePro(models.Model):
    idProfessionnel = models.ForeignKey(Professionnel, on_delete=models.CASCADE)
    idPersonne = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return self.idProfessionnel, self.idPersonne
    