from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
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
router.register(r'questionnaires', QuestionnaireViewSet)
router.register(r'reponses', ResponseViewSet)
router.register(r'seuils', SeuilViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
