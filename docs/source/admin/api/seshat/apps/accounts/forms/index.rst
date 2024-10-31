seshat.apps.accounts.forms
==========================

.. py:module:: seshat.apps.accounts.forms


Classes
-------

.. autoapisummary::

   seshat.apps.accounts.forms.CustomSignUpForm
   seshat.apps.accounts.forms.ProfileForm
   seshat.apps.accounts.forms.Seshat_TaskForm


Module Contents
---------------

.. py:class:: CustomSignUpForm(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.forms.UserCreationForm`


   Form for signing up a user.


   .. py:method:: clean_email()

      A method to clean the email field and check if it contains too many
      dots in the username part.

      :returns: The email address if it is valid.
      :rtype: str

      :raises ValidationError: If the email address contains too many dots in the
          username part.



.. py:class:: ProfileForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a profile.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ['first_name', 'last_name', 'role', 'location', 'bio']



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



   .. py:attribute:: first_name


   .. py:attribute:: last_name


.. py:class:: Seshat_TaskForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a task.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ['giver', 'taker', 'task_description', 'task_url']



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



