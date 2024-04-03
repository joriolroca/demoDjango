from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(requets):
    professor = {"nom": "Joe", "cognom": "Dhoe", "edat": 25}
    template = loader.get_template('index.html')
    dades = template.render({"nom_template": professor['nom'], "cognom_template": professor['cognom'], "edat_template": professor['edat']})
    return HttpResponse(dades)

def about(requets):
    return HttpResponse("<h1>About</h1>")