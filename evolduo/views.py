from django.http.response import Http404
from django.shortcuts import render

from .models import Evolution, Chromosome

# Create your views here.

def index(request):
    evolutions = Evolution.objects.all()
    context = {
        'evolutions': evolutions,
    }
    return render(request, 'evolduo/index.html', context)

def detail(request, evolution_id):
    try:
        evolution = Evolution.objects.get(pk=evolution_id)
    except Evolution.DoesNotExist:
        raise Http404("Evolution does not exist")
    return render(request, 'evolduo/detail.html', {'evolution': evolution})

def chromosome_detail(request, chromosome_id):
    try:
        chromosome = Chromosome.objects.get(pk=chromosome_id)
    except Evolution.DoesNotExist:
        raise Http404("Chromosome does not exist")
    return render(request, 'evolduo/chromosome_detail.html', {'chromosome': chromosome})
