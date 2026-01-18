# Campus Zen Backend

Backend Django + Django REST Framework pour le projet Campus Zen

## Objectif

- Fournir une API REST pour les utilisateurs les questionnaires et les ressources
- Gérer l authentification via JWT
- Stocker les données dans SQLite en dev

## Pré requis

- Python installé
- Pip installé
- Optionnel Docker et Docker Compose

## Installation

### Mode Python

1 Cloner le projet
2 Installer les dépendances

```bash
pip install -r requirements.txt
```

3 Lancer les migrations

```bash
python manage.py migrate
```

4 Lancer le serveur

```bash
python manage.py runserver
```

## Lancer avec Docker

```bash
docker compose up --build
```

## Urls utiles

- Admin Django
	- http://127.0.0.1:8000/admin/

- API
	- base http://127.0.0.1:8000/api/

## Auth JWT

- Register
	- POST /api/register/
	- body json
		- emailPers
		- passwordPers

- Login
	- POST /api/token/
	- body json
		- emailPers
		- password
	- réponse
		- access
		- refresh

- Refresh
	- POST /api/token/refresh/
	- body json
		- refresh

## Exemple rapide avec curl

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
	-H "Content-Type: application/json" \
	-d "{\"emailPers\": \"test@example.com\", \"password\": \"mypassword\"}"
```

## Endpoints principaux

Les endpoints CRUD sont générés par les viewsets

- /api/personnes/
- /api/professionnels/
- /api/climats/
- /api/messages/
- /api/ressources/
- /api/avis/
- /api/questionnaires/
- /api/questions/
- /api/reponses/
- /api/seuils/
- /api/statuts/

## Soumission questionnaire

- POST /api/questionnaire/<id>/submit
- body json
	- idPers
	- reponses
		- idQuestion
		- idReponse

## Tests

```bash
python manage.py test
```

## Notes

- En dev l API est ouverte en AllowAny
- En prod il faudra activer IsAuthenticated sur les endpoints sensibles
