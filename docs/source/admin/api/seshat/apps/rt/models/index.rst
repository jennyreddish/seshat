seshat.apps.rt.models
=====================

.. py:module:: seshat.apps.rt.models


Attributes
----------

.. autoapisummary::

   seshat.apps.rt.models.ABSENT_PRESENT_CHOICES
   seshat.apps.rt.models.FREQUENCY_CHOICES
   seshat.apps.rt.models.ORDER_CHOICES
   seshat.apps.rt.models.PREVALENCE_CHOICES


Classes
-------

.. autoapisummary::

   seshat.apps.rt.models.Elites_religion
   seshat.apps.rt.models.Gov_dis_rel_grp_occ_fun
   seshat.apps.rt.models.Gov_obl_rel_grp_ofc_reco
   seshat.apps.rt.models.Gov_press_conv
   seshat.apps.rt.models.Gov_press_conv_for_aga
   seshat.apps.rt.models.Gov_res_cir_rel_lit
   seshat.apps.rt.models.Gov_res_cons_rel_buil
   seshat.apps.rt.models.Gov_res_conv
   seshat.apps.rt.models.Gov_res_prop_own_for_rel_grp
   seshat.apps.rt.models.Gov_res_pub_pros
   seshat.apps.rt.models.Gov_res_pub_wor
   seshat.apps.rt.models.Gov_res_rel_edu
   seshat.apps.rt.models.Gov_vio_freq_rel_grp
   seshat.apps.rt.models.Official_religion
   seshat.apps.rt.models.Religious_fragmentation
   seshat.apps.rt.models.Soc_dis_rel_grp_occ_fun
   seshat.apps.rt.models.Soc_vio_freq_rel_grp
   seshat.apps.rt.models.Sync_rel_pra_ind_beli
   seshat.apps.rt.models.Tax_rel_adh_act_ins
   seshat.apps.rt.models.Theo_sync_dif_rel
   seshat.apps.rt.models.Widespread_religion


Functions
---------

.. autoapisummary::

   seshat.apps.rt.models.call_my_name
   seshat.apps.rt.models.clean_times
   seshat.apps.rt.models.return_citations


Module Contents
---------------

.. py:class:: Elites_religion(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Elites_religion'



      .. py:attribute:: verbose_name_plural
         :value: 'Elites_religions'




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


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_dis_rel_grp_occ_fun(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_dis_rel_grp_occ_fun'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Discrimination Against Religious Groups Taking up Certain Occupations or Functionss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_obl_rel_grp_ofc_reco(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_obl_rel_grp_ofc_reco'



      .. py:attribute:: verbose_name_plural
         :value: 'Governmental Obligations for Religious Groups to Apply for Official Recognitions'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_press_conv(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_press_conv'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Pressure to Converts'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_press_conv_for_aga(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_press_conv_for_aga'



      .. py:attribute:: verbose_name_plural
         :value: 'Societal Pressure to Convert or Against Conversions'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_res_cir_rel_lit(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_res_cir_rel_lit'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Restrictions on Circulation of Religious Literatures'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_res_cons_rel_buil(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_res_cons_rel_buil'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Restrictions on Construction of Religious Buildingss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_res_conv(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_res_conv'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Restrictions on Conversions'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_res_prop_own_for_rel_grp(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_res_prop_own_for_rel_grp'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Restrictions on Property Ownership for Adherents of Any Religious Groups'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_res_pub_pros(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_res_pub_pros'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Restrictions on Public Proselytizings'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_res_pub_wor(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_res_pub_wor'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Restrictions on Public Worships'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_res_rel_edu(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_res_rel_edu'



      .. py:attribute:: verbose_name_plural
         :value: 'Government Restrictions on Religious Educations'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Gov_vio_freq_rel_grp(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gov_vio_freq_rel_grp'



      .. py:attribute:: verbose_name_plural
         :value: 'Frequency of Governmental Violence Against Religious Groupss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Official_religion(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: verbose_name
         :value: 'Official_religion'



      .. py:attribute:: verbose_name_plural
         :value: 'Official_religions'




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


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Religious_fragmentation(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Religious_fragmentation'



      .. py:attribute:: verbose_name_plural
         :value: 'Religious Fragmentations'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Soc_dis_rel_grp_occ_fun(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Soc_dis_rel_grp_occ_fun'



      .. py:attribute:: verbose_name_plural
         :value: 'Societal Discrimination Against Religious Groups Taking up Certain Occupations or Functionss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Soc_vio_freq_rel_grp(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Soc_vio_freq_rel_grp'



      .. py:attribute:: verbose_name_plural
         :value: 'Frequency of Societal Violence Against Religious Groupss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Sync_rel_pra_ind_beli(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Sync_rel_pra_ind_beli'



      .. py:attribute:: verbose_name_plural
         :value: 'Syncretism of Religious Practices at the Level of Individual Believerss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Tax_rel_adh_act_ins(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Tax_rel_adh_act_ins'



      .. py:attribute:: verbose_name_plural
         :value: 'Taxes Based on Religious Adherence or on Religious Activities and Institutionss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Theo_sync_dif_rel(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Theo_sync_dif_rel'



      .. py:attribute:: verbose_name_plural
         :value: 'Theological Syncretism of Different Religionss'




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


   .. py:method:: show_value_from()


   .. py:method:: show_value_to()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: coded_value


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Widespread_religion(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   



   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['order']



      .. py:attribute:: verbose_name
         :value: 'Widespread_religion'



      .. py:attribute:: verbose_name_plural
         :value: 'Widespread_religions'




   .. py:method:: clean_name()

      Return the name of the model instance.

      :noindex:

      .. note::

         TODO This method should probably just be an attribute set on the
         model instead.

      :returns: The name of the model instance.
      :rtype: str



   .. py:method:: clean_name_dynamic()


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


   .. py:attribute:: degree_of_prevalence


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


   .. py:attribute:: order


   .. py:attribute:: widespread_religion


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


.. py:data:: FREQUENCY_CHOICES
   :value: (('never', 'never (absent)'), ('vr', 'very rarely'), ('mftvr', 'more frequently than very...


.. py:data:: ORDER_CHOICES
   :value: (('1', '1. Most widespread'), ('2', '2. Second most widespread'), ('3', '3. Third most...


.. py:data:: PREVALENCE_CHOICES
   :value: (('v_m', 'Vast majority'), ('o_h_p', 'Over half of the population'), ('sz_m', 'Sizeable...


