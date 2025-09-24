from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'personnes', PersonneViewSet)
router.register(r'professionnels', ProfessionnelViewSet)
router.register(r'climats', ClimatViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'ressources', RessourceViewSet)
router.register(r'avis', AvisViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'statuts', StatutViewSet)
router.register(r'consultesRessources', ConsulteRessourceViewSet)
router.register(r'recus', RecuViewSet)
router.register(r'consultesPro', ConsulteProViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
