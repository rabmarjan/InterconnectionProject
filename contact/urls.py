from django.conf.urls import url
from contact.views import ContactView, ContactDetail

urlpatterns = [
    url(r'^api/v1/contact/$', ContactView.as_view()),
    url(r'^api/v1/contact/(?P<contact_id>[0-9]+)/$', ContactDetail.as_view()),
]
