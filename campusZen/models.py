from django.db import models

class Personne(models.Model):
    idPers = models.AutoField(primary_key=True)
    emailPers = models.CharField(max_length=255)
    passwordPers = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    lastConnection = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.idPers} - {self.emailPers} - {self.role} - {self.lastConnection}"
    
class Professionnel(models.Model):
    idPro = models.AutoField(primary_key=True)
    nomPro = models.CharField(max_length=255)
    prenomPro = models.CharField(max_length=255)
    fonctionPro = models.CharField(max_length=255)
    emailPro = models.CharField(max_length=255)
    telephonePro = models.CharField(max_length=20)
    adressePro = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.idPro} - {self.nomPro} - {self.prenomPro} - {self.emailPro} - {self.fonctionPro} - {self.telephonePro} - {self.adressePro}"

class Climat(models.Model):
    idClimat = models.AutoField(primary_key=True)
    nomClimat = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.idClimat} - {self.nomClimat}"

class Message(models.Model):
    idMessage = models.AutoField(primary_key=True)
    message = models.CharField(max_length=10000)
    idClimat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="climats_messages", null=False, blank=False)

    def __str__(self):
        return f"{self.idMessage} - {self.message} - {self.idClimat}"
    
class Ressource(models.Model):
    idR = models.AutoField(primary_key=True)
    typeR = models.CharField(max_length=255)
    titreR = models.CharField(max_length=255)
    descriptionR = models.CharField(max_length=500)
    lienR = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.idR} - {self.typeR} - {self.titreR} - {self.descriptionR} - {self.lienR}"
    
class Avis(models.Model):
    idAvis = models.AutoField(primary_key=True)
    nbEtoile = models.IntegerField()
    messageAvis = models.CharField(max_length=255)
    dateAvis = models.DateTimeField(auto_now=True)
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_avis", null=False, blank=False)

    def __str__(self):
        return f"{self.idAvis} - {self.nbEtoile} - {self.messageAvis} - {self.dateAvis} - {self.idPers}"
    
class Question(models.Model):
    idQuestion = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.idQuestion} - {self.question}"
    
class Statut(models.Model):
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_statuts", null=False, blank=False)
    idClimat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="climats_statuts", null=False, blank=False)
    dateStatut = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.idClimat} - {self.idPers} - {self.dateStatut}"

class ConsulteRessource(models.Model):
    idR = models.ForeignKey(Ressource, on_delete=models.CASCADE, related_name="ressources_consultes", null=False, blank=False)
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_consultes", null=False, blank=False)

    def __str__(self):
        return f"{self.idR} - {self.idPers}"
    
class Recu(models.Model):
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_recus", null=False, blank=False)
    idMessage = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="messages_recus", null=False, blank=False)
    dateMessage = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.idMessage} - {self.idPers} - {self.dateMessage}"
    
class ConsultePro(models.Model):
    idPro = models.ForeignKey(Professionnel, on_delete=models.CASCADE, related_name="professionnels_consultes", null=False, blank=False)
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_consultesPro", null=False, blank=False)

    def __str__(self):
        return f"{self.idPro} - {self.idPers}"