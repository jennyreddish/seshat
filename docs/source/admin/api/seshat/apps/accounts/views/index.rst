seshat.apps.accounts.views
==========================

.. py:module:: seshat.apps.accounts.views


Classes
-------

.. autoapisummary::

   seshat.apps.accounts.views.ProfileUpdate
   seshat.apps.accounts.views.Seshat_taskCreate
   seshat.apps.accounts.views.Seshat_taskDetailView


Functions
---------

.. autoapisummary::

   seshat.apps.accounts.views.accounts
   seshat.apps.accounts.views.accounts_new
   seshat.apps.accounts.views.has_add_scp_prv_permission
   seshat.apps.accounts.views.profile
   seshat.apps.accounts.views.signup


Module Contents
---------------

.. py:class:: ProfileUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Generic class-based view for updating a user's profile.


   .. py:method:: form_valid(form)

      Method for saving the form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponseRedirect



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: context_object_name
      :value: 'user'



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_seshatprivatecommentpart'



   .. py:attribute:: queryset


   .. py:attribute:: template_name
      :value: 'registration/profile_update.html'



.. py:class:: Seshat_taskCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Generic class-based view for creating a task.


   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_seshatprivatecommentpart'



   .. py:attribute:: template_name
      :value: 'registration/seshat_task/seshat_task_form.html'



.. py:class:: Seshat_taskDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   Generic class-based detail view for a task.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'registration/seshat_task/seshat_task_detail.html'



.. py:function:: accounts(request)

   View function for the accounts page.

   .. note:: TODO: This seems like an unused function and it should be removed.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: accounts_new(request)

   View function for the accounts page.

   .. note:: TODO: This seems like an unused function and it should be removed.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: has_add_scp_prv_permission(user)

   Function to check if a user has the 'core.add_seshatprivatecommentpart' permission.

   .. note::

      TODO: Investigate whether this function doubles with the functionality
      of the 'permission_required' decorator.

   :param user: The user object.
   :type user: User

   :returns: True if the user has the permission, False otherwise.
   :rtype: bool


.. py:function:: profile(request)

   View function for displaying a user's profile.

   .. note::

      This view requires that the user be logged in.
      This view requires that the user have the 'core.add_seshatprivatecommentpart' permission.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: signup(request)

   View function for signing up a new user.

   .. note:: This view function handles both GET and POST requests.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


