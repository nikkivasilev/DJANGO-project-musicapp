
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music_app.album.urls')),
    path('', include('music_app.profiles.urls')),
]
