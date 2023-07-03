from django.dispatch import Signal,receiver

# Creating Signal

notification = Signal(providing_args=["request","user"])

# Reciever Function
@receiver(notification)
def show_notification(sender,**kwargs):
    print(sender)
    print(f'Kwargs: {kwargs}')
    print("Notification")
    