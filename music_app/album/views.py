from django.shortcuts import render, redirect

from music_app.album.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from music_app.album.models import Album


def album_add(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'album/add-album.html', context=context)


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        "album": album,
    }
    return render(request, 'album/album-details.html', context=context)


def album_edit(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "album": album,
        "form": form,
    }

    return render(request, 'album/edit-album.html', context=context)


def album_delete(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "album": album,
        "form": form,
    }

    return render(request, 'album/delete-album.html', context=context)
