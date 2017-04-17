from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Genre
from django.shortcuts import render, redirect
from .forms import GenreForm


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


def add_skill(request, pk):
    skill_form = GenreForm()

    # TODO aqui hay que agregar una forma para capturar los datos de la nueva habilidad

    if request.method == 'POST':
        skill_form = GenreForm(request.POST)
        if skill_form.is_valid():
            result = Genre(name=request.POST.get('name'),
                           skill_type=request.POST.get('skill_type'),
                           description=request.POST.get('description'),
                           context=request.POST.get('context'),
                           ).insert_at(Genre.objects.get(id=pk), save=True)
            return redirect("genre_list")

    return render(request, 'genre/add_skill.html', {'form': skill_form})


def home(request):
    return render(request, 'home.html')


# how to define your own class-based view?
'''
from django.view.generic import UpdateView
class MyCustomUpdateView(UpdateView):
    model = Genre

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        """
        kwargs = super(MyCustomUpdateView, self).get_form_kwargs()
        kwargs.update({'my_first_param_to_init_form': 1,
                      'my_second_param_to_init_form': 2,
        })
        return kwargs
        
url(r'update/(?P<pk>\d+)', MyCustomUpdateView.as_view(), name="genre_update",),
        
'''
