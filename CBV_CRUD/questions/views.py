from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Question
# Create your views here.
class index(ListView):
    template_name='questions/index.html'
    model = Question
    
class create(CreateView):
    model = Question
    fields = ('title','answerA','answerB')

    
class read(DetailView):
    template_name='questions/read.html'
    model = Question
    
class update(UpdateView):
    model = Question
    fields = ('title','answerA','answerB')
    
class delete(DeleteView):
    model = Question
    success_url = reverse_lazy('questions:index')