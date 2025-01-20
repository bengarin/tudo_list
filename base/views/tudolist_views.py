from django.views import View 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from ..models.TaskModels import Task

class TudoListView(View):
    class TaskList(ListView):  
        model = Task
        context_object_name= "tasklist"
