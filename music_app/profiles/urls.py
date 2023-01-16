from django.urls import path

from music_app.profiles.views import profile_details, profile_delete, index

urlpatterns = (
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('', index, name='index'),
)

