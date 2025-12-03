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
router.register(r'seuils', SeuilViewSet)



urlpatterns = [
    path('questionnaire/<int:pk>/', QuestionnaireDetailView.as_view(), name='questionnaire-detail'),
    path('questionnaire/<int:pk>/questions/', QuestionsListView.as_view(), name='question-list'),
    path('questionnaire/<int:pk>/question/<int:question_pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('questionnaire/<int:pk>/question/<int:question_pk>/reponses/', ReponseListView.as_view(), name='reponse-list'),
    path('questionnaire/<int:pk>/question/<int:question_pk>/reponses/<int:reponse_pk>/', ReponseDetailView.as_view(), name='reponse-detail'),
    path('questionnaire/<int:pk>/submit',SubmitQuestionnaireView.as_view(),name='submit-questionnaire'),
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", MeView.as_view(), name="me"),
]
