
from django.urls import path
from body.views import home

urlpatterns = [
    path('', home)
]
