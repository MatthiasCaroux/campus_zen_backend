
# routes principales du projet
# on expose l admin django et toutes les routes api de l app
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('campusZen.urls')),
]
