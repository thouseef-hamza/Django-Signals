from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print('-------------------------------------')
    print("Logged-in Signal....... Welcome To Meta World")
    print("Sender:  ",sender)
    print("Request:  ",request)
    print("User:  ",user)
    print("User Password:  ",user.password)
    print("Kwargs:  ",kwargs)
    
# user_logged_in.connect(login_success,sender=User)
    
@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print('-------------------------------------')
    print("Logged-Out Signal...Thank You For Your Valuable Time With Our World")
    print("Sender:  ",sender)
    print("Request:  ",request)
    print("User:  ",user)
    print("User Password:  ",user.password)
    print("Kwargs:  ",kwargs)       

# user_logged_out.connect(log_out,sender=User)

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print('-------------------------------------')
    print("Log-In-Failed Signal...Oh Oh Invalid Credentials,Correct Your Credentials To Access Our Meta World")
    print("Sender:  ",sender)
    print("Request:  ",request)
    print("Credentials Are  :",credentials)
    print("Kwargs:  ",kwargs)       

# user_login_failed.connect(login_failed)