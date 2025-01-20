from django.views import View 
from django.shortcuts import render
from django.http import HttpResponse

class TudoListView(View):
    def home(request):  
        return HttpResponse('hy')
