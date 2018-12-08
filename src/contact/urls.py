from django.urls import path
from . import views

urlpatterns = [
    path('', views.SnippetListView.as_view()),
    path('create/', views.SnippetCreateView.as_view()),
]
