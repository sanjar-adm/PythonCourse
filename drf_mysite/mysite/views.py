from rest_framework import generics
from .serializers import ContactDetailSerializers
from .models import *


class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactDetailSerializers


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers