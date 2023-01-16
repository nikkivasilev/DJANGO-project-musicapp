from django.shortcuts import render, redirect

from music_app.album.models import Album
from music_app.profiles.forms import CreateProfileForm, DeleteProfileForm
from music_app.profiles.models import Profile


def get_profile():
    try:
        return Profile.objects.get()

    except Profile.DoesNotExist as ex:
        return None


def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'albums_count': Album.objects.count()
    }
    return render(request, 'profiles/profile-details.html', context=context)


def profile_delete(request):
    if request.method == 'GET':
        form = DeleteProfileForm()
    else:
        form = DeleteProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'albums': Album.objects.all(),
    }
    return render(request, 'profiles/profile-delete.html', context=context)


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'albums': Album.objects.all(),
    }

    if profile is None:
        return add_profile(request)

    return render(request, 'base/home-with-profile.html', context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request,
                  'base/home-no-profile.html',
                  context=context,
                  )
