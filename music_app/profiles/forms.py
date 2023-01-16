from django import forms

from music_app.album.models import Album
from music_app.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    "placeholder": 'Age',
                },

            )
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Profile.objects.all().delete()
            Album.objects.all().delete()

        return self.instance