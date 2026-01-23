
# Manuel Utilisateur

Projet Campus Zen

## C est quoi ce backend

Ce backend fournit une API REST pour l application Campus Zen
Vous pouvez vous inscrire vous connecter répondre à un questionnaire et récupérer des ressources

## Accès

- Base API
	- http://127.0.0.1:8000/api/

- Admin
	- http://127.0.0.1:8000/admin/

## Démarrage rapide

### Lancer le serveur

```bash
python manage.py runserver
```

Si tout est ok vous pouvez ouvrir la base api dans votre navigateur

## Authentification

### 1 Créer un compte

- Requête
	- POST /api/register/
- Body JSON
	- emailPers
	- passwordPers

Exemple

```json
{
	"emailPers": "test@example.com",
	"passwordPers": "securepassword123"
}
```

### 2 Se connecter

- Requête
	- POST /api/token/
- Body JSON
	- emailPers
	- password

Exemple

```json
{
	"emailPers": "test@example.com",
	"password": "securepassword123"
}
```

Réponse attendue

- access
- refresh
- idPers
- role

### 3 Utiliser le token

Pour appeler un endpoint protégé vous envoyez un header

- Authorization: Bearer <access>

## Utilisation des endpoints

### Récupérer des ressources

- GET /api/ressources/

Vous pouvez aussi récupérer une ressource précise

- GET /api/ressources/<id>/

### Voir les climats

- GET /api/climats/

### Voir les questionnaires

- GET /api/questionnaires/

### Voir les questions d un questionnaire

Option 1 filtre via query param

- GET /api/questions/?questionnaireId=<idQuestionnaire>

Option 2 via endpoints imbriqués si vous les utilisez

- GET /api/questionnaires/<id>/questions

### Voir les réponses d une question

Option filtre via query param

- GET /api/reponses/?question=<idQuestion>

## Envoyer un questionnaire

### But

Vous envoyez la liste des réponses choisies
Le backend calcule un score total avec les poids des questions
Puis il trouve le climat correspondant via les seuils
Et il enregistre un statut

### Requête

- POST /api/questionnaire/<idQuestionnaire>/submit

### Body JSON

- idPers
- reponses
	- idQuestion
	- idReponse

Exemple

```json
{
	"idPers": 1,
	"reponses": [
		{"idQuestion": 10, "idReponse": 41},
		{"idQuestion": 11, "idReponse": 45}
	]
}
```

Réponse

- score_total
- idClimat

## Outils recommandés

- Postman pour tester rapidement les routes
- Insomnia si vous préférez une interface plus simple

## Problèmes courants

### Erreur 401

- Votre token access est manquant ou expiré
- Refaites un login ou utilisez /api/token/refresh/

### Erreur 400 sur login

- Vérifiez que vous envoyez bien password et pas passwordPers
- Vérifiez que l emailPers existe

### Je ne vois rien dans la base

- Vérifiez que vous avez lancé les migrations

```bash
python manage.py migrate
```

## Notes de dev

- En dev plusieurs endpoints sont en AllowAny donc pas de blocage auth
- Pour une version plus réaliste il faudra remettre IsAuthenticated

