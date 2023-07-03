from django.shortcuts import render

# Create your views here.

#========================================================================================================================================
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
#===============================================================================================================================================================
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
#======================================================================================================================================
""" 
pre_delete--------------------------------------------------------------------------------------------->
django.db.models.signals.pre_delete

Sent at the beginning of a model’s delete() method and a queryset’s delete() method.

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
#========================================================================================================================================
"""
post_delete---------------------------------------------------------------------------------------->
django.db.models.signals.post_delete

Like pre_delete, but sent at the end of a model’s delete() method and a queryset’s delete() method.

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
#=======================================================================================================================================
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
#========================================================================================================================================
"""
post_init--------------------------------------------------------------------------------------------->
django.db.models.signals.post_init

Like pre_init, but this one is sent when the __init__() method finishes.

Arguments sent with this signal:

<>sender
    As above: the model class that just had an instance created.
<>instance
    The actual instance of the model that’s just been created.

"""