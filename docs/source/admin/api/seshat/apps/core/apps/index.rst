seshat.apps.core.apps
=====================

.. py:module:: seshat.apps.core.apps


Classes
-------

.. autoapisummary::

   seshat.apps.core.apps.CoreConfig


Module Contents
---------------

.. py:class:: CoreConfig(app_name, app_module)

   Bases: :py:obj:`django.apps.AppConfig`


   Class representing a Django application and its configuration.


   .. py:method:: ready()

      Override this method in subclasses to run code when Django starts.



   .. py:attribute:: default_auto_field
      :value: 'django.db.models.BigAutoField'



   .. py:attribute:: name
      :value: 'seshat.apps.core'



