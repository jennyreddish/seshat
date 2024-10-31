seshat.apps.general.models
==========================

.. py:module:: seshat.apps.general.models


Attributes
----------

.. autoapisummary::

   seshat.apps.general.models.POLITY_ALTERNATE_RELIGION_CHOICES
   seshat.apps.general.models.POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES
   seshat.apps.general.models.POLITY_ALTERNATE_RELIGION_GENUS_CHOICES
   seshat.apps.general.models.POLITY_CONSECUTIVE_ENTITY_CHOICES
   seshat.apps.general.models.POLITY_DEGREE_OF_CENTRALIZATION_CHOICES
   seshat.apps.general.models.POLITY_LANGUAGE_CHOICES
   seshat.apps.general.models.POLITY_LANGUAGE_GENUS_CHOICES
   seshat.apps.general.models.POLITY_LINGUISTIC_FAMILY_CHOICES
   seshat.apps.general.models.POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES
   seshat.apps.general.models.POLITY_RELIGION_CHOICES
   seshat.apps.general.models.POLITY_RELIGION_FAMILY_CHOICES
   seshat.apps.general.models.POLITY_RELIGION_GENUS_CHOICES
   seshat.apps.general.models.POLITY_SUPRAPOLITY_RELATIONS_CHOICES


Classes
-------

.. autoapisummary::

   seshat.apps.general.models.Polity_alternate_religion
   seshat.apps.general.models.Polity_alternate_religion_family
   seshat.apps.general.models.Polity_alternate_religion_genus
   seshat.apps.general.models.Polity_alternative_name
   seshat.apps.general.models.Polity_capital
   seshat.apps.general.models.Polity_degree_of_centralization
   seshat.apps.general.models.Polity_duration
   seshat.apps.general.models.Polity_editor
   seshat.apps.general.models.Polity_expert
   seshat.apps.general.models.Polity_language
   seshat.apps.general.models.Polity_language_genus
   seshat.apps.general.models.Polity_linguistic_family
   seshat.apps.general.models.Polity_original_name
   seshat.apps.general.models.Polity_peak_years
   seshat.apps.general.models.Polity_preceding_entity
   seshat.apps.general.models.Polity_relationship_to_preceding_entity
   seshat.apps.general.models.Polity_religion
   seshat.apps.general.models.Polity_religion_family
   seshat.apps.general.models.Polity_religion_genus
   seshat.apps.general.models.Polity_religious_tradition
   seshat.apps.general.models.Polity_research_assistant
   seshat.apps.general.models.Polity_scale_of_supracultural_interaction
   seshat.apps.general.models.Polity_succeeding_entity
   seshat.apps.general.models.Polity_supracultural_entity
   seshat.apps.general.models.Polity_suprapolity_relations
   seshat.apps.general.models.Polity_utm_zone


Functions
---------

.. autoapisummary::

   seshat.apps.general.models.call_my_name
   seshat.apps.general.models.clean_times
   seshat.apps.general.models.return_citations


Module Contents
---------------

.. py:class:: Polity_alternate_religion(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the alternate religion of
   the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_alternate_religion'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_alternate_religions'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the alternate religion of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The alternate religion of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:attribute:: alternate_religion


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Polity_alternate_religion_family(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the alternate religion family
   of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_alternate_religion_family'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_alternate_religion_families'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the alternate religion family of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The alternate religion family of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:attribute:: alternate_religion_family


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Polity_alternate_religion_genus(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the alternate religion genus
   of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_alternate_religion_genus'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_alternate_religion_genus'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the alternate religion genus of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The alternate religion genus of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:attribute:: alternate_religion_genus


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Polity_alternative_name(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the alternative names of
   the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_alternative_name'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_alternative_names'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the alternative name (if it exists, otherwise return a dash).

      :returns: The alternative name (or " - " if it does not exist).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:attribute:: alternative_name


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Polity_capital(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the capitals of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_capital'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_capitals'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the capital of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The capital of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:attribute:: capital


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: polity_cap


.. py:class:: Polity_degree_of_centralization(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the degree of
   centralization of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_degree_of_centralization'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_degree_of_centralizations'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the degree of centralisation of the polity (if it exists on the
      instance, otherwise return a dash).

      :returns: The degree of centralisation of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:attribute:: degree_of_centralization


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Polity_duration(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the duration of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_duration'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_durations'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the duration of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The duration of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: polity_year_from


   .. py:attribute:: polity_year_to


.. py:class:: Polity_editor(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the editors of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_editor'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_editors'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the editor of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The editor of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: editor


   .. py:attribute:: name


.. py:class:: Polity_expert(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the experts of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_expert'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_experts'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the expert of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The expert of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: expert


   .. py:attribute:: name


.. py:class:: Polity_language(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the languages of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_language'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_languages'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the language of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The language of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: language


   .. py:attribute:: name


.. py:class:: Polity_language_genus(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the language genus of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_language_genus'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_language_genus'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the language genus of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The language genus of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: language_genus


   .. py:attribute:: name


.. py:class:: Polity_linguistic_family(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the linguistic family
   of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_linguistic_family'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_linguistic_families'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the linguistic family of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The linguistic family of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: linguistic_family


   .. py:attribute:: name


.. py:class:: Polity_original_name(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the original names of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_original_name'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_original_names'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the original name (if it exists, otherwise return a dash).

      :returns: The original name (or " - " if it does not exist).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: original_name


.. py:class:: Polity_peak_years(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the peak years of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_peak_years'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_peak_years'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the peak years of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The peak years of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: peak_year_from


   .. py:attribute:: peak_year_to


.. py:class:: Polity_preceding_entity(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the preceding entities of
   the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_preceding_entity'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_preceding_entities'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: display_value()

      Depending on the instance, return a HTML string with information about
      the instance's other_polity attribute and its relationship to its
      preceding entity, the preceding entity (if it exists) or a dash if the
      preceding entity does not exist on the instance.

      :returns: A string representation of the instance's other_polity/preceding entity relationship or a dash if the preceding entity does not exist on the instance.
      :rtype: str



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the polity's preceding entity, its long name, and its new name
      (if it exists on the instance, otherwise, if there's a preceding entity,
      return its name, otherwise return a dash).

      :returns: A string representation of polity's preceding entity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: merged_old_data


   .. py:attribute:: name


   .. py:attribute:: other_polity


   .. py:attribute:: preceding_entity


   .. py:attribute:: relationship_to_preceding_entity


.. py:class:: Polity_relationship_to_preceding_entity(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the relationship of the
   polities to their preceding entities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_relationship_to_preceding_entity'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_relationship_to_preceding_entities'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the polity's relationship to the preceding entity (if it exists
      on the instance, otherwise return a dash).

      :returns: The polity's relationship to the preceding entity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: relationship_to_preceding_entity


.. py:class:: Polity_religion(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the religion of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_religion'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_religions'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the religion of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The religion of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: religion


.. py:class:: Polity_religion_family(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the religion family of the


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_religion_family'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_religion_families'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the religion family of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The religion family of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: religion_family


.. py:class:: Polity_religion_genus(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the religion genus of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_religion_genus'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_religion_genus'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the religion genus of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The religion genus of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: religion_genus


.. py:class:: Polity_religious_tradition(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the religious tradition of
   the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_religious_tradition'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_religious_traditions'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the religious tradition of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The religious tradition of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: religious_tradition


.. py:class:: Polity_research_assistant(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the research assistants
   of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['polity_ra', 'year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_research_assistant'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_research_assistants'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the name of the research assistant (if it exists, otherwise
      return a dash).

      :returns: The name of the research assistant (or " - " if it does not exist).
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: polity_ra


.. py:class:: Polity_scale_of_supracultural_interaction(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the scale of supracultural
   interaction of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_scale_of_supracultural_interaction'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_scale_of_supracultural_interactions'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the polity's scale of supracultural interaction (if it exists
      on the instance, otherwise return a dash).

      :returns: The supracultural interaction of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: scale_from


   .. py:attribute:: scale_to


.. py:class:: Polity_succeeding_entity(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the succeeding entities of
   the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_succeeding_entity'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_succeeding_entities'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the succeeding entity of the polity (if it exists on the
      instance, otherwise return a dash).

      :returns: The succeeding entity of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: succeeding_entity


.. py:class:: Polity_supracultural_entity(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the supracultural entity of
   the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_supracultural_entity'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_supracultural_entities'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the supracultural entity of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The supracultural entity of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: supracultural_entity


.. py:class:: Polity_suprapolity_relations(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the supra-polity
   relations of the polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_suprapolity_relations'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_suprapolity_relations'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: display_value()


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the supra polity relations of the polity (if it exists on the
      instance, otherwise return a dash).

      :returns: The supra polity relations of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: other_polity


   .. py:attribute:: supra_polity_relations


.. py:class:: Polity_utm_zone(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   This model is used to store the information about the UTM zone of the
   polities.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_utm_zone'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_utm_zones'




   .. py:method:: clean()

      Validate the year_from and year_to fields of the model instance.

      :noindex:

      .. note:: The method an alias for the clean_times function.

      :returns: None

      :raises ValidationError: If the year_from is greater than the year_to.
      :raises ValidationError: If the year_from is out of range.
      :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
      :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
      :raises ValidationError: If the year_to is out of range.



   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_spaced()

      Return the name of the model instance with spaces.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_value()

      Return the UTM zone of the polity (if it exists on the instance,
      otherwise return a dash).

      :returns: The UTM zone of the polity (or " - " if it does not exist on the instance).
      :rtype: str



   .. py:method:: sub_subsection()

      Return the subsection's subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: None



   .. py:method:: subsection()

      Return the subsection of the model instance.

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The subsection of the model instance.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: utm_zone


.. py:function:: call_my_name(self)

   This function is used to return the name of the model instance (in lieu of
   the __str__ representation of the model instance).

   .. note::

      The model instance must have the following attributes:
      - name
      - polity (and polity.name)
      - year_from
      - year_to

   :param self: The model instance.
   :type self: model instance

   :returns: The name of the model instance.
   :rtype: str


.. py:function:: clean_times(self)

   This function is used to validate the year_from and year_to fields of the
   model instance (called from each model's clean method).

   .. note::

      The model instance must have the following attributes:
      - year_from
      - year_to
      - polity (and polity.start_year and polity.end_year)

   :param self: The model instance.
   :type self: model instance

   :returns: None

   :raises ValidationError: If the year_from is greater than the year_to.
   :raises ValidationError: If the year_from is out of range.
   :raises ValidationError: If the year_from is earlier than the start year of the corresponding polity.
   :raises ValidationError: If the year_to is later than the end year of the corresponding polity.
   :raises ValidationError: If the year_to is out of range.


.. py:function:: return_citations(self)

   This function is used to return the citations of the model instance
   (returning the value used in the display_citations method of the model
   instance).

   .. note::

      The model instance must have the following attribute:
      - citations
      
      The model instance must have the following methods:
      - zoteroer

   :param self: The model instance.
   :type self: model instance

   :returns: The citations of the model instance, separated by comma.
   :rtype: str


.. py:data:: POLITY_ALTERNATE_RELIGION_CHOICES

.. py:data:: POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES

.. py:data:: POLITY_ALTERNATE_RELIGION_GENUS_CHOICES

.. py:data:: POLITY_CONSECUTIVE_ENTITY_CHOICES
   :value: (('continuity', 'continuity'), ('elite migration', 'elite migration'), ('cultural assimilation',...


.. py:data:: POLITY_DEGREE_OF_CENTRALIZATION_CHOICES
   :value: (('loose', 'loose'), ('confederated state', 'confederated state'), ('unitary state', 'unitary...


.. py:data:: POLITY_LANGUAGE_CHOICES
   :value: (('Polish', 'Polish'), ('Pashto', 'Pashto'), ('Persian', 'Persian'), ('Greek', 'Greek'),...


.. py:data:: POLITY_LANGUAGE_GENUS_CHOICES
   :value: (('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'), ('Afro-Asiatic', 'Afro-Asiatic'), ('Indo-European',...


.. py:data:: POLITY_LINGUISTIC_FAMILY_CHOICES
   :value: (('Indo-European', 'Indo-European'), ('Sino-Tibetan', 'Sino-Tibetan'), ('NO_VALUE_ON_WIKI',...


.. py:data:: POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES
   :value: (('continuity', 'continuity'), ('elite migration', 'elite migration'), ('cultural assimilation',...


.. py:data:: POLITY_RELIGION_CHOICES
   :value: (('Islam', 'Islam'), ('Shadhil', 'Shadhil'), ('Karrami', 'Karrami'), ('Hanafi', 'Hanafi'),...


.. py:data:: POLITY_RELIGION_FAMILY_CHOICES
   :value: (('Saivist Traditions', 'Saivist Traditions'), ('Assyrian Religions', 'Assyrian Religions'),...


.. py:data:: POLITY_RELIGION_GENUS_CHOICES
   :value: (('Zoroastrianism', 'Zoroastrianism'), ('Graeco-Bactrian Religions', 'Graeco-Bactrian...


.. py:data:: POLITY_SUPRAPOLITY_RELATIONS_CHOICES
   :value: (('vassalage', 'vassalage to'), ('alliance', 'alliance with'), ('nominal allegiance', 'nominal...


