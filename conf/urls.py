from django.contrib import admin
from django.urls import path

from myapp import views


handler404 = views.custom_handler404
handler500 = views.custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='index'),
    path(
        'departure/<str:departure>/',
        views.departure_view,
        name='departure_views'
    ),
    path('tour/<int:id>', views.tour_view, name='tour'),

]
