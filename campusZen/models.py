from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Personne(models.Model):
    idPers = models.AutoField(primary_key=True)
    emailPers = models.EmailField(max_length=255, unique=True)
    passwordPers = models.CharField(max_length=255)  # sera hashé
    role = models.CharField(max_length=50, choices=(('étudiant', 'Étudiant'), ('admin', 'Admin')), default='étudiant')
    lastConnection = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.idPers} - {self.emailPers} - {self.role} - {self.lastConnection}"

    def set_password(self, password):
        self.passwordPers = make_password(password)

    def check_password(self, password):
        return check_password(password, self.passwordPers)

    @property
    def id(self):
        # alias pour que JWT trouve un "id"
        return self.idPers


class Professionnel(models.Model):
    idPro = models.AutoField(primary_key=True)
    nomPro = models.CharField(max_length=255)
    prenomPro = models.CharField(max_length=255)
    fonctionPro = models.CharField(max_length=255)
    emailPro = models.EmailField(unique=True)
    telephonePro = models.CharField(max_length=20)
    adressePro = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nomPro} - {self.prenomPro} - {self.emailPro} - {self.fonctionPro}"


class Climat(models.Model):
    idClimat = models.AutoField(primary_key=True)
    nomClimat = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nomClimat}"


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
        return f"{self.titreR} - {self.typeR}"


class Avis(models.Model):
    idAvis = models.AutoField(primary_key=True)
    nbEtoile = models.IntegerField()
    messageAvis = models.CharField(max_length=255)
    dateAvis = models.DateTimeField(auto_now=True)
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_avis", null=False, blank=False)

    def __str__(self):
        return f"{self.idAvis} - {self.nbEtoile} - {self.messageAvis} - {self.dateAvis} - {self.idPers}"


class Questionnaire(models.Model):
    idQuestionnaire = models.AutoField(primary_key=True)
    nomQuestionnaire = models.CharField(max_length=255)
    descriptionQuestionnaire = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.idQuestionnaire} - {self.nomQuestionnaire}"


class Question(models.Model):
    idQuestion = models.AutoField(primary_key=True)
    intituleQuestion = models.CharField(max_length=255)
    poids = models.FloatField()

    questionnaireId = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="questionnaires_questions", null=False, blank=False, default=1)

    def __str__(self):
        return f"{self.idQuestion} - {self.intituleQuestion}"


class Reponse(models.Model):
    idReponse = models.AutoField(primary_key=True)
    texte = models.CharField(max_length=255)
    score = models.IntegerField()

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="reponses")

    def __str__(self):
        return f"{self.idReponse} - {self.texte} ({self.score})"


class Seuil(models.Model):
    idSeuil = models.AutoField(primary_key=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="seuils")
    climat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="seuils")
    minScore = models.IntegerField()
    maxScore = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.minScore}-{self.maxScore} : {self.description}"



class Statut(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="statuts")
    climat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="statuts")
    scoreTotal = models.FloatField()
    dateStatut = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.personne} - {self.climat} - {self.scoreTotal} - {self.dateStatut}"

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

score_user = 0 
for question in questionnaire : 
    score_user += score_reponse * poids_question

score_user