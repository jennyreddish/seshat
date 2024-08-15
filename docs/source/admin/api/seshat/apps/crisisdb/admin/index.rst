seshat.apps.crisisdb.admin
==========================

.. py:module:: seshat.apps.crisisdb.admin


Classes
-------

.. autoapisummary::

   seshat.apps.crisisdb.admin.UsLocationAdmin
   seshat.apps.crisisdb.admin.UsViolenceDataSourceAdmin
   seshat.apps.crisisdb.admin.UsViolenceSubtypeAdmin


Module Contents
---------------

.. py:class:: UsLocationAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:attribute:: list_display
      :value: ['us_state', 'city', 'county', 'special_place']



   .. py:attribute:: list_filter
      :value: ['us_state', 'city', 'county']



   .. py:attribute:: search_fields
      :value: ['us_state', 'city', 'county', 'special_place']



.. py:class:: UsViolenceDataSourceAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:attribute:: list_display
      :value: ['name', 'abbreviation', 'is_uncertain', 'attention_tag']



   .. py:attribute:: list_filter
      :value: ['is_uncertain', 'attention_tag']



   .. py:attribute:: search_fields
      :value: ['name', 'abbreviation']



.. py:class:: UsViolenceSubtypeAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:attribute:: list_display
      :value: ['name', 'is_uncertain']



   .. py:attribute:: list_filter
      :value: ['is_uncertain']



   .. py:attribute:: search_fields
      :value: ['name']



