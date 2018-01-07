from django.conf.urls import url
from django.urls import path
from contact.views import ContactView, ContactDetail

urlpatterns = [
    path('api/v1/contact/', ContactView.as_view()),
    path('api/v1/contact/<int:id>', ContactDetail.as_view()),
]
