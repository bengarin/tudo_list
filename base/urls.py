from django.urls import path
from .views.tudolist_views import TudoListView

urlpatterns = [
    path('',TudoListView.home,name="home")
]
