import threading
from django.db import transaction
from django.test import TestCase
from .models import Book


# test case for signal behavior
class SignalTest(TestCase):
    
    def test_signal_execution(self):
        # print caller thread id
        print("Caller Thread:", threading.get_ident())
        
        # create book inside transaction
        with transaction.atomic():
            print("Caller in transaction:", transaction.get_connection().in_atomic_block)
            Book.objects.create(title="Accuknox Test")
        
        print("Caller finished")
