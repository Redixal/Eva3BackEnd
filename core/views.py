from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Videojuego
from .forms import VideojuegoForm

class VideojuegoListView(ListView):
    model = Videojuego
    template_name = 'core/videojuego_list.html'
    context_object_name = 'videojuegos'

    def get_queryset(self):
        return Videojuego.objects.select_related('genero').all()

class VideojuegoDetailView(DetailView):
    model = Videojuego
    template_name = 'core/videojuego_detail.html'
    context_object_name = 'videojuego'

class VideojuegoCreateView(CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'core/videojuego_form.html'
    success_url = reverse_lazy('videojuego_list')

class VideojuegoUpdateView(UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'core/videojuego_form.html'
    success_url = reverse_lazy('videojuego_list')

class VideojuegoDeleteView(DeleteView):
    model = Videojuego
    template_name = 'core/videojuego_confirm_delete.html'
    success_url = reverse_lazy('videojuego_list')