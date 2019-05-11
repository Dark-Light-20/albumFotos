from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from fotos.models import Category, Photo

# Create your views here.
class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class PhotoListView(ListView):
    model = Photo

class PhotoDetailView(DetailView):
    model = Photo

class PhotoUpdate(UpdateView):
    model = Photo
    fields = '__all__'

class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'

class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')

def base(request):
    return render(request, 'base.html')