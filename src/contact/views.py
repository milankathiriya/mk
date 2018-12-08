from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics

# Create your views here.


class SnippetListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SnippetCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
