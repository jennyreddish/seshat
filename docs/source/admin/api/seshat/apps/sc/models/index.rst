seshat.apps.sc.models
=====================

.. py:module:: seshat.apps.sc.models


Attributes
----------

.. autoapisummary::

   seshat.apps.sc.models.ABSENT_PRESENT_CHOICES
   seshat.apps.sc.models.SOURCE_OF_SUPPORT_CHOICES


Classes
-------

.. autoapisummary::

   seshat.apps.sc.models.Administrative_level
   seshat.apps.sc.models.Area_measurement_system
   seshat.apps.sc.models.Article
   seshat.apps.sc.models.Bridge
   seshat.apps.sc.models.Burial_site
   seshat.apps.sc.models.Calendar
   seshat.apps.sc.models.Canal
   seshat.apps.sc.models.Ceremonial_site
   seshat.apps.sc.models.Communal_building
   seshat.apps.sc.models.Courier
   seshat.apps.sc.models.Court
   seshat.apps.sc.models.Debt_and_credit_structure
   seshat.apps.sc.models.Drinking_water_supply_system
   seshat.apps.sc.models.Enclosure
   seshat.apps.sc.models.Entertainment_building
   seshat.apps.sc.models.Examination_system
   seshat.apps.sc.models.Fastest_individual_communication
   seshat.apps.sc.models.Fiction
   seshat.apps.sc.models.Food_storage_site
   seshat.apps.sc.models.Foreign_coin
   seshat.apps.sc.models.Formal_legal_code
   seshat.apps.sc.models.Full_time_bureaucrat
   seshat.apps.sc.models.General_postal_service
   seshat.apps.sc.models.Geometrical_measurement_system
   seshat.apps.sc.models.History
   seshat.apps.sc.models.Indigenous_coin
   seshat.apps.sc.models.Irrigation_system
   seshat.apps.sc.models.Judge
   seshat.apps.sc.models.Knowledge_or_information_building
   seshat.apps.sc.models.Largest_communication_distance
   seshat.apps.sc.models.Length_measurement_system
   seshat.apps.sc.models.Lists_tables_and_classification
   seshat.apps.sc.models.Market
   seshat.apps.sc.models.Merit_promotion
   seshat.apps.sc.models.Military_level
   seshat.apps.sc.models.Mines_or_quarry
   seshat.apps.sc.models.Mnemonic_device
   seshat.apps.sc.models.Non_phonetic_writing
   seshat.apps.sc.models.Nonwritten_record
   seshat.apps.sc.models.Occupational_complexity
   seshat.apps.sc.models.Other_measurement_system
   seshat.apps.sc.models.Other_special_purpose_site
   seshat.apps.sc.models.Other_utilitarian_public_building
   seshat.apps.sc.models.Paper_currency
   seshat.apps.sc.models.Philosophy
   seshat.apps.sc.models.Phonetic_alphabetic_writing
   seshat.apps.sc.models.Polity_population
   seshat.apps.sc.models.Polity_territory
   seshat.apps.sc.models.Population_of_the_largest_settlement
   seshat.apps.sc.models.Port
   seshat.apps.sc.models.Postal_station
   seshat.apps.sc.models.Practical_literature
   seshat.apps.sc.models.Precious_metal
   seshat.apps.sc.models.Professional_lawyer
   seshat.apps.sc.models.Professional_military_officer
   seshat.apps.sc.models.Professional_priesthood
   seshat.apps.sc.models.Professional_soldier
   seshat.apps.sc.models.Ra
   seshat.apps.sc.models.Religious_level
   seshat.apps.sc.models.Religious_literature
   seshat.apps.sc.models.Road
   seshat.apps.sc.models.Sacred_text
   seshat.apps.sc.models.Scientific_literature
   seshat.apps.sc.models.Script
   seshat.apps.sc.models.Settlement_hierarchy
   seshat.apps.sc.models.Source_of_support
   seshat.apps.sc.models.Special_purpose_house
   seshat.apps.sc.models.Special_purpose_site
   seshat.apps.sc.models.Specialized_government_building
   seshat.apps.sc.models.Store_of_wealth
   seshat.apps.sc.models.Symbolic_building
   seshat.apps.sc.models.Time_measurement_system
   seshat.apps.sc.models.Token
   seshat.apps.sc.models.Trading_emporia
   seshat.apps.sc.models.Utilitarian_public_building
   seshat.apps.sc.models.Volume_measurement_system
   seshat.apps.sc.models.Weight_measurement_system
   seshat.apps.sc.models.Written_record


Functions
---------

.. autoapisummary::

   seshat.apps.sc.models.call_my_name
   seshat.apps.sc.models.clean_times
   seshat.apps.sc.models.return_citations


Module Contents
---------------

.. py:class:: Administrative_level(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Administrative_level'



      .. py:attribute:: verbose_name_plural
         :value: 'Administrative_levels'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: administrative_level_from


   .. py:attribute:: administrative_level_to


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Area_measurement_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Area_measurement_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Area_measurement_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: area_measurement_system


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Article(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Article'



      .. py:attribute:: verbose_name_plural
         :value: 'Articles'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: article


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Bridge(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Bridge'



      .. py:attribute:: verbose_name_plural
         :value: 'Bridges'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: bridge


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Burial_site(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Burial_site'



      .. py:attribute:: verbose_name_plural
         :value: 'Burial_sites'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: burial_site


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Calendar(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Calendar'



      .. py:attribute:: verbose_name_plural
         :value: 'Calendars'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: calendar


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Canal(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Canal'



      .. py:attribute:: verbose_name_plural
         :value: 'Canals'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: canal


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Ceremonial_site(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Ceremonial_site'



      .. py:attribute:: verbose_name_plural
         :value: 'Ceremonial_sites'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: ceremonial_site


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Communal_building(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Communal_building'



      .. py:attribute:: verbose_name_plural
         :value: 'Communal_buildings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: communal_building


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Courier(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Courier'



      .. py:attribute:: verbose_name_plural
         :value: 'Couriers'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: courier


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Court(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Court'



      .. py:attribute:: verbose_name_plural
         :value: 'Courts'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: court


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Debt_and_credit_structure(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Debt_and_credit_structure'



      .. py:attribute:: verbose_name_plural
         :value: 'Debt_and_credit_structures'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: debt_and_credit_structure


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Drinking_water_supply_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Drinking_water_supply_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Drinking_water_supply_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: drinking_water_supply_system


   .. py:attribute:: name


.. py:class:: Enclosure(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Enclosure'



      .. py:attribute:: verbose_name_plural
         :value: 'Enclosures'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: enclosure


   .. py:attribute:: name


.. py:class:: Entertainment_building(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Entertainment_building'



      .. py:attribute:: verbose_name_plural
         :value: 'Entertainment_buildings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: entertainment_building


   .. py:attribute:: name


.. py:class:: Examination_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Examination_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Examination_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: examination_system


   .. py:attribute:: name


.. py:class:: Fastest_individual_communication(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Fastest_individual_communication'



      .. py:attribute:: verbose_name_plural
         :value: 'Fastest Individual Communications'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: fastest_individual_communication_from


   .. py:attribute:: fastest_individual_communication_to


   .. py:attribute:: name


.. py:class:: Fiction(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Fiction'



      .. py:attribute:: verbose_name_plural
         :value: 'Fictions'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: fiction


   .. py:attribute:: name


.. py:class:: Food_storage_site(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Food_storage_site'



      .. py:attribute:: verbose_name_plural
         :value: 'Food_storage_sites'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: food_storage_site


   .. py:attribute:: name


.. py:class:: Foreign_coin(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Foreign_coin'



      .. py:attribute:: verbose_name_plural
         :value: 'Foreign_coins'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: foreign_coin


   .. py:attribute:: name


.. py:class:: Formal_legal_code(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Formal_legal_code'



      .. py:attribute:: verbose_name_plural
         :value: 'Formal_legal_codes'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: formal_legal_code


   .. py:attribute:: name


.. py:class:: Full_time_bureaucrat(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Full_time_bureaucrat'



      .. py:attribute:: verbose_name_plural
         :value: 'Full_time_bureaucrats'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: full_time_bureaucrat


   .. py:attribute:: name


.. py:class:: General_postal_service(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'General_postal_service'



      .. py:attribute:: verbose_name_plural
         :value: 'General_postal_services'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: general_postal_service


   .. py:attribute:: name


.. py:class:: Geometrical_measurement_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Geometrical_measurement_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Geometrical_measurement_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: geometrical_measurement_system


   .. py:attribute:: name


.. py:class:: History(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'History'



      .. py:attribute:: verbose_name_plural
         :value: 'Histories'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: history


   .. py:attribute:: name


.. py:class:: Indigenous_coin(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Indigenous_coin'



      .. py:attribute:: verbose_name_plural
         :value: 'Indigenous_coins'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: indigenous_coin


   .. py:attribute:: name


.. py:class:: Irrigation_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Irrigation_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Irrigation_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: irrigation_system


   .. py:attribute:: name


.. py:class:: Judge(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Judge'



      .. py:attribute:: verbose_name_plural
         :value: 'Judges'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: judge


   .. py:attribute:: name


.. py:class:: Knowledge_or_information_building(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Knowledge_or_information_building'



      .. py:attribute:: verbose_name_plural
         :value: 'Knowledge_or_information_buildings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: knowledge_or_information_building


   .. py:attribute:: name


.. py:class:: Largest_communication_distance(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Largest_communication_distance'



      .. py:attribute:: verbose_name_plural
         :value: 'Largest Communication Distances'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: largest_communication_distance_from


   .. py:attribute:: largest_communication_distance_to


   .. py:attribute:: name


.. py:class:: Length_measurement_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Length_measurement_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Length_measurement_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: length_measurement_system


   .. py:attribute:: name


.. py:class:: Lists_tables_and_classification(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Lists_tables_and_classification'



      .. py:attribute:: verbose_name_plural
         :value: 'Lists_tables_and_classifications'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: lists_tables_and_classification


   .. py:attribute:: name


.. py:class:: Market(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Market'



      .. py:attribute:: verbose_name_plural
         :value: 'Markets'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: market


   .. py:attribute:: name


.. py:class:: Merit_promotion(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Merit_promotion'



      .. py:attribute:: verbose_name_plural
         :value: 'Merit_promotions'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: merit_promotion


   .. py:attribute:: name


.. py:class:: Military_level(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Military_level'



      .. py:attribute:: verbose_name_plural
         :value: 'Military_levels'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: military_level_from


   .. py:attribute:: military_level_to


   .. py:attribute:: name


.. py:class:: Mines_or_quarry(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Mines_or_quarry'



      .. py:attribute:: verbose_name_plural
         :value: 'Mines_or_quarries'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: mines_or_quarry


   .. py:attribute:: name


.. py:class:: Mnemonic_device(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Mnemonic_device'



      .. py:attribute:: verbose_name_plural
         :value: 'Mnemonic_devices'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: mnemonic_device


   .. py:attribute:: name


.. py:class:: Non_phonetic_writing(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Non_phonetic_writing'



      .. py:attribute:: verbose_name_plural
         :value: 'Non_phonetic_writings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: non_phonetic_writing


.. py:class:: Nonwritten_record(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Nonwritten_record'



      .. py:attribute:: verbose_name_plural
         :value: 'Nonwritten_records'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: nonwritten_record


.. py:class:: Occupational_complexity(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Occupational_complexity'



      .. py:attribute:: verbose_name_plural
         :value: 'Occupational_complexies'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: occupational_complexity


.. py:class:: Other_measurement_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Other_measurement_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Other_measurement_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: other_measurement_system


.. py:class:: Other_special_purpose_site(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Other_special_purpose_site'



      .. py:attribute:: verbose_name_plural
         :value: 'Other Special Purpose Sites'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: other_special_purpose_site


.. py:class:: Other_utilitarian_public_building(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Other_utilitarian_public_building'



      .. py:attribute:: verbose_name_plural
         :value: 'Other_utilitarian_public_buildings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: other_utilitarian_public_building


.. py:class:: Paper_currency(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Paper_currency'



      .. py:attribute:: verbose_name_plural
         :value: 'Paper_currencies'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: paper_currency


.. py:class:: Philosophy(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Philosophy'



      .. py:attribute:: verbose_name_plural
         :value: 'Philosophies'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: philosophy


.. py:class:: Phonetic_alphabetic_writing(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Phonetic_alphabetic_writing'



      .. py:attribute:: verbose_name_plural
         :value: 'Phonetic_alphabetic_writings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: phonetic_alphabetic_writing


.. py:class:: Polity_population(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_population'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_populations'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: polity_population_from


   .. py:attribute:: polity_population_to


.. py:class:: Polity_territory(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polity_territory'



      .. py:attribute:: verbose_name_plural
         :value: 'Polity_territories'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: polity_territory_from


   .. py:attribute:: polity_territory_to


.. py:class:: Population_of_the_largest_settlement(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Population_of_the_largest_settlement'



      .. py:attribute:: verbose_name_plural
         :value: 'Population_of_the_largest_settlements'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: population_of_the_largest_settlement_from


   .. py:attribute:: population_of_the_largest_settlement_to


.. py:class:: Port(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Port'



      .. py:attribute:: verbose_name_plural
         :value: 'Ports'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: port


.. py:class:: Postal_station(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Postal_station'



      .. py:attribute:: verbose_name_plural
         :value: 'Postal_stations'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: postal_station


.. py:class:: Practical_literature(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Practical_literature'



      .. py:attribute:: verbose_name_plural
         :value: 'Practical_literatures'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: practical_literature


.. py:class:: Precious_metal(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Precious_metal'



      .. py:attribute:: verbose_name_plural
         :value: 'Precious_metals'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: precious_metal


.. py:class:: Professional_lawyer(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Professional_lawyer'



      .. py:attribute:: verbose_name_plural
         :value: 'Professional_lawyers'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: professional_lawyer


.. py:class:: Professional_military_officer(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Professional_military_officer'



      .. py:attribute:: verbose_name_plural
         :value: 'Professional_military_officers'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: professional_military_officer


.. py:class:: Professional_priesthood(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Professional_priesthood'



      .. py:attribute:: verbose_name_plural
         :value: 'Professional_priesthoods'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: professional_priesthood


.. py:class:: Professional_soldier(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Professional_soldier'



      .. py:attribute:: verbose_name_plural
         :value: 'Professional_soldiers'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: professional_soldier


.. py:class:: Ra(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Ra'



      .. py:attribute:: verbose_name_plural
         :value: 'Ras'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: sc_ra


.. py:class:: Religious_level(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Religious_level'



      .. py:attribute:: verbose_name_plural
         :value: 'Religious_levels'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: religious_level_from


   .. py:attribute:: religious_level_to


.. py:class:: Religious_literature(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Religious_literature'



      .. py:attribute:: verbose_name_plural
         :value: 'Religious_literatures'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: religious_literature


.. py:class:: Road(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Road'



      .. py:attribute:: verbose_name_plural
         :value: 'Roads'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: road


.. py:class:: Sacred_text(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Sacred_text'



      .. py:attribute:: verbose_name_plural
         :value: 'Sacred_texts'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: sacred_text


.. py:class:: Scientific_literature(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Scientific_literature'



      .. py:attribute:: verbose_name_plural
         :value: 'Scientific_literatures'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: scientific_literature


.. py:class:: Script(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Script'



      .. py:attribute:: verbose_name_plural
         :value: 'Scripts'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: script


.. py:class:: Settlement_hierarchy(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Settlement_hierarchy'



      .. py:attribute:: verbose_name_plural
         :value: 'Settlement_hierarchies'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: settlement_hierarchy_from


   .. py:attribute:: settlement_hierarchy_to


.. py:class:: Source_of_support(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Source_of_support'



      .. py:attribute:: verbose_name_plural
         :value: 'Source_of_supports'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: source_of_support


.. py:class:: Special_purpose_house(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Special_purpose_house'



      .. py:attribute:: verbose_name_plural
         :value: 'Special Purpose Houses'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: special_purpose_house


.. py:class:: Special_purpose_site(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Special_purpose_site'



      .. py:attribute:: verbose_name_plural
         :value: 'Special_purpose_sites'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: special_purpose_site


.. py:class:: Specialized_government_building(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Specialized_government_building'



      .. py:attribute:: verbose_name_plural
         :value: 'Specialized_government_buildings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: specialized_government_building


.. py:class:: Store_of_wealth(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Store_of_wealth'



      .. py:attribute:: verbose_name_plural
         :value: 'Store_of_wealths'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: store_of_wealth


.. py:class:: Symbolic_building(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Symbolic_building'



      .. py:attribute:: verbose_name_plural
         :value: 'Symbolic_buildings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: symbolic_building


.. py:class:: Time_measurement_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Time_measurement_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Time_measurement_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: time_measurement_system


.. py:class:: Token(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Token'



      .. py:attribute:: verbose_name_plural
         :value: 'Tokens'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: token


.. py:class:: Trading_emporia(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Trading_emporia'



      .. py:attribute:: verbose_name_plural
         :value: 'Trading_emporias'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: trading_emporia


.. py:class:: Utilitarian_public_building(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Utilitarian_public_building'



      .. py:attribute:: verbose_name_plural
         :value: 'Utilitarian_public_buildings'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: utilitarian_public_building


.. py:class:: Volume_measurement_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Volume_measurement_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Volume_measurement_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: volume_measurement_system


.. py:class:: Weight_measurement_system(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Weight_measurement_system'



      .. py:attribute:: verbose_name_plural
         :value: 'Weight_measurement_systems'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: weight_measurement_system


.. py:class:: Written_record(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Written_record'



      .. py:attribute:: verbose_name_plural
         :value: 'Written_records'




   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: written_record


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


.. py:data:: ABSENT_PRESENT_CHOICES
   :value: (('present', 'present'), ('absent', 'absent'), ('unknown', 'unknown'), ('A~P', 'Transitional...


.. py:data:: SOURCE_OF_SUPPORT_CHOICES
   :value: (('state salary', 'state salary'), ('pensions', 'pensions'), ('enoblement', 'enoblement'),...


