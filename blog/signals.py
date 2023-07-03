from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print('--------------------------------------------------------------------------------------------------------------------------->')
    print("Logged-in Signal....... Welcome To Meta World")
    print("Sender:  ",sender)
    print("Request:  ",request)
    print("User:  ",user)
    print("User Password:  ",user.password)
    print("Kwargs:  ",kwargs)
    
# user_logged_in.connect(login_success,sender=User)
    
@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print('--------------------------------------------------------------------------------------------------------------------------->')
    print("Logged-Out Signal...Thank You For Your Valuable Time With Our World")
    print("Sender:  ",sender)
    print("Request:  ",request)
    print("User:  ",user)
    print("User Password:  ",user.password)
    print("Kwargs:  ",kwargs)       

# user_logged_out.connect(log_out,sender=User)

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print('-------------------------------------------------------------------------------------------------------------------------->')
    print("Log-In-Failed Signal...Oh Oh Invalid Credentials,Correct Your Credentials To Access Our Meta World")
    print("Sender:  ",sender)
    print("Request:  ",request)
    print("Credentials Are  :",credentials)
    print("Kwargs:  ",kwargs)       

# user_login_failed.connect(login_failed)

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Pre Save Signal.............")
    print("Sender:  ",sender)
    print("Instance:  ",instance)
    print("Kwargs:  ",kwargs)

# pre_save.connect(at_beginning_save,sender=User)

@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("----------------------------------------------------------------------------------------------------------------------->")
        print("Post Save Signal.....")
        print("Sender:  ",sender)
        print("Instance:  ",instance)
        print("Created:  ",created)
        print("Kwargs:  ",kwargs)
    else:
        print("----------------------------------------------------------------------------------------------------------------------->")
        print("Post Save Signal.......")
        print("UPDATED")
        print("Sender:  ",sender)
        print("Instance:  ",instance)
        print("Created:  ",created)
        print("Kwargs:  ",kwargs)

# post_save.connect(at_ending_save,sender=User)

@receiver(pre_delete,sender=User)
def at_beginning_delete(sender,instance,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Pre Delete Signal.............")
    print("Sender:  ",sender)
    print("Instance:  ",instance)
    print("Kwargs:  ",kwargs)
    
# pre_delete.connect(at_beginning_delete,sender=User)

@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Post Delete Signal.............")
    print("Sender:  ",sender)
    print("Instance:  ",instance)
    print("Kwargs:  ",kwargs)
    
# post_delete.connect(at_ending_delete,sender=User)


@receiver(pre_init,sender=User)
def at_beginning_init(sender,*args,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Pre Init Signal.............")
    print("Sender:  ",sender)
    print("Args:  ",args)
    print("Kwargs:  ",kwargs)
    
# pre_init.connect(at_beginning_init,sender=User)

@receiver(post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Post Init Signal.............")
    print("Sender:  ",sender)
    print("Args:  ",args)
    print("Kwargs:  ",kwargs)
    
# post_init.connect(at_ending_init,sender=User)

@receiver(request_started)
def at_beginning_request(sender,environ,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("At Beginning Request Started.............")
    print("Sender:  ",sender)
    print("Environ:  ",environ)
    print("Kwargs:  ",kwargs)
    
# request_started.connect(at_beginning_request)

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("At Ending Request.............")
    print("Sender:  ",sender)
    print("Kwargs:  ",kwargs)
    
# request_finished.connect(at_beginning_request)

@receiver(got_request_exception)
def at_request_exception(sender,request,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("At Request Exception.............")
    print("Sender:  ",sender)
    print("Request:  ",request)
    print("Kwargs:  ",kwargs)
     
# got_request_exception.connect(at_request_exception)

@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Pre Migrate.............")
    print("Sender:  ",sender)
    print("AppConfig:  ",app_config)
    print("Interactive:  ",interactive)
    print("Verbosity:  ",verbosity)
    print("Using:  ",using)
    print("Plan:  ",plan)
    print("Apps:  ",apps)
    print("Kwargs:  ",kwargs)
    
# pre_migrate.connect(before_install_app)

@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Post Migrate.............")
    print("Sender:  ",sender)
    print("AppConfig:  ",app_config)
    print("Interactive:  ",interactive)
    print("Verbosity:  ",verbosity)
    print("Using:  ",using)
    print("Plan:  ",plan)
    print("Apps:  ",apps)
    print("Kwargs:  ",kwargs)

# post_migrate.connect(at_end_migrate_flush)

@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print("------------------------------------------------------------------------------------------------------------------------->")
    print("Initial connection to database........")
    print("Sender:  ",sender)
    print("Connection:  ",connection)
    print("Kwargs:  ",kwargs)

# connection_created.connect(conn_db)
    
    