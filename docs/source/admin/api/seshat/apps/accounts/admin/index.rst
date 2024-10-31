seshat.apps.accounts.admin
==========================

.. py:module:: seshat.apps.accounts.admin


Classes
-------

.. autoapisummary::

   seshat.apps.accounts.admin.CustomUserAdmin
   seshat.apps.accounts.admin.ProfileInline


Module Contents
---------------

.. py:class:: CustomUserAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:method:: get_email_confirmed(instance)


   .. py:method:: get_inline_instances(request, obj=None)


   .. py:method:: get_location(instance)


   .. py:attribute:: inlines


   .. py:attribute:: list_display
      :value: ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'last_login',...



   .. py:attribute:: list_select_related
      :value: ('profile',)



.. py:class:: ProfileInline(parent_model, admin_site)

   Bases: :py:obj:`django.contrib.admin.StackedInline`


   Options for inline editing of ``model`` instances.

   Provide ``fk_name`` to specify the attribute name of the ``ForeignKey``
   from ``model`` to its parent. This is required if ``model`` has more than
   one ``ForeignKey`` to its parent.


   .. py:attribute:: can_delete
      :value: False



   .. py:attribute:: fk_name
      :value: 'user'



   .. py:attribute:: model


   .. py:attribute:: verbose_name_plural
      :value: 'Profile'



