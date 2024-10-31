seshat.apps.core.admin
======================

.. py:module:: seshat.apps.core.admin


Classes
-------

.. autoapisummary::

   seshat.apps.core.admin.CustomReferenceAdmin


Module Contents
---------------

.. py:class:: CustomReferenceAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:attribute:: list_display
      :value: ('title', 'created_date', 'creator')



