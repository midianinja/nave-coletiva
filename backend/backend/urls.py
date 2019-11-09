from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Nave Coletiva'

urlpatterns = [
    path('admin/', admin.site.urls),
]
