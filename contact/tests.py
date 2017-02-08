# Create your tests here.


from django.test import TestCase
from django.core import serializers
from contact.models import Contact


class ContactSerializerTest (TestCase):
    def test_serializer(self):
        # Stuff to serialize
        Contact(first_name='soma').save()
        Contact(first_name='Rahman').save()
        Contact(first_name='Ivey').save()

        # Expected output
        expect_yaml = \
            'contact.Contact:\n' \
            '  1: {first_name: soma, last_name: Arif}\n' \
            '  2: {first_name: Rahman, last_name: Mini}\n' \
            '  3: {first_name: Ivey, last_name: Jakir}\n'

        # Do the serialization
        actual_yaml = serializers.serialize('yaml', Contact.objects.all())

        # Did it work?
        self.assertEqual(actual_yaml, expect_yaml)
