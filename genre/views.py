from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Genre
from django.shortcuts import render



class SkillCreate(CreateView):
    model = Genre
    fields = ['name']


class SkillDetail(DetailView):
    model = Genre
    fields = ['name']


class SkillUpdate(UpdateView):
    model = Genre
    fields = ['name']


class SkillDelete(DeleteView):
    model = Genre
    fields = ['name']


class SkillList(ListView):
    model = Genre
    fields = ['name']


def home(request):
    return render(request, 'home.html')

