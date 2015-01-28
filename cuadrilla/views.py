# from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from cuadrilla.forms import BomberoForm
from cuadrilla.models import Bombero


class BomberoCreate(CreateView):
    model = Bombero
    form_class = BomberoForm


class BomberoDetail(DetailView):
    model = Bombero


class BomberoUpdate(UpdateView):
    model = Bombero
    form_class = BomberoForm


class BomberoDelete(DeleteView):
    model = Bombero
    form_class = BomberoForm


class BomberoList(ListView):
    model = Bombero
    paginate_by = 10
