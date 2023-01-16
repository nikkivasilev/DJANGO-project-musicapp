from django.urls import path, include

from music_app.album.views import album_add, album_details, album_edit, album_delete

urlpatterns = (
    path('album/', include([
        path('add/', album_add, name='album add'),
        path('details/<int:pk>/', album_details, name='album details'),
        path('edit/<int:pk>/', album_edit, name='album edit'),
        path('delete/<int:pk>/', album_delete, name='album delete')]
    ),
         ),)
