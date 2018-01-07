from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('', include('contact.urls')),
]
