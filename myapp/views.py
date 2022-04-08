from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def custom_handler500(*args, **kwargs):
    return HttpResponseServerError('Произошла ошибка на сервере')


def main_view(request):
    template = 'myapp/departure.html'
    return render(request, template)


def departure_view(request, departure):
    template = 'myapp/departure.html'
    return render(request, template)


def tour_view(request, id):
    template = 'myapp/tour.html'
    return render(request, template)
