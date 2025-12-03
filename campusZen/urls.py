from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

router = DefaultRouter()
router.register(r'personnes', PersonneViewSet)
router.register(r'professionnels', ProfessionnelViewSet)
router.register(r'climats', ClimatViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'ressources', RessourceViewSet)
router.register(r'avis', AvisViewSet)
router.register(r'questionnaires', QuestionnairesViewSet)
router.register(r'statuts', StatutViewSet)
router.register(r'consultesRessources', ConsulteRessourceViewSet)
router.register(r'recus', RecuViewSet)
router.register(r'consultesPro', ConsulteProViewSet)


router.register(r'questions', QuestionViewSet)
router.register(r'reponses', ReponseViewSet)
router.register(r'seuils', SeuilViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", MeView.as_view(), name="me"),
]
