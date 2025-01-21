from django.views import View 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ..models.TaskModels import Task

class TudoListView(View):
    class TaskList(ListView):  
        model = Task
        context_object_name= "tasklist"
        template_name="base/tasklist.html"
        
    class DetailList(DetailView):
        model = Task
        context_object_name= "taskdetail"
        template_name="base/taskdetail.html"    
