from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading
import logging


#QUESTION 1 ANSWER: Synchronous behavior
'''The default behavior of Django signals is that they are executed synchronously. 
This means that when a signal is sent, the corresponding signal receiver function 
is executed immediately, and the code execution will pause until the receiver 
has completed its execution before proceeding to the next line of code.'''


# Set up logging
logging.basicConfig(level=logging.INFO)

# Synchronous behavior demonstration
@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if created:
        logging.info("QUESTION 1: Synchronous Behavior")
        logging.info(f"Signal executed in thread: {threading.current_thread().name}")
        logging.info(f"User {instance.username} has been created.")
        
        # Simulate a time-consuming task
        time.sleep(5)
        
        logging.info("Signal processing finished after 5 seconds delay.")


#QUESTION 2 ANSWER: Same thread behavior
'''Yes, by default, Django signals run in the same thread as the caller. 
This means that if the thread that triggered the signal is the main thread, 
the signal receiver will also execute in the same thread.'''


# Same thread behavior demonstration
@receiver(post_save, sender=User)
def log_user_thread(sender, instance, created, **kwargs):
    if created:
        logging.info("QUESTION 2: Same Thread Behavior")
        current_thread = threading.current_thread().name
        logging.info(f"Signal executed in thread: {current_thread}.")


#QUESTION 3 ANSWER : Database transaction behavior
'''Yes, by default, Django signals run in the same database transaction as the caller. 
If an exception is raised during the signal processing, it will roll back the entire 
database transaction, including the changes made by the caller.'''


# Database transaction behavior demonstration
@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        logging.info("QUESTION 3: Database Transaction Behavior")
        logging.info(f"User {instance.username} has been created.")
        if instance.username == "error_trigger":
            raise ValueError("Simulating a transaction rollback.")




