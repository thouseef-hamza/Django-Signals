from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    a = 10 / 0
    return HttpResponse("Hello")


# ========================================================================================================================================
"""
pre_save---------------------------------------------------------------------------------------------------------->
django.db.models.signals.pre_save

This is sent at the beginning of a model's save() method.

Arguments sent with this signal:

<>sender
    The model class.
<>instance
    The actual instance being saved.
<>raw
    A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). 
    One should not query/modify other records in the database as the database might not be in a consistent state yet.
<>using
    The database alias being used.
<>update_fields
    The set of fields to update as passed to Model.save(), or None if update_fields wasn’t passed to save().

"""
# ===============================================================================================================================================================
"""
post_save----------------------------------------------------------------------------------------------------------------->
django.db.models.signals.post_save

Like pre_save, but sent at the end of the save() method.

Arguments sent with this signal:

<>sender
    The model class.
<>instance
    The actual instance being saved.
<>created
    A boolean; True if a new record was created.
<>raw
    A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). 
    One should not query/modify other records in the database as the database might not be in a consistent state yet.
<>using
    The database alias being used.
<>update_fields
    The set of fields to update as passed to Model.save(), or None if update_fields wasn’t passed to save().
"""
# ======================================================================================================================================
""" 
pre_delete--------------------------------------------------------------------------------------------->
django.db.models.signals.pre_delete

Sent at the beginning of a model's delete() method and a queryset's delete() method.

Arguments sent with this signal:

<>sender
    The model class.
<>instance
    The actual instance being deleted.
<>using
    The database alias being used.
<>origin
    The origin of the deletion being the instance of a Model or QuerySet class.
"""
# ========================================================================================================================================
"""
post_delete---------------------------------------------------------------------------------------->
django.db.models.signals.post_delete

Like pre_delete, but sent at the end of a model's delete() method and a queryset's delete() method.

Arguments sent with this signal:

<>sender
    The model class.
<>instance
    The actual instance being deleted.

^^^^^^^                                                                                                            ^^^^^^^^^^^
        Note that the object will no longer be in the database, so be very careful what you do with this instance.
^^^^^^^                                                                                                            ^^^^^^^ 

<>using
The database alias being used.
<>origin
    The origin of the deletion being the instance of a Model or QuerySet class.
"""
# =======================================================================================================================================
"""
pre_init-------------------------------------------------------------------------------------------->
django.db.models.signals.pre_init

Whenever you instantiate a Django model, this signal is sent at the beginning of the model’s __init__() method.

Arguments sent with this signal:

<>sender
    The model class that just had an instance created.
<>args
    A list of positional arguments passed to __init__().
<>kwargs
    A dictionary of keyword arguments passed to __init__().

"""
# ========================================================================================================================================
"""
post_init--------------------------------------------------------------------------------------------->
django.db.models.signals.post_init

Like pre_init, but this one is sent when the __init__() method finishes.

Arguments sent with this signal:

<>sender
    As above: the model class that just had an instance created.
<>instance
    The actual instance of the model that's just been created.

"""
# =====================================================================================================================================
"""
request_started--------------------------------------------------------------------------------------->
django.core.signals.request_started

Sent when Django begins processing an HTTP request.

Arguments sent with this signal:

<>sender
    The handler class - e.g. django.core.handlers.wsgi.WsgiHandler - that handled the request.
<>environ
    The environ dictionary provided to the request.

"""
# =====================================================================================================================================
"""
request_finished
django.core.signals.request_finished

Sent when Django finishes delivering an HTTP response to the client.

Arguments sent with this signal:

<>sender
    The handler class, as above.
"""
# ======================================================================================================================================
"""
pre_migrate-------------------------------------------------------------------------------------->
django.db.models.signals.pre_migrate

Sent by the migrate command before it starts to install an application. 
It's not emitted for applications that lack a models module.

Arguments sent with this signal:

<>sender
    An AppConfig instance for the application about to be migrated/synced.
<>app_config
    Same as sender.
<>verbosity
    Indicates how much information manage.py is printing on screen. See the --verbosity flag for details.

Functions which listen for pre_migrate should adjust what they output to the screen based on the value of this argument.

<>interactive
    If interactive is True, it's safe to prompt the user to input things on the command line. 
    If interactive is False, functions which listen for this signal should not try to prompt for anything.
    
For example, the django.contrib.auth app only prompts to create a superuser when interactive is True.

<>stdout
    A stream-like object where verbose output should be redirected.
<>using
    The alias of database on which a command will operate.
<>plan
    The migration plan that is going to be used for the migration run. While the plan is not public API, 
    this allows for the rare cases when it is necessary to know the plan. 
    A plan is a list of two-tuples with the first item being the instance of a migration class and 
    the second item showing if the migration was rolled back (True) or applied (False).
<>apps
    An instance of Apps containing the state of the project before the migration run. 
    It should be used instead of the global apps registry to retrieve the models you want to perform operations on.
"""
# ========================================================================================================================================
"""
post_migrate
django.db.models.signals.post_migrate

Sent at the end of the migrate (even if no migrations are run) and flush commands. 
It's not emitted for applications that lack a models module.

Handlers of this signal must not perform database schema alterations as doing so may cause 
the flush command to fail if it runs during the migrate command.

Arguments sent with this signal:

<>sender
    An AppConfig instance for the application that was just installed.
<>app_config
    Same as sender.
<>verbosity
    Indicates how much information manage.py is printing on screen. See the --verbosity flag for details.

Functions which listen for post_migrate should adjust what they output to the screen based on the value of this argument.

<>interactive
    If interactive is True, it's safe to prompt the user to input things on the command line. 
    If interactive is False, functions which listen for this signal should not try to prompt for anything.

For example, the django.contrib.auth app only prompts to create a superuser when interactive is True.

<>stdout
    A stream-like object where verbose output should be redirected.
<>using
    The database alias used for synchronization. Defaults to the default database.
<>plan
    The migration plan that was used for the migration run. While the plan is not public API, 
    this allows for the rare cases when it is necessary to know the plan. A plan is a list of two-tuples with 
    the first item being the instance of a migration class and the second item showing 
    if the migration was rolled back (True) or applied (False).
<>apps
    An instance of Apps containing the state of the project after the migration run. 
    It should be used instead of the global apps registry to retrieve the models you want to perform operations on.

"""
# =====================================================================================================================================
"""
connection_created
django.db.backends.signals.connection_created

Sent when the database wrapper makes the initial connection to the database. 
This is particularly useful if you'd like to send any post connection commands to the SQL backend.

Arguments sent with this signal:

<>sender
    The database wrapper class - i.e. django.db.backends.postgresql.DatabaseWrapper or django.db.backends.mysql.DatabaseWrapper, etc.
<>connection
    The database connection that was opened. 
    This can be used in a multiple-database configuration to differentiate connection signals from different databases.
"""