"""
views for organising business logic
"""
from typing import Dict, Any
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from contact.models import Contact
from contact.serializers import ContactSerializer


class ContactView(APIView):
    """
    Get or post a contact instance.
    """
    def get(self, request: Any) -> Response:
        """
        :param request:
        :return:
        """
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request: Any) -> Response:
        """
        :param request:
        :return:
        """
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"serializer.data": 200, "status": status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):
    """
     Update or delete a contact instance.
    """
    def get_object(self, contact_id: Any) -> Any:
        """
        :param id:
        :return:
        """
        try:
            return Contact.objects.get(contact_id=contact_id)
        except Contact.DoesNotExist:
            raise Http404

    def put(self, request: Any, contact_id: Any) -> Response:
        """
        :param request:
        :param id:
        :return:
        """
        contact = self.get_object(contact_id)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Any, contact_id: Any) -> Response:
        """
        :param request:
        :param id:
        :return:
        """
        contact = self.get_object(contact_id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
