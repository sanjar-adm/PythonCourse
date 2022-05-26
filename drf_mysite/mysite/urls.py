from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ContactCreateView.as_view()),
    path('list/', ContactListView.as_view()),
    path('detail/<int:pk>', ContactDetailView.as_view()),
]
