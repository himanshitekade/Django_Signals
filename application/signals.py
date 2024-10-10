
'''The default behavior of Django signals is that they are executed synchronously. 
This means that when a signal is sent, the corresponding signal receiver function 
is executed immediately, and the code execution will pause until the receiver 
has completed its execution before proceeding to the next line of code.'''



from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import time


# Signal receiver that triggers after a User is saved
@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if created:
        print(f"User {instance.username} has been created.")
        
        # Simulate a time-consuming task
        time.sleep(5)
        
        print("Signal processing finished after 5 seconds delay.")
