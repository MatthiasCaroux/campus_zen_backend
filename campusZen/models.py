from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# ici on met tous les modeles de la base
# ca sert a definir les tables et les relations


class PersonneManager(BaseUserManager):
    # manager custom pour creer un user ou un admin
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
    # modele utilisateur custom base sur l email

    # role sert a separer etudiant et admin
    # lastConnection sert surtout a garder une date de derniere connexion

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
    # professionnel de sante ou contact propose dans l app
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
    # un climat correspond a un resultat ou un etat general
    idClimat = models.AutoField(primary_key=True)
    nomClimat = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nomClimat}"


class Message(models.Model):
    # message associe a un climat
    idMessage = models.AutoField(primary_key=True)
    message = models.CharField(max_length=10000)
    idClimat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="climats_messages", null=False, blank=False)

    def __str__(self):
        return f"{self.idMessage} - {self.message} - {self.idClimat}"


class Ressource(models.Model):
    # ressource conseillee genre article video etc
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
    # avis laisse par une personne
    idAvis = models.AutoField(primary_key=True)
    nbEtoile = models.IntegerField()
    messageAvis = models.CharField(max_length=255)
    dateAvis = models.DateTimeField(auto_now=True)
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_avis", null=False, blank=False)

    def __str__(self):
        return f"{self.idAvis} - {self.nbEtoile} - {self.messageAvis} - {self.dateAvis} - {self.idPers}"


class Questionnaire(models.Model):
    # questionnaire qui contient plusieurs questions
    idQuestionnaire = models.AutoField(primary_key=True)
    nomQuestionnaire = models.CharField(max_length=255)
    descriptionQuestionnaire = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.idQuestionnaire} - {self.nomQuestionnaire}"


class Question(models.Model):
    # question d un questionnaire
    # poids sert a donner plus d importance a certaines questions
    idQuestion = models.AutoField(primary_key=True)
    TYPE_CHOICES = (
        ('likert', 'Likert'),
        ('slider', 'Slider'),
        ('smiley', 'Smiley'),
    )

    typeQuestion = models.CharField(max_length=50, choices=TYPE_CHOICES, null=False, blank=False, default='likert')
    intituleQuestion = models.CharField(max_length=255, null=False, blank=False)
    poids = models.FloatField(default=1.0)

    # lien vers le questionnaire parent
    questionnaireId = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="questionnaires_questions", null=False, blank=False, default=1)

    def __str__(self):
        return f"{self.idQuestion} - {self.intituleQuestion} - {self.poids} - {self.questionnaireId} - {self.typeQuestion} " 


class Reponse(models.Model):
    # reponse possible a une question avec un score
    idReponse = models.AutoField(primary_key=True, default=None)
    texte = models.CharField(max_length=255)
    score = models.IntegerField()

    # foreign key obligatoire on garde une reponse liee a une question
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="reponses")

    def __str__(self):
        return f"{self.idReponse} - {self.texte} ({self.score})"


class Seuil(models.Model):
    # plage de score qui renvoie vers un climat
    idSeuil = models.AutoField(primary_key=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="seuils", default=None)
    climat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="seuils", default=None)
    minScore = models.IntegerField()
    maxScore = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.minScore}-{self.maxScore} : {self.description}"



class Statut(models.Model):
    # resultat final pour une personne a une date donnee
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="statuts", default=None)
    climat = models.ForeignKey(Climat, on_delete=models.CASCADE, related_name="statuts",default=None)
    scoreTotal = models.FloatField(default=0.0)
    dateStatut = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.personne} - {self.climat} - {self.scoreTotal} - {self.dateStatut}"

class ConsulteRessource(models.Model):
    # trace que la personne a consulte une ressource
    idR = models.ForeignKey(Ressource, on_delete=models.CASCADE, related_name="ressources_consultes", null=False, blank=False)
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_consultes", null=False, blank=False)

    def __str__(self):
        return f"{self.idR} - {self.idPers}"


class Recu(models.Model):
    # trace qu une personne a recu un message
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_recus", null=False, blank=False)
    idMessage = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="messages_recus", null=False, blank=False)
    dateMessage = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.idMessage} - {self.idPers} - {self.dateMessage}"


class ConsultePro(models.Model):
    # trace que la personne a consulte un professionnel
    idPro = models.ForeignKey(Professionnel, on_delete=models.CASCADE, related_name="professionnels_consultes", null=False, blank=False)
    idPers = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="personnes_consultesPro", null=False, blank=False)

    def __str__(self):
        return f"{self.idPro} - {self.idPers}"
