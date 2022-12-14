import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV) as f:
        reader = list(csv.DictReader(f))    

    page = request.GET.get('page', 1)
    paginator = Paginator(reader, 10)
    current_page = paginator.get_page(page)

    context = {
        'bus_stations': current_page.object_list,
        'page': current_page,
    }
    return render(request, 'stations/index.html', context)
