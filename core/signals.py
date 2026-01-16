import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book


# signal handler for Book model
@receiver(post_save, sender=Book)
def book_signal(sender, instance, **kwargs):
    print("Signal START")
    
    # checking which thread is running
    print("Signal Thread:", threading.get_ident())
    
    # check if signal runs in same transaction
    print("Signal in transaction:", transaction.get_connection().in_atomic_block)
    
    # adding delay to test synchronous behavior
    time.sleep(3)
    
    print("Signal END")