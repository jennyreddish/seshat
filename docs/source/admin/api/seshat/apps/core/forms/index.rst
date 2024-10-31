seshat.apps.core.forms
======================

.. py:module:: seshat.apps.core.forms


Attributes
----------

.. autoapisummary::

   seshat.apps.core.forms.CommentPartFormSet
   seshat.apps.core.forms.ReferenceFormSet10
   seshat.apps.core.forms.ReferenceFormSet2
   seshat.apps.core.forms.ReferenceFormSet2_UPGRADE
   seshat.apps.core.forms.ReferenceFormSet5


Classes
-------

.. autoapisummary::

   seshat.apps.core.forms.BaseReferenceFormSet
   seshat.apps.core.forms.CapitalForm
   seshat.apps.core.forms.CitationForm
   seshat.apps.core.forms.NgaForm
   seshat.apps.core.forms.PolityForm
   seshat.apps.core.forms.PolityUpdateForm
   seshat.apps.core.forms.ReferenceForm
   seshat.apps.core.forms.ReferenceWithPageForm
   seshat.apps.core.forms.ReferenceWithPageForm_UPGRADE
   seshat.apps.core.forms.ReligionForm
   seshat.apps.core.forms.SeshatCommentForm
   seshat.apps.core.forms.SeshatCommentForm2
   seshat.apps.core.forms.SeshatCommentPartForm
   seshat.apps.core.forms.SeshatCommentPartForm10
   seshat.apps.core.forms.SeshatCommentPartForm2
   seshat.apps.core.forms.SeshatCommentPartForm2_UPGRADE
   seshat.apps.core.forms.SeshatCommentPartForm5
   seshat.apps.core.forms.SeshatPrivateCommentForm
   seshat.apps.core.forms.SeshatPrivateCommentPartForm
   seshat.apps.core.forms.SignUpForm
   seshat.apps.core.forms.VariablehierarchyFormNew


Module Contents
---------------

.. py:class:: BaseReferenceFormSet(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, form_kwargs=None, error_messages=None)

   Bases: :py:obj:`django.forms.formsets.BaseFormSet`


   Base formset for adding or updating multiple references to a comment.


   .. py:method:: add_fields(form, index)

      Add fields to the form.

      :param form: The form to add fields to.
      :type form: Form
      :param index: The index of the form.
      :type index: int

      :returns: None



.. py:class:: CapitalForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new capital in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('name', 'latitude', 'longitude', 'current_country', 'alternative_names', 'is_verified',...



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: CitationForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new citation in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('ref', 'page_from', 'page_to')



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



   .. py:method:: clean()

      Check if the citation is a duplicate.

      :returns: The cleaned data.
      :rtype: dict

      :raises ValidationError: If the citation is a duplicate.



.. py:class:: NgaForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new NGA in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('name', 'world_region', 'subregion', 'fao_country')



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: PolityForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new polity in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('name', 'new_name', 'long_name', 'start_year', 'end_year', 'home_seshat_region', 'polity_tag',...



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: PolityUpdateForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating an existing polity in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('name', 'new_name', 'long_name', 'start_year', 'end_year', 'home_seshat_region', 'polity_tag',...



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: ReferenceForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new reference in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('title', 'year', 'creator', 'zotero_link', 'long_name')



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: ReferenceWithPageForm(*args, **kwargs)

   Bases: :py:obj:`django.forms.Form`


   Form for adding or updating a new reference with page numbers in the database.


   .. py:attribute:: page_from


   .. py:attribute:: page_to


   .. py:attribute:: parent_pars


   .. py:attribute:: ref


.. py:class:: ReferenceWithPageForm_UPGRADE(*args, **kwargs)

   Bases: :py:obj:`django.forms.Form`


   A collection of Fields, plus their associated data.


   .. py:attribute:: page_from


   .. py:attribute:: page_to


   .. py:attribute:: parent_pars


   .. py:attribute:: ref


.. py:class:: ReligionForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new religion in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ['religion_name']



      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: SeshatCommentForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new comment in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('text',)



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: SeshatCommentForm2(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.Form`


   A collection of Fields, plus their associated data.


   .. py:attribute:: formset


.. py:class:: SeshatCommentPartForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new comment part in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('comment', 'comment_part_text', 'comment_citations', 'comment_order', 'comment_curator')



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: SeshatCommentPartForm10(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.Form`


   A collection of Fields, plus their associated data.


   .. py:attribute:: comment_order


   .. py:attribute:: comment_text


   .. py:attribute:: formset


.. py:class:: SeshatCommentPartForm2(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.Form`


   A collection of Fields, plus their associated data.


   .. py:attribute:: comment_order


   .. py:attribute:: comment_text


   .. py:attribute:: formset


.. py:class:: SeshatCommentPartForm2_UPGRADE(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.Form`


   A collection of Fields, plus their associated data.


   .. py:attribute:: comment_order


   .. py:attribute:: comment_text


   .. py:attribute:: references_formset


.. py:class:: SeshatCommentPartForm5(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.Form`


   A collection of Fields, plus their associated data.


   .. py:attribute:: comment_order


   .. py:attribute:: comment_text


   .. py:attribute:: formset


.. py:class:: SeshatPrivateCommentForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new private comment in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('text',)



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: SeshatPrivateCommentPartForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for adding or updating a new private comment part in the database.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('private_comment', 'private_comment_part_text', 'private_comment_owner', 'private_comment_reader')



      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: SignUpForm(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.forms.UserCreationForm`


   A form that creates a user, with no privileges, from the given username and
   password.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'captcha')



      .. py:attribute:: model


      .. py:attribute:: widgets



   .. py:method:: clean_email()


   .. py:attribute:: captcha


   .. py:attribute:: password1


   .. py:attribute:: password2


.. py:class:: VariablehierarchyFormNew(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.Form`


   A collection of Fields, plus their associated data.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: unique_together
         :value: ('variable_name', 'section_name', 'subsection_name')




   .. py:attribute:: is_verified


   .. py:attribute:: my_vars


   .. py:attribute:: my_vars_tuple
      :value: [('', ' -- Select Variable -- ')]



   .. py:attribute:: section_name


   .. py:attribute:: subsection_name


   .. py:attribute:: variable_name


.. py:data:: CommentPartFormSet

.. py:data:: ReferenceFormSet10

.. py:data:: ReferenceFormSet2

.. py:data:: ReferenceFormSet2_UPGRADE

.. py:data:: ReferenceFormSet5

