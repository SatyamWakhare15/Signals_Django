import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def book_signal(sender, instance, **kwargs):
    print("Signal START")
    print("Signal Thread:", threading.get_ident())
    print("Signal in transaction:", transaction.get_connection().in_atomic_block)
    time.sleep(3)
    print("Signal END")