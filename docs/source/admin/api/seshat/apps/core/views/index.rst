seshat.apps.core.views
======================

.. py:module:: seshat.apps.core.views


Attributes
----------

.. autoapisummary::

   seshat.apps.core.views.POLITY_RELIGIOUS_TRADITION_CHOICES
   seshat.apps.core.views.app_map
   seshat.apps.core.views.categorical_variables
   seshat.apps.core.views.world_map_initial_displayed_year
   seshat.apps.core.views.world_map_initial_polity


Classes
-------

.. autoapisummary::

   seshat.apps.core.views.CapitalCreate
   seshat.apps.core.views.CapitalDelete
   seshat.apps.core.views.CapitalListView
   seshat.apps.core.views.CapitalUpdate
   seshat.apps.core.views.CitationCreate
   seshat.apps.core.views.CitationDelete
   seshat.apps.core.views.CitationDetailView
   seshat.apps.core.views.CitationListView
   seshat.apps.core.views.CitationUpdate
   seshat.apps.core.views.NgaCreate
   seshat.apps.core.views.NgaDetailView
   seshat.apps.core.views.NgaListView
   seshat.apps.core.views.NgaUpdate
   seshat.apps.core.views.NlpReferenceListView
   seshat.apps.core.views.PolityCreate
   seshat.apps.core.views.PolityDetailView
   seshat.apps.core.views.PolityListView
   seshat.apps.core.views.PolityListView1
   seshat.apps.core.views.PolityListViewCommented
   seshat.apps.core.views.PolityListViewLight
   seshat.apps.core.views.PolityListViewX
   seshat.apps.core.views.PolityListView_old
   seshat.apps.core.views.PolityUpdate
   seshat.apps.core.views.ReferenceCreate
   seshat.apps.core.views.ReferenceDelete
   seshat.apps.core.views.ReferenceDetailView
   seshat.apps.core.views.ReferenceListView
   seshat.apps.core.views.ReferenceUpdate
   seshat.apps.core.views.ReligionListView
   seshat.apps.core.views.SeshatCommentCreate
   seshat.apps.core.views.SeshatCommentDelete
   seshat.apps.core.views.SeshatCommentDetailView
   seshat.apps.core.views.SeshatCommentListView
   seshat.apps.core.views.SeshatCommentPartCreate
   seshat.apps.core.views.SeshatCommentPartCreate2
   seshat.apps.core.views.SeshatCommentPartDelete
   seshat.apps.core.views.SeshatCommentPartDetailView
   seshat.apps.core.views.SeshatCommentPartListView
   seshat.apps.core.views.SeshatCommentPartListView3
   seshat.apps.core.views.SeshatCommentPartUpdate
   seshat.apps.core.views.SeshatCommentUpdate
   seshat.apps.core.views.SeshatPrivateCommentPartCreate2
   seshat.apps.core.views.SeshatPrivateCommentPartUpdate
   seshat.apps.core.views.SeshatPrivateCommentUpdate


Functions
---------

.. autoapisummary::

   seshat.apps.core.views.account_activation_sent
   seshat.apps.core.views.activate
   seshat.apps.core.views.ajax_test
   seshat.apps.core.views.assign_categorical_variables_to_shapes
   seshat.apps.core.views.assign_variables_to_shapes
   seshat.apps.core.views.capital_download
   seshat.apps.core.views.cliopatria
   seshat.apps.core.views.create_a_comment_with_a_subcomment_new
   seshat.apps.core.views.create_a_comment_with_a_subcomment_newer
   seshat.apps.core.views.create_a_private_comment_with_a_private_subcomment_new
   seshat.apps.core.views.discussion_room
   seshat.apps.core.views.do_zotero
   seshat.apps.core.views.do_zotero_manually
   seshat.apps.core.views.download_csv_all_polities
   seshat.apps.core.views.download_oldcsv
   seshat.apps.core.views.four_o_four
   seshat.apps.core.views.get_all_polity_capitals
   seshat.apps.core.views.get_or_create_citation
   seshat.apps.core.views.get_polity_data_single
   seshat.apps.core.views.get_polity_shape_content
   seshat.apps.core.views.get_provinces
   seshat.apps.core.views.index
   seshat.apps.core.views.is_ajax
   seshat.apps.core.views.map_view_all
   seshat.apps.core.views.map_view_all_with_vars
   seshat.apps.core.views.map_view_initial
   seshat.apps.core.views.nlp_datapoints
   seshat.apps.core.views.nlp_datapoints_2
   seshat.apps.core.views.no_zotero_refs_list
   seshat.apps.core.views.polity_filter_options_view
   seshat.apps.core.views.provinces_and_countries_view
   seshat.apps.core.views.random_polity_shape
   seshat.apps.core.views.reference_update_modal
   seshat.apps.core.views.references_download
   seshat.apps.core.views.religion_create
   seshat.apps.core.views.religion_update
   seshat.apps.core.views.search_suggestions
   seshat.apps.core.views.search_view
   seshat.apps.core.views.seshat_comment_part_create_from_null_view
   seshat.apps.core.views.seshat_comment_part_create_from_null_view_OLD
   seshat.apps.core.views.seshat_comment_part_create_from_null_view_inline
   seshat.apps.core.views.seshat_private_comment_part_create_from_null_view
   seshat.apps.core.views.seshatacknowledgements
   seshat.apps.core.views.seshatcodebooknew1
   seshat.apps.core.views.seshatcodebookold
   seshat.apps.core.views.seshatcomment_create_view
   seshat.apps.core.views.seshatcommentpart_create_view
   seshat.apps.core.views.seshatcommentpart_create_view_old
   seshat.apps.core.views.seshatindex
   seshat.apps.core.views.seshatindex2
   seshat.apps.core.views.seshatmethods
   seshat.apps.core.views.seshatolddownloads
   seshat.apps.core.views.seshatwhoweare
   seshat.apps.core.views.signup_traditional
   seshat.apps.core.views.signupfollowup
   seshat.apps.core.views.synczotero
   seshat.apps.core.views.synczotero100
   seshat.apps.core.views.synczoteromanually
   seshat.apps.core.views.update_citations
   seshat.apps.core.views.update_citations_from_inside_zotero_update
   seshat.apps.core.views.update_seshat_comment_part_view
   seshat.apps.core.views.variablehierarchysetting
   seshat.apps.core.views.xxyyzz


Module Contents
---------------

.. py:class:: CapitalCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new Capital.


   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'You successfully created a new Capital.'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/capital/capital_form_create.html'



.. py:class:: CapitalDelete(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.DeleteView`


   Delete a Capital.


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'You successfully deleted one Capital.'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/delete_general.html'



.. py:class:: CapitalListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all Capitals.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/capital/capital_list.html'



.. py:class:: CapitalUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update a Capital.


   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'You successfully updated the Capital.'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/capital/capital_form.html'



.. py:class:: CitationCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new citation.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'Yoohoooo...'



   .. py:attribute:: template_name
      :value: 'core/references/citation_form.html'



.. py:class:: CitationDelete(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.DeleteView`


   Delete a citation.


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/delete_general.html'



.. py:class:: CitationDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   Display the details of a citation.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/references/citation_detail.html'



.. py:class:: CitationListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all citations.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:attribute:: model


   .. py:attribute:: paginate_by
      :value: 20



   .. py:attribute:: template_name
      :value: 'core/references/citation_list.html'



.. py:class:: CitationUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update a citation.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'Yoohoooo...'



   .. py:attribute:: template_name
      :value: 'core/references/citation_update.html'



.. py:class:: NgaCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new NGA.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/nga/nga_form.html'



.. py:class:: NgaDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   Show details of an NGA.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/nga/nga_detail.html'



.. py:class:: NgaListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all NGAs.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/nga/nga_list.html'



.. py:class:: NgaUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update an NGA.


   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'You successfully updated the Nga.'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/nga/nga_update.html'



.. py:class:: NlpReferenceListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all NLP references.


   .. py:method:: get_absolute_url()

      Return the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_queryset()

      Return the queryset of NLP references.

      :returns: The queryset of NLP references.
      :rtype: QuerySet



   .. py:attribute:: model


   .. py:attribute:: paginate_by
      :value: 50



   .. py:attribute:: template_name
      :value: 'core/references/nlp_reference_list.html'



.. py:class:: PolityCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new Polity.


   .. py:method:: form_invalid(form)

      If the form is invalid, render the invalid form.



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/polity/polity_form.html'



.. py:class:: PolityDetailView(**kwargs)

   Bases: :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.DetailView`


   Show details of a polity.


   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:method:: get_object(queryset=None)

      Get the object of the view.

      :param queryset: The queryset to use.

      :returns: The object of the view.
      :rtype: Polity

      :raises Http404: If no polity matches the given name.
      :raises Http404: If multiple polities are found with the same name.



   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/polity/polity_detail.html'



.. py:class:: PolityListView(**kwargs)

   Bases: :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.ListView`


   List all polities.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/polity/polity_list.html'



.. py:class:: PolityListView1(**kwargs)

   Bases: :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.ListView`


   List all polities.

   .. note:: This class is not used in the current implementation.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/polity/polity_list.html'



.. py:class:: PolityListViewCommented(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.ListView`


   List all polities with comments.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_seshatprivatecommentpart'



   .. py:attribute:: template_name
      :value: 'core/polity/polity_list_commented.html'



.. py:class:: PolityListViewLight(**kwargs)

   Bases: :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.ListView`


   List all polities.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/polity/polity_list_light.html'



.. py:class:: PolityListViewX(**kwargs)

   Bases: :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.ListView`


   List all polities.

   .. note:: This class is not used in the current implementation.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/polity/polity_list.html'



.. py:class:: PolityListView_old(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.ListView`


   List all polities.

   .. note:: This class is not used in the current implementation.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/polity/polity_list.html'



.. py:class:: PolityUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update a Polity.


   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:method:: get_success_url()

      Return the URL to redirect to after processing a valid form.



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'You successfully updated the Polity.'



   .. py:attribute:: template_name
      :value: 'core/polity/polity_form.html'



.. py:class:: ReferenceCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new reference.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/references/reference_form.html'



.. py:class:: ReferenceDelete(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.DeleteView`


   Delete a reference.


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/delete_general.html'



.. py:class:: ReferenceDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   Display the details of a reference.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/references/reference_detail.html'



.. py:class:: ReferenceListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all references.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_queryset()

      Get the queryset of references.

      :returns: The queryset of references.
      :rtype: QuerySet



   .. py:attribute:: model


   .. py:attribute:: paginate_by
      :value: 100



   .. py:attribute:: template_name
      :value: 'core/references/reference_list.html'



.. py:class:: ReferenceUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update a reference.


   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/references/reference_update.html'



.. py:class:: ReligionListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all religions.


   .. py:attribute:: context_object_name
      :value: 'religions'



   .. py:attribute:: model


   .. py:attribute:: ordering
      :value: ['religion_name']



   .. py:attribute:: permission_required
      :value: 'core.add_seshatprivatecommentpart'



   .. py:attribute:: template_name
      :value: 'core/religion_list.html'



.. py:class:: SeshatCommentCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new comment.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcomment_form.html'



.. py:class:: SeshatCommentDelete(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.DeleteView`


   Delete a comment.


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_url


   .. py:attribute:: template_name
      :value: 'core/delete_general.html'



.. py:class:: SeshatCommentDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   Display the details of a comment.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcomment_detail.html'



.. py:class:: SeshatCommentListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all comments.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:attribute:: model


   .. py:attribute:: paginate_by
      :value: 20



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcomment_list.html'



.. py:class:: SeshatCommentPartCreate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new comment part.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcommentpart_form.html'



.. py:class:: SeshatCommentPartCreate2(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new comment part.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcommentpart_form_prefilled.html'



.. py:class:: SeshatCommentPartDelete(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.DeleteView`


   Delete a comment part.


   .. py:method:: get_success_url()

      Return the URL to redirect to after processing a valid form.



   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/delete_general.html'



.. py:class:: SeshatCommentPartDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   Render a "detail" view of an object.

   By default this is a model instance looked up from `self.queryset`, but the
   view will support display of *any* object by overriding `self.get_object()`.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcommentpart_detail.html'



.. py:class:: SeshatCommentPartListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all comment parts.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:attribute:: model


   .. py:attribute:: paginate_by
      :value: 20



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcommentpart_list.html'



.. py:class:: SeshatCommentPartListView3(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   List all comment parts.


   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:attribute:: model


   .. py:attribute:: paginate_by
      :value: 20



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcommentpart_list3.html'



.. py:class:: SeshatCommentPartUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update a comment part.


   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: success_message
      :value: 'You successfully updated the subdescription.'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcommentpart_update.html'



.. py:class:: SeshatCommentUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update a comment.


   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_capital'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatcomment_update.html'



.. py:class:: SeshatPrivateCommentPartCreate2(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Create a new private comment part.


   .. py:method:: form_invalid(form)

      Handle invalid form data.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: form_valid(form)

      Validate the form.

      :param form: The form object.
      :type form: Form

      :returns: The response object.
      :rtype: HttpResponse



   .. py:method:: get_absolute_url()

      Get the absolute URL of the view.

      :returns: The absolute URL of the view.
      :rtype: str



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_seshatprivatecommentpart'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatprivatecommentpart_form_prefilled.html'



.. py:class:: SeshatPrivateCommentPartUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.contrib.messages.views.SuccessMessageMixin`, :py:obj:`django.views.generic.edit.UpdateView`


   Update a private comment part.


   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_seshatprivatecommentpart'



   .. py:attribute:: success_message
      :value: 'You successfully updated the Private comment.'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatprivatecommentpart_update2.html'



.. py:class:: SeshatPrivateCommentUpdate(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.PermissionRequiredMixin`, :py:obj:`django.views.generic.edit.UpdateView`, :py:obj:`django.views.generic.edit.FormMixin`


   View to update a SeshatPrivateComment instance.


   .. py:method:: get_another_form(request, *args, **kwargs)

      Return the data from another form in the SeshatPrivateCommentPartForm.

      :param request: The request object.
      :param \*args: Variable length argument list.
      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The form instance.
      :rtype: SeshatPrivateCommentPartForm



   .. py:method:: get_context_data(**kwargs)

      Get the context data of the view.

      :noindex:

      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The context data of the view.
      :rtype: dict



   .. py:method:: post(request, *args, **kwargs)

      Handle POST requests: instantiate a form instance with the passed
      POST variables and then check if it's valid.

      :param request: The request object.
      :param \*args: Variable length argument list.
      :param \*\*kwargs: Arbitrary keyword arguments.

      :returns: The HTTP response.
      :rtype: HttpResponse



   .. py:attribute:: form_class


   .. py:attribute:: model


   .. py:attribute:: permission_required
      :value: 'core.add_seshatprivatecommentpart'



   .. py:attribute:: template_name
      :value: 'core/seshatcomments/seshatprivatecomment_update.html'



.. py:function:: account_activation_sent(request)

   Render the account activation sent page.


.. py:function:: activate(request, uidb64, token)

   Activate user account.

   :param request: The request object.
   :param uidb64: The user ID encoded in base64.
   :param token: The token.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: ajax_test(request)

   Test if the request is an AJAX request.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: assign_categorical_variables_to_shapes(shapes, variables)

   Assign the categorical variables to the shapes.

   .. note:: Currently only language and religion variables are implemented.

   :param shapes: The shapes to assign the variables to.
   :type shapes: list
   :param variables: The variables to assign to the shapes.
   :type variables: dict

   :returns: A tuple containing the shapes and the variables.
   :rtype: tuple


.. py:function:: assign_variables_to_shapes(shapes, app_map)

   Assign the absent/present variables to the shapes.

   :param shapes: The shapes to assign the variables to.
   :type shapes: list
   :param app_map: A dictionary mapping app names to their long names.
   :type app_map: dict

   :returns: A tuple containing the shapes and the variables.
   :rtype: tuple


.. py:function:: capital_download(request)

   Download all Capitals as CSV.

   .. note:: This view is only accessible to users with the 'view_capital' permission.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: cliopatria(request)

.. py:function:: create_a_comment_with_a_subcomment_new(request, app_name, model_name, instance_id)

   Create a Comment and assign it to a model instance.

   .. note::

      This view has the login_required decorator to ensure that only
      logged-in users can access it.

   :param request: The request object.
   :param app_name: The name of the app containing the model.
   :param model_name: The name of the model.
   :param instance_id: The id of the model instance.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: create_a_comment_with_a_subcomment_newer(request, app_name, model_name, instance_id)

   Create the first chunk of a new comment and assign it to a model instance and a seshat comment.
   Get the data on citations and do the appropriate assignments there as well.


.. py:function:: create_a_private_comment_with_a_private_subcomment_new(request, app_name, model_name, instance_id)

   Create a PrivateComment and assign it to a model instance.

   .. note:: This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

   :param request: The request object.
   :param app_name: The name of the app containing the model.
   :param model_name: The name of the model.
   :param instance_id: The id of the model instance.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: discussion_room(request)

   Render the discussion room page.


.. py:function:: do_zotero(results)

   Process the results from the Zotero API.

   :param results: The results from the Zotero API.

   :returns: A list of dictionaries containing the processed data.
   :rtype: list


.. py:function:: do_zotero_manually(results)

   Process the results from the Zotero API.

   :param results: The results from the Zotero API.

   :returns: A list of dictionaries containing the processed data.
   :rtype: list


.. py:function:: download_csv_all_polities(request)

   Download a CSV file containing all polities.

   .. note:: This view is restricted to users with the 'view_capital' permission.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: download_oldcsv(request, file_name)

   Download a CSV file.

   :param request: The request object.
   :param file_name: The name of the file to download.
   :type file_name: str

   :returns: The file response.
   :rtype: FileResponse


.. py:function:: four_o_four(request)

   Return a 404 error page.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: get_all_polity_capitals()

   Get capital cities for polities that have them.

   :returns: A dictionary containing the capital cities for polities.
   :rtype: dict


.. py:function:: get_or_create_citation(reference, page_from, page_to)

   Get or create a Citation instance. If a matching citation already exists, it
   is returned; otherwise, a new one is created.

   :param reference: The reference.
   :type reference: Reference
   :param page_from: The starting page number.
   :type page_from: int
   :param page_to: The ending page number.
   :type page_to: int

   :returns: The Citation instance.
   :rtype: Citation


.. py:function:: get_polity_data_single(polity_id)

   Get the data for a single polity. The returned data includes the number of
   records for each app (general, sc, wf, hs, cc, pt).

   :param polity_id: The ID of the polity.

   :returns: The data for the polity.
   :rtype: dict


.. py:function:: get_polity_shape_content(displayed_year='all', seshat_id='all', tick_number=80, override_earliest_year=None, override_latest_year=None, geometries=True)

   This function returns the polity shapes and other content for the map.
   Only one of displayed_year or seshat_id should be set; not both.

   .. note:: seshat_id in Cliopatria is new_name in Polity.

   :param displayed_year: The year to display the polities for. "all" will return all polities. Any given year will return polities that were active in that year.
   :type displayed_year: str
   :param seshat_id: The seshat_id of the polity to display. If a value is provided, only the shapes for that polity being returned.
   :type seshat_id: str

   :returns: The content for the polity shapes.
   :rtype: dict


.. py:function:: get_provinces(selected_base_map_gadm='province')

   Get all the province or country shapes for the map base layer.

   :param selected_base_map_gadm: The selected base map GADM level.
   :type selected_base_map_gadm: str

   :returns: A list of dictionaries containing the province or country shapes.
   :rtype: list


.. py:function:: index(request)

   Returns a simple "Hello World" response.

   .. note::

      This is a simple view to test the server. It is not part of the
      application.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: is_ajax(request)

   Return True if the request is an AJAX request, False otherwise.

   :param request: The request object.
   :type request: HttpRequest

   :returns: True if the request is an AJAX request, False otherwise.
   :rtype: bool


.. py:function:: map_view_all(request)

   This view is used to display a map with polities plotted on it. The view
   loads all polities for the range of years.

   :param request: The request object.

   :returns: The HTTP response with serialized JSON.
   :rtype: JsonResponse


.. py:function:: map_view_all_with_vars(request)

   This view is used to display a map with polities plotted on it. The view
   loads all polities for the range of years with added variables for each polity shape.

   :param request: The request object.

   :returns: The HTTP response with serialized JSON.
   :rtype: JsonResponse


.. py:function:: map_view_initial(request)

.. py:function:: nlp_datapoints(request)

   Render the NLP data points page.


.. py:function:: nlp_datapoints_2(request)

   Render the NLP data points page.


.. py:function:: no_zotero_refs_list(request)

   List all references without a Zotero link.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: polity_filter_options_view(request)

   This view returns the options for the polity filter.

   .. note::

      The view is decorated with the `require_GET` decorator to ensure that
      only GET requests are allowed.

   :param request: The request object.

   :returns: The JSON response.
   :rtype: JsonResponse


.. py:function:: provinces_and_countries_view(request)

   This view is used to get the provinces and countries for the map.

   :param request: The request object.

   :returns: The HTTP response with serialized JSON.
   :rtype: JsonResponse


.. py:function:: random_polity_shape(from_selection=True)

   This function is used to get a pseudo-random polity for the map_view_initial and map_view_initial views to display.
   It selects a polity with a large area and which has a seshat_id.

   If from_selection is true, choose a polity from a pre-approved list.
   TODO: if the loading time of map_view_initial becomes sufficiently fast, we could set from_selection to False.

   :returns: A tuple containing the start year and seshat_id.
   :rtype: tuple


.. py:function:: reference_update_modal(request, pk)

   Update a reference using a modal or a standalone page depending on the
   request.

   :param request: The request object.
   :type request: HttpRequest
   :param pk: The primary key of the reference.
   :type pk: int

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: references_download(request)

   Download all references as a CSV file.

   .. note:: This view is only accessible to users with the 'view_capital' permission.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: religion_create(request)

   Create a new religion.

   .. note:: This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: religion_update(request, pk)

   Update an existing religion.

   .. note:: This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

   :param request: The request object.
   :type request: HttpRequest
   :param pk: The primary key of the religion.
   :type pk: int

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: search_suggestions(request)

   View to get search suggestions for a polity.

   .. note:: This view can handle GET requests.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: search_view(request)

   View to search for a polity.

   .. note:: This view can handle GET requests.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: seshat_comment_part_create_from_null_view(request, com_id, subcom_order)

   Create a new comment part.

   .. note:: This view is only accessible to users with the 'add_capital' permission.

   :param request: The request object.
   :type request: HttpRequest
   :param com_id: The primary key of the comment.
   :type com_id: int
   :param subcom_order: The order of the comment part.
   :type subcom_order: int

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshat_comment_part_create_from_null_view_OLD(request, com_id, subcom_order)

   Create a new comment part.

   .. note::

      This function is not used in the current implementation.
      This view is only accessible to users with the 'add_capital' permission.

   :param request: The request object.
   :type request: HttpRequest
   :param com_id: The primary key of the comment.
   :type com_id: int
   :param subcom_order: The order of the comment part.
   :type subcom_order: int

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshat_comment_part_create_from_null_view_inline(request, app_name, model_name, instance_id)

.. py:function:: seshat_private_comment_part_create_from_null_view(request, private_com_id)

   Create a new private comment part.

   .. note:: This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

   :param request: The request object.
   :type request: HttpRequest
   :param private_com_id: The primary key of the private comment.
   :type private_com_id: int

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshatacknowledgements(request)

   Return the Seshat "Acknowledgements" page.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshatcodebooknew1(request)

.. py:function:: seshatcodebookold(request)

   Return the Seshat "Codebook" page.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshatcomment_create_view(request)

   View to create a SeshatComment instance.

   .. note:: This view can handle POST and GET requests.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: seshatcommentpart_create_view(request)

   Create a new SeshatCommentPart instance.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: seshatcommentpart_create_view_old(request)

   Create a new SeshatCommentPart instance.

   .. note::

      The old view of the SeshatCommentPart creation is not currently used in
      the application.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: seshatindex(request)

   Render the Seshat landing page.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: seshatindex2(request)

   Return the Seshat landing page.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshatmethods(request)

   Return the Seshat "Methods" page.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshatolddownloads(request)

   Return the Seshat "Downloads" page.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: seshatwhoweare(request)

   Return the Seshat "Who We are" page.

   :param request: The request object.
   :type request: HttpRequest

   :returns: The response object.
   :rtype: HttpResponse


.. py:function:: signup_traditional(request)

   Handle user signup.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: signupfollowup(request)

   Handle user signup follow-up.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: synczotero(request)

   This function is used to sync the Zotero data with the database.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: synczotero100(request)

   This function is used to sync the Zotero data with the database.

   .. note:: This function syncs only 100 references.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: synczoteromanually(request)

   This function is used to manually input the references from the Zotero data
   available in the manual_input_refs.py file into the database.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: update_citations(request)

   This function takes all the references and build a citation for them.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: update_citations_from_inside_zotero_update()

   This function takes all the references and build a citation for them.

   :param None:

   :returns: None


.. py:function:: update_seshat_comment_part_view(request, pk)

   View to update a SeshatCommentPart instance.

   .. note:: This view can handle POST and GET requests.

   :param request: The request object.
   :param pk: The primary key of the SeshatCommentPart instance.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: variablehierarchysetting(request)

   Handle variable hierarchy setting. This is a view for the admin to set the
   variable hierarchy.

   :param request: The request object.

   :returns: The HTTP response.
   :rtype: HttpResponse


.. py:function:: xxyyzz(request, com_id)

.. py:data:: POLITY_RELIGIOUS_TRADITION_CHOICES

.. py:data:: app_map

.. py:data:: categorical_variables

.. py:data:: world_map_initial_displayed_year
   :value: 117


.. py:data:: world_map_initial_polity
   :value: 'it_roman_principate'


