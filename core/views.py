from django.contrib.auth.mixins import LoginRequiredMixin
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

class VideojuegoCreateView(LoginRequiredMixin, CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'core/videojuego_form.html'
    success_url = reverse_lazy('videojuego_list')

class VideojuegoUpdateView(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'core/videojuego_form.html'
    success_url = reverse_lazy('videojuego_list')

class VideojuegoDeleteView(LoginRequiredMixin, DeleteView):
    model = Videojuego
    template_name = 'core/videojuego_confirm_delete.html'
    success_url = reverse_lazy('videojuego_list')