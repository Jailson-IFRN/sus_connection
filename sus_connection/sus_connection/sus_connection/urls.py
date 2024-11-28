from django.contrib import admin
from django.urls import path, include
from ubs.views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ubs.urls')),
    path('', include('usuarios.urls')),
    path('', include('vacinas.urls')),
    path('', include('cartoes_sus_vacinas.urls')),

]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
