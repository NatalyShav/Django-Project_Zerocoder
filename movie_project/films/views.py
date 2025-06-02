from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm


def add_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_film')  # замените на нужный URL или имя маршрута
        else:
            error = 'Пожалуйста, исправьте ошибки в форме.'

    form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form, 'error': error})


def list_films(request):
    films = Film.objects.all()
    return render(request, 'films/list_films.html', {'films': films})





