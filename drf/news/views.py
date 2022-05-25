from rest_framework import generics
from .serializers import *
from .models import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsDetailSerializers


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializers
    permission_classes = (IsAuthenticated,)


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsDetailSerializers
    queryset = News.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class CargoSerializers(generics.CreateAPIView):
    serializer_class = CargoSerializers