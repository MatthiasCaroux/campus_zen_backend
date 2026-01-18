from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class PersonneManager(BaseUserManager):
    def create_user(self, emailPers, passwordPers=None, **extra_fields):
        if not emailPers:
            raise ValueError("L'utilisateur doit avoir une adresse email")

        emailPers = self.normalize_email(emailPers)
        user = self.model(emailPers=emailPers, **extra_fields)
        user.set_password(passwordPers)
        user.save(using=self._db)
        return user

    def create_superuser(self, emailPers, passwordPers=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Le superutilisateur doit avoir is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Le superutilisateur doit avoir is_superuser=True.")

        return self.create_user(emailPers, passwordPers, **extra_fields)


class Personne(AbstractBaseUser, PermissionsMixin):
    """Modèle utilisateur personnalisé basé sur l'email."""

    idPers = models.AutoField(primary_key=True)
    emailPers = models.EmailField(max_length=255, unique=True)
    role = models.CharField(
        max_length=50,
        choices=(('étudiant', 'Étudiant'), ('admin', 'Admin')),
        default='étudiant'
    )
    lastConnection = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'emailPers'
    REQUIRED_FIELDS = []

    objects = PersonneManager()

    @property
    def id(self):
        return self.idPers

    def __str__(self):
        return f"{self.emailPers} ({self.role})"


class Professionnel(models.Model):
    idPro = models.AutoField(primary_key=True)
    nomPro = models.CharField(max_length=255)
    prenomPro = models.CharField(max_length=255)
    fonctionPro = models.CharField(max_length=255)
    emailPro = models.EmailField(unique=True)
    telephonePro = models.CharField(max_length=20)
    adressePro = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()

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
    choices_typeR = [
        ('article', 'Article'),
        ('video', 'Vidéo'),
        ('podcast', 'Podcast'),
        ('livre', 'Livre'),
        ('site_web', 'Site Web'),
        ('documentaire', 'Documentaire'),
        ('film', 'Film'),
        ('formation', 'Formation'),
        ('autre', 'Autre'),
    ]
    idR = models.AutoField(primary_key=True)
    typeR = models.CharField(max_length=255, choices=choices_typeR)
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
    intituleQuestion = models.CharField(max_length=255, null=False, blank=False)
    poids = models.FloatField(default=1.0)

    questionnaireId = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="questionnaires_questions", null=False, blank=False, default=1)

    def __str__(self):
        return f"{self.idQuestion} - {self.intituleQuestion} - {self.poids} - {self.questionnaireId}"


class Reponse(models.Model):
    idReponse = models.AutoField(primary_key=True, default=None)
    texte = models.CharField(max_length=255)
    score = models.IntegerField()

    # ForeignKey obligatoire : supprimer default=None qui provoquait des tentatives d'insertion NULL
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="reponses")

    def __str__(self):
        return f"{self.idReponse} - {self.texte} ({self.score})"


class Seuil(models.Model):
    idSeuil = models.AutoField(primary_key=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="seuils", default=None)
    climat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="seuils", default=None)
    minScore = models.IntegerField()
    maxScore = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.minScore}-{self.maxScore} : {self.description}"


class Statut(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="statuts", default=None)
    climat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="statuts", default=None)
    scoreTotal = models.FloatField(default=0.0)
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
