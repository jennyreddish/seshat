seshat.apps.crisisdb.models
===========================

.. py:module:: seshat.apps.crisisdb.models


Attributes
----------

.. autoapisummary::

   seshat.apps.crisisdb.models.ATTENTION_TAGS_CHOICES
   seshat.apps.crisisdb.models.CRISIS_CONSEQUENCE_CHOICES
   seshat.apps.crisisdb.models.DURATION_DISEASE_OUTBREAK_CHOICES
   seshat.apps.crisisdb.models.HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES
   seshat.apps.crisisdb.models.MAGNITUDE_DISEASE_OUTBREAK_CHOICES
   seshat.apps.crisisdb.models.SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES
   seshat.apps.crisisdb.models.US_STATE_CHOICES
   seshat.apps.crisisdb.models.VIOLENCE_TYPE_CHOICES


Classes
-------

.. autoapisummary::

   seshat.apps.crisisdb.models.Agricultural_population
   seshat.apps.crisisdb.models.Arable_land
   seshat.apps.crisisdb.models.Arable_land_per_farmer
   seshat.apps.crisisdb.models.Crisis_consequence
   seshat.apps.crisisdb.models.Crop_failure_event
   seshat.apps.crisisdb.models.Disease_outbreak
   seshat.apps.crisisdb.models.Drought_event
   seshat.apps.crisisdb.models.External_conflict
   seshat.apps.crisisdb.models.External_conflict_side
   seshat.apps.crisisdb.models.Famine_event
   seshat.apps.crisisdb.models.Gdp_per_capita
   seshat.apps.crisisdb.models.Gross_grain_shared_per_agricultural_population
   seshat.apps.crisisdb.models.Human_sacrifice
   seshat.apps.crisisdb.models.Internal_conflict
   seshat.apps.crisisdb.models.Locust_event
   seshat.apps.crisisdb.models.Military_expense
   seshat.apps.crisisdb.models.Net_grain_shared_per_agricultural_population
   seshat.apps.crisisdb.models.Power_transition
   seshat.apps.crisisdb.models.Silver_inflow
   seshat.apps.crisisdb.models.Silver_stock
   seshat.apps.crisisdb.models.Socioeconomic_turmoil_event
   seshat.apps.crisisdb.models.Surplus
   seshat.apps.crisisdb.models.Total_population
   seshat.apps.crisisdb.models.Us_location
   seshat.apps.crisisdb.models.Us_violence
   seshat.apps.crisisdb.models.Us_violence_data_source
   seshat.apps.crisisdb.models.Us_violence_subtype


Functions
---------

.. autoapisummary::

   seshat.apps.crisisdb.models.call_my_name
   seshat.apps.crisisdb.models.clean_times
   seshat.apps.crisisdb.models.clean_times_light
   seshat.apps.crisisdb.models.has_a_polity
   seshat.apps.crisisdb.models.return_beautiful_abs_pres
   seshat.apps.crisisdb.models.return_citations


Module Contents
---------------

.. py:class:: Agricultural_population(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing an agricultural population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Agricultural_population'



      .. py:attribute:: verbose_name_plural
         :value: 'Agricultural_populations'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: agricultural_population


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Arable_land(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing an arable land.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Arable_land'



      .. py:attribute:: verbose_name_plural
         :value: 'Arable_lands'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: arable_land


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Arable_land_per_farmer(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing an arable land per farmer.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Arable_land_per_farmer'



      .. py:attribute:: verbose_name_plural
         :value: 'Arable_land_per_farmers'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: arable_land_per_farmer


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Crisis_consequence(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a crisis consequence.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Crisis consequence'



      .. py:attribute:: verbose_name_plural
         :value: 'Crisis consequences'




   .. py:method:: clean()

      




   .. py:method:: clean_collapse()


   .. py:method:: clean_decline()


   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: get_columns_with_value(value)

      Return the columns with a given value.

      :noindex:

      :param value: The value to search for.
      :type value: str

      :returns:

                A list of columns with the given value. If no columns have
                    the given value, the method returns None.
      :rtype: list



   .. py:method:: get_columns_with_value_dic(value)


   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:attribute:: assassination


   .. py:attribute:: capital


   .. py:attribute:: century_plus


   .. py:attribute:: civil_war


   .. py:attribute:: collapse


   .. py:attribute:: conquest


   .. py:attribute:: constitution


   .. py:attribute:: crisis_case_id


   .. py:attribute:: decline


   .. py:attribute:: depose


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: downward_mobility


   .. py:attribute:: epidemic


   .. py:attribute:: extermination


   .. py:attribute:: fragmentation


   .. py:attribute:: is_first_100


   .. py:attribute:: labor


   .. py:attribute:: name


   .. py:attribute:: other_polity


   .. py:attribute:: public_goods


   .. py:attribute:: religion


   .. py:attribute:: revolution


   .. py:attribute:: successful_revolution


   .. py:attribute:: suffrage


   .. py:attribute:: unfree_labor


   .. py:attribute:: uprising


.. py:class:: Crop_failure_event(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a crop failure event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Crop_failure_event'



      .. py:attribute:: verbose_name_plural
         :value: 'Crop_failure_events'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: crop_failure_event


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Disease_outbreak(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a disease outbreak.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Disease_outbreak'



      .. py:attribute:: verbose_name_plural
         :value: 'Disease_outbreaks'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: duration


   .. py:attribute:: elevation


   .. py:attribute:: latitude


   .. py:attribute:: longitude


   .. py:attribute:: magnitude


   .. py:attribute:: name


   .. py:attribute:: sub_category


.. py:class:: Drought_event(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a drought event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Drought_event'



      .. py:attribute:: verbose_name_plural
         :value: 'Drought_events'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: drought_event


   .. py:attribute:: name


.. py:class:: External_conflict(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing an external conflict.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'External_conflict'



      .. py:attribute:: verbose_name_plural
         :value: 'External_conflicts'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: conflict_name


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: External_conflict_side(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing an external conflict side.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'External_conflict_side'



      .. py:attribute:: verbose_name_plural
         :value: 'External_conflict_sides'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: casualty


   .. py:attribute:: conflict_id


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: expenditure


   .. py:attribute:: leader


   .. py:attribute:: name


.. py:class:: Famine_event(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a famine event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Famine_event'



      .. py:attribute:: verbose_name_plural
         :value: 'Famine_events'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: famine_event


   .. py:attribute:: name


.. py:class:: Gdp_per_capita(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a GDP value per capita.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Gdp_per_capita'



      .. py:attribute:: verbose_name_plural
         :value: 'Gdp_per_capitas'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: gdp_per_capita


   .. py:attribute:: name


.. py:class:: Gross_grain_shared_per_agricultural_population(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a gross grain shared per agricultural population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Gross_grain_shared_per_agricultural_population'



      .. py:attribute:: verbose_name_plural
         :value: 'Gross_grain_shared_per_agricultural_populations'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: gross_grain_shared_per_agricultural_population


   .. py:attribute:: name


.. py:class:: Human_sacrifice(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a human sacrifice.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Human_sacrifice'



      .. py:attribute:: verbose_name_plural
         :value: 'Human_sacrifices'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: human_sacrifice


   .. py:attribute:: name


.. py:class:: Internal_conflict(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing an internal conflict.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Internal_conflict'



      .. py:attribute:: verbose_name_plural
         :value: 'Internal_conflicts'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: casualty


   .. py:attribute:: conflict


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: expenditure


   .. py:attribute:: leader


   .. py:attribute:: name


.. py:class:: Locust_event(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a locust event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Locust_event'



      .. py:attribute:: verbose_name_plural
         :value: 'Locust_events'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: locust_event


   .. py:attribute:: name


.. py:class:: Military_expense(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a military expense.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Military_expense'



      .. py:attribute:: verbose_name_plural
         :value: 'Military_expenses'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: conflict


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: expenditure


   .. py:attribute:: name


.. py:class:: Net_grain_shared_per_agricultural_population(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a net grain shared per agricultural population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Net_grain_shared_per_agricultural_population'



      .. py:attribute:: verbose_name_plural
         :value: 'Net_grain_shared_per_agricultural_populations'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
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


   .. py:attribute:: net_grain_shared_per_agricultural_population


.. py:class:: Power_transition(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a power transition.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Power Transition'



      .. py:attribute:: verbose_name_plural
         :value: 'Power Transitions'




   .. py:method:: clean()

      




   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: get_columns_with_value(value)

      Return the columns with a given value.

      :noindex:

      :param value: The value to search for.
      :type value: str

      :returns:

                A list of columns with the given value. If no columns have
                    the given value, the method returns None.
      :rtype: list



   .. py:method:: get_columns_with_value_dic(value)


   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:attribute:: contested


   .. py:attribute:: culture_group


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: external_interference


   .. py:attribute:: external_invasion


   .. py:attribute:: intra_elite


   .. py:attribute:: military_revolt


   .. py:attribute:: name


   .. py:attribute:: overturn


   .. py:attribute:: popular_uprising


   .. py:attribute:: predecessor


   .. py:attribute:: predecessor_assassination


   .. py:attribute:: reign_number_predecessor


   .. py:attribute:: separatist_rebellion


   .. py:attribute:: successor


.. py:class:: Silver_inflow(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a silver inflow.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Silver_inflow'



      .. py:attribute:: verbose_name_plural
         :value: 'Silver_inflows'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
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


   .. py:attribute:: silver_inflow


.. py:class:: Silver_stock(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a silver stock.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Silver_stock'



      .. py:attribute:: verbose_name_plural
         :value: 'Silver_stocks'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
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


   .. py:attribute:: silver_stock


.. py:class:: Socioeconomic_turmoil_event(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a socioeconomic turmoil event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Socioeconomic_turmoil_event'



      .. py:attribute:: verbose_name_plural
         :value: 'Socioeconomic_turmoil_events'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
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


   .. py:attribute:: socioeconomic_turmoil_event


.. py:class:: Surplus(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a surplus.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Surplus'



      .. py:attribute:: verbose_name_plural
         :value: 'Surplus'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
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


   .. py:attribute:: surplus


.. py:class:: Total_population(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a total population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Total_population'



      .. py:attribute:: verbose_name_plural
         :value: 'Total_populations'




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



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
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


   .. py:attribute:: total_population


.. py:class:: Us_location(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model representing a location in the US.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['us_state', '-city', '-county', '-special_place']




   .. py:attribute:: attention_tag


   .. py:attribute:: city


   .. py:attribute:: county


   .. py:attribute:: special_place


   .. py:attribute:: us_state


.. py:class:: Us_violence(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model representing a violence event in the US.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['-violence_date', '-fatalities']




   .. py:method:: show_locations()


   .. py:method:: show_narrative_without_quotes()


   .. py:method:: show_short_data_sources()


   .. py:method:: show_source_details_without_quotes()


   .. py:method:: show_violence_subtypes()


   .. py:attribute:: fatalities


   .. py:attribute:: location


   .. py:attribute:: narrative


   .. py:attribute:: short_data_source


   .. py:attribute:: source_details


   .. py:attribute:: url_address


   .. py:attribute:: violence_date


   .. py:attribute:: violence_subtype


   .. py:attribute:: violence_type


.. py:class:: Us_violence_data_source(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model representing a data source for violence in the US.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['name']




   .. py:attribute:: abbreviation


   .. py:attribute:: attention_tag


   .. py:attribute:: is_uncertain


   .. py:attribute:: name


   .. py:attribute:: url_address


.. py:class:: Us_violence_subtype(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model representing a subtype of violence in the US.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['name']




   .. py:attribute:: is_uncertain


   .. py:attribute:: name


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


.. py:function:: clean_times_light(self)

.. py:function:: has_a_polity(self)

.. py:function:: return_beautiful_abs_pres(item)

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


.. py:data:: ATTENTION_TAGS_CHOICES
   :value: (('NeedsExpertInput', 'Needs Expert Input'), ('IsInconsistent', 'Is Inconsistent'), ('IsWrong',...


.. py:data:: CRISIS_CONSEQUENCE_CHOICES
   :value: (('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP',...


.. py:data:: DURATION_DISEASE_OUTBREAK_CHOICES
   :value: (('No description', 'No description'), ('Over 90 Days', 'Over 90 Days'), ('Uncertain',...


.. py:data:: HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES
   :value: (('U', 'Unknown'), ('P', 'Present'), ('A~P', 'Transitional (Absent -> Present)'), ('A',...


.. py:data:: MAGNITUDE_DISEASE_OUTBREAK_CHOICES
   :value: (('Uncertain', 'Uncertain'), ('Light', 'Light'), ('Heavy', 'Heavy'), ('No description', 'No...


.. py:data:: SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES
   :value: (('Peculiar Epidemics', 'Peculiar Epidemics'), ('Pestilence', 'Pestilence'), ('Miasm', 'Miasm'),...


.. py:data:: US_STATE_CHOICES
   :value: (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA',...


.. py:data:: VIOLENCE_TYPE_CHOICES
   :value: (('lynching', 'lynching'), ('riot', 'riot'), ('executions', 'executions'), ('war', 'war'),...


