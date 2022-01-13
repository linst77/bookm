from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BookM
# Create your views here.


class BookMListView( ListView):
    model = BookM
    template_name_suffix = "_list"

class BookMCreateView( CreateView):
    model = BookM
    template_name_suffix = "_create"
    # success_url = reverse_lazy('list')
    fields = ['site_name', 'site_url']

class BookmDetailView( DetailView):
    model = BookM

class BookmUpdateView( UpdateView):
    model = BookM
    template_name_suffix = "_update"
    fields = ['site_name', 'site_url']

class BookmDeleteView( DeleteView):
    model = BookM
    success_url = reverse_lazy('list')


