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
    main_image = sample_tours[keys[0]].get(
        'picture', 'https://place-hold.it/1600x300'
    )
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
    tours = {k: v for k, v in data.tours.items() if v['departure'] == departure}
    price_range = [tours[i]['price'] for i in tours]
    night_range = [tours[i]['nights'] for i in tours]
    min_price, max_price = min(price_range), max(price_range)
    min_nights, max_nights = min(night_range), max(night_range)
    current_departure = [departure, data.departures[departure]]
    context = {
        'title': data.title,
        'departures': data.departures,
        'count_tours': len(tours),
        'min_price': min_price,
        'max_price': max_price,
        'min_nights': min_nights,
        'max_nights': max_nights,
        'current_departure': current_departure,
        'tours': tours
    }
    template = 'myapp/departure_upd.html'
    return render(request, template, context)


def tour_view(request, id):
    departure = data.tours[id]['departure']
    context = {
        'departures': data.departures,
        'current_departure': [departure, data.departures[departure]],
        'tour_data': data.tours[id]
    }
    template = 'myapp/tour_upd.html'
    return render(request, template, context)
