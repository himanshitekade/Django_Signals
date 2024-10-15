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
has completed its execution before proceeding to the next line of code.

Importance in real-world applications:
Synchronous signals can block the main thread, especially if they involve 
long-running tasks like sending emails or processing heavy data. This can lead to 
delays in the response time for users. In such cases, offloading these tasks to 
an asynchronous task queue (like Celery) would improve performance.'''


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
the signal receiver will also execute in the same thread.

Importance in real-world applications:
Running in the same thread ensures that the signal receiver shares the same 
resources (like memory and database connections) as the caller. While this is 
efficient for short tasks, long-running tasks should be moved to separate threads 
or async systems to avoid blocking the main thread.'''



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
database transaction, including the changes made by the caller.

Importance in real-world applications:
This behavior ensures data consistency. If something goes wrong in the signal handler, 
the changes made in the main logic will not be saved to the database, preventing 
partial or corrupt data from being committed. However, developers should be careful 
about which exceptions are allowed to propagate, as some exceptions might rollback 
transactions unnecessarily.'''


# Database transaction behavior demonstration
@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        logging.info("QUESTION 3: Database Transaction Behavior")
        logging.info(f"User {instance.username} has been created.")
        if instance.username == "error_trigger":
            raise ValueError("Simulating a transaction rollback.")




