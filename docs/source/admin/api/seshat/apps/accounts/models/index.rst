seshat.apps.accounts.models
===========================

.. py:module:: seshat.apps.accounts.models


Classes
-------

.. autoapisummary::

   seshat.apps.accounts.models.Profile
   seshat.apps.accounts.models.Seshat_Expert
   seshat.apps.accounts.models.Seshat_Task


Functions
---------

.. autoapisummary::

   seshat.apps.accounts.models.create_or_update_user_profile


Module Contents
---------------

.. py:class:: Profile(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model representing a user profile.


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: PUBLICUSER
      :value: 4



   .. py:attribute:: RA
      :value: 2



   .. py:attribute:: ROLE_CHOICES


   .. py:attribute:: SESHATADMIN
      :value: 1



   .. py:attribute:: SESHATEXPERT
      :value: 3



   .. py:attribute:: bio


   .. py:attribute:: email_confirmed


   .. py:attribute:: location


   .. py:attribute:: role


   .. py:attribute:: user


.. py:class:: Seshat_Expert(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model representing a Seshat Expert.


   .. py:attribute:: RA
      :value: 'RA'



   .. py:attribute:: ROLE_CHOICES


   .. py:attribute:: SESHATADMIN
      :value: 'Seshat Admin'



   .. py:attribute:: SESHATEXPERT
      :value: 'Seshat Expert'



   .. py:attribute:: role


   .. py:attribute:: user


.. py:class:: Seshat_Task(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model representing a Seshat Task.


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:property:: clickable_url
      Returns a clickable URL.

      :returns: A string of a clickable URL.
      :rtype: str


   .. py:property:: display_takers
      Returns a string of all takers of the task.

      :returns: A string of all takers of the task, joined with a HTML tag ("<br />").
      :rtype: str


   .. py:attribute:: giver


   .. py:attribute:: taker


   .. py:attribute:: task_description


   .. py:attribute:: task_url


.. py:function:: create_or_update_user_profile(sender, instance, created, **kwargs)

   Signal handler for creating or updating a user profile.


