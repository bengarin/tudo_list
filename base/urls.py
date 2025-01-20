from django.urls import path
from .views.tudolist_views import TudoListView

urlpatterns = [
    path('',TudoListView.TaskList.as_view(),name="home")
]
