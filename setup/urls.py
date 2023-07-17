
from django.contrib import admin
from django.urls import path, include
from agenda.views import index, imagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agenda.urls')),
]
