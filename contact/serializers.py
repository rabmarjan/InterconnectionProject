from contact.models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    """Serializes an Address object"""

    class Meta:
        model = Contact
        fields = ("contact_id", "first_name", "last_name", "middle_name", "email", "country", "phone", "address")
