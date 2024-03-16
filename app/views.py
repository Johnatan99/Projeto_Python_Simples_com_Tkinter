from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.http import HttpResponse
from app.forms import CarrosForm
from app.models import Carros

# Create your views here.


def home(request):
    data = {}
    data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        salvar = form.save(commit=False)
        salvar.save()

        return HttpResponse("Dados inseridos")
    
    return render_to_response("index.html", locals(), context_instance = RequestContext(request))