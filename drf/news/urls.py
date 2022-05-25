from django.urls import path
from .views import *

urlpatterns = [
    path('create/', NewsCreateView.as_view()),
    path('list/', NewsListView.as_view()),
    path('detail/<int:pk>/', NewsDetailView.as_view()),
    path('create-cargo/', CargoSerializers.as_view()),
]

