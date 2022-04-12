import random
from conf.settings import TOUR_NUMBER
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from . import data


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена, упс!</h1>')


def custom_handler500(request):
    return HttpResponseServerError('<h1>Произошла ошибка на сервере, упс!</h1>')


def main_view(request):
    template = 'myapp/index_upd.html'
    keys = random.sample(data.tours.keys(), TOUR_NUMBER)
    sample_tours = {key: data.tours[key] for key in keys}
    main_image = sample_tours[keys[0]].get('picture', 'https://place-hold.it/1600x300')
    context = {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
        'tours': sample_tours,
        'main_image': main_image
    }
    return render(request, template, context)


def departure_view(request, departure):
    template = 'myapp/departure.html'
    return render(request, template)


def tour_view(request, id):
    template = 'myapp/tour.html'
    return render(request, template)
