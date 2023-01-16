from music_app.profiles.models import Profile


class Validate_profile_exists():
    def __bool__(self):
        return Profile.objects.all().count() == 1

    def __call__(self, *args, **kwargs):
        return Profile.objects.all().count() == 1
