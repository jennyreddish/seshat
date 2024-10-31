seshat.apps.crisisdb.forms
==========================

.. py:module:: seshat.apps.crisisdb.forms


Attributes
----------

.. autoapisummary::

   seshat.apps.crisisdb.forms.commonfields
   seshat.apps.crisisdb.forms.commonlabels
   seshat.apps.crisisdb.forms.commonwidgets


Classes
-------

.. autoapisummary::

   seshat.apps.crisisdb.forms.Agricultural_populationForm
   seshat.apps.crisisdb.forms.Arable_landForm
   seshat.apps.crisisdb.forms.Arable_land_per_farmerForm
   seshat.apps.crisisdb.forms.Crisis_consequenceForm
   seshat.apps.crisisdb.forms.Crop_failure_eventForm
   seshat.apps.crisisdb.forms.Disease_outbreakForm
   seshat.apps.crisisdb.forms.Drought_eventForm
   seshat.apps.crisisdb.forms.External_conflictForm
   seshat.apps.crisisdb.forms.External_conflict_sideForm
   seshat.apps.crisisdb.forms.Famine_eventForm
   seshat.apps.crisisdb.forms.Gdp_per_capitaForm
   seshat.apps.crisisdb.forms.Gross_grain_shared_per_agricultural_populationForm
   seshat.apps.crisisdb.forms.Human_sacrificeForm
   seshat.apps.crisisdb.forms.Internal_conflictForm
   seshat.apps.crisisdb.forms.Locust_eventForm
   seshat.apps.crisisdb.forms.Military_expenseForm
   seshat.apps.crisisdb.forms.Net_grain_shared_per_agricultural_populationForm
   seshat.apps.crisisdb.forms.Power_transitionForm
   seshat.apps.crisisdb.forms.Silver_inflowForm
   seshat.apps.crisisdb.forms.Silver_stockForm
   seshat.apps.crisisdb.forms.Socioeconomic_turmoil_eventForm
   seshat.apps.crisisdb.forms.SurplusForm
   seshat.apps.crisisdb.forms.Total_populationForm
   seshat.apps.crisisdb.forms.Us_locationForm
   seshat.apps.crisisdb.forms.Us_violenceForm
   seshat.apps.crisisdb.forms.Us_violence_data_sourceForm
   seshat.apps.crisisdb.forms.Us_violence_subtypeForm


Module Contents
---------------

.. py:class:: Agricultural_populationForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating an agricultural population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Arable_landForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating an arable land.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Arable_land_per_farmerForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating an arable land per farmer.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Crisis_consequenceForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a crisis consequence.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Crop_failure_eventForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a crop failure event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Disease_outbreakForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a disease outbreak.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Drought_eventForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a drought event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: External_conflictForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating an external conflict.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: External_conflict_sideForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Side form for creating and updating an external conflict.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Famine_eventForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a famine event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Gdp_per_capitaForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a GDP per capita.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Gross_grain_shared_per_agricultural_populationForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a gross grain shared per agricultural population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Human_sacrificeForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a human sacrifice.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Internal_conflictForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating an internal conflict.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Locust_eventForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a locust event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Military_expenseForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a military expense.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Net_grain_shared_per_agricultural_populationForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a net grain shared per agricultural population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Power_transitionForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a power transition.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Silver_inflowForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a silver inflow.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Silver_stockForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a silver stock.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Socioeconomic_turmoil_eventForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a socioeconomic turmoil event.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: SurplusForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a surplus.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Total_populationForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a total population.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields


      .. py:attribute:: labels


      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Us_locationForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a US location.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: '__all__'



      .. py:attribute:: model



.. py:class:: Us_violenceForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a US violence.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: ['violence_date', 'violence_type', 'violence_subtype', 'fatalities', 'location', 'url_address',...



      .. py:attribute:: model


      .. py:attribute:: widgets



.. py:class:: Us_violence_data_sourceForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a US violence data source.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: '__all__'



      .. py:attribute:: model



.. py:class:: Us_violence_subtypeForm(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None)

   Bases: :py:obj:`django.forms.ModelForm`


   Form for creating and updating a US violence subtype.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: fields
         :value: '__all__'



      .. py:attribute:: model



.. py:data:: commonfields
   :value: ['polity', 'year_from', 'year_to', 'description', 'tag', 'is_disputed', 'is_uncertain',...


.. py:data:: commonlabels

.. py:data:: commonwidgets

