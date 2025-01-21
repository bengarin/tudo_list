from django.urls import path
from .views.tudolist_views import TudoListView

urlpatterns = [
    path('',TudoListView.TaskList.as_view(),name="home"),
    path('task/<int:pk>/',TudoListView.DetailList.as_view(),name="task"),
]
