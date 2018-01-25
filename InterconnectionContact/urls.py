from django.conf.urls import url
from django.urls import include, path
urlpatterns = [
    path('', include('contact.urls')),
]
