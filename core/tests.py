import threading
from django.db import transaction
from django.test import TestCase
from .models import Book

class SignalTest(TestCase):

    def test_signal_execution(self):
        print("Caller Thread:", threading.get_ident())

        with transaction.atomic():
            print("Caller in transaction:",
                  transaction.get_connection().in_atomic_block)
            Book.objects.create(title="Accuknox Test")

        print("Caller finished")
