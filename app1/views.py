from django.shortcuts import render

# Create your views here.

from app1.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView

class school_list(ListView):
    model=School
    context_object_name='school'
    ordering=['sname']
    #queryset=School.objects.filter(id=1)
    #template_name='app1/school_list.html'


class School_details(DetailView):
    model=School
    context_object_name='schools'
    

class School_Create(CreateView):
    model=School
    fields='__all__'