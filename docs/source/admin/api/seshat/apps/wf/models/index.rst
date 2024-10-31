seshat.apps.wf.models
=====================

.. py:module:: seshat.apps.wf.models


Attributes
----------

.. autoapisummary::

   seshat.apps.wf.models.ABSENT_PRESENT_CHOICES


Classes
-------

.. autoapisummary::

   seshat.apps.wf.models.Atlatl
   seshat.apps.wf.models.Battle_axe
   seshat.apps.wf.models.Breastplate
   seshat.apps.wf.models.Bronze
   seshat.apps.wf.models.Camel
   seshat.apps.wf.models.Chainmail
   seshat.apps.wf.models.Complex_fortification
   seshat.apps.wf.models.Composite_bow
   seshat.apps.wf.models.Copper
   seshat.apps.wf.models.Crossbow
   seshat.apps.wf.models.Dagger
   seshat.apps.wf.models.Ditch
   seshat.apps.wf.models.Dog
   seshat.apps.wf.models.Donkey
   seshat.apps.wf.models.Earth_rampart
   seshat.apps.wf.models.Elephant
   seshat.apps.wf.models.Fortified_camp
   seshat.apps.wf.models.Gunpowder_siege_artillery
   seshat.apps.wf.models.Handheld_firearm
   seshat.apps.wf.models.Helmet
   seshat.apps.wf.models.Horse
   seshat.apps.wf.models.Iron
   seshat.apps.wf.models.Javelin
   seshat.apps.wf.models.Laminar_armor
   seshat.apps.wf.models.Leather_cloth
   seshat.apps.wf.models.Limb_protection
   seshat.apps.wf.models.Long_wall
   seshat.apps.wf.models.Merchant_ships_pressed_into_service
   seshat.apps.wf.models.Moat
   seshat.apps.wf.models.Modern_fortification
   seshat.apps.wf.models.Plate_armor
   seshat.apps.wf.models.Polearm
   seshat.apps.wf.models.Scaled_armor
   seshat.apps.wf.models.Self_bow
   seshat.apps.wf.models.Settlements_in_a_defensive_position
   seshat.apps.wf.models.Shield
   seshat.apps.wf.models.Sling
   seshat.apps.wf.models.Sling_siege_engine
   seshat.apps.wf.models.Small_vessels_canoes_etc
   seshat.apps.wf.models.Spear
   seshat.apps.wf.models.Specialized_military_vessel
   seshat.apps.wf.models.Steel
   seshat.apps.wf.models.Stone_walls_mortared
   seshat.apps.wf.models.Stone_walls_non_mortared
   seshat.apps.wf.models.Sword
   seshat.apps.wf.models.Tension_siege_engine
   seshat.apps.wf.models.War_club
   seshat.apps.wf.models.Wood_bark_etc
   seshat.apps.wf.models.Wooden_palisade


Functions
---------

.. autoapisummary::

   seshat.apps.wf.models.call_my_name
   seshat.apps.wf.models.clean_times
   seshat.apps.wf.models.return_citations


Module Contents
---------------

.. py:class:: Atlatl(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Atlatl'



      .. py:attribute:: verbose_name_plural
         :value: 'Atlatls'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: atlatl


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Battle_axe(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Battle_axe'



      .. py:attribute:: verbose_name_plural
         :value: 'Battle_axes'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: battle_axe


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Breastplate(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Breastplate'



      .. py:attribute:: verbose_name_plural
         :value: 'Breastplates'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: breastplate


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Bronze(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Bronze'



      .. py:attribute:: verbose_name_plural
         :value: 'Bronzes'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: bronze


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Camel(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Camel'



      .. py:attribute:: verbose_name_plural
         :value: 'Camels'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: camel


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Chainmail(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Chainmail'



      .. py:attribute:: verbose_name_plural
         :value: 'Chainmails'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: chainmail


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Complex_fortification(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Complex_fortification'



      .. py:attribute:: verbose_name_plural
         :value: 'Complex_fortifications'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: complex_fortification


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Composite_bow(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Composite_bow'



      .. py:attribute:: verbose_name_plural
         :value: 'Composite_bows'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: composite_bow


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Copper(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Copper'



      .. py:attribute:: verbose_name_plural
         :value: 'Coppers'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: copper


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Crossbow(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Crossbow'



      .. py:attribute:: verbose_name_plural
         :value: 'Crossbows'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: crossbow


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Dagger(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Dagger'



      .. py:attribute:: verbose_name_plural
         :value: 'Daggers'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


   .. py:method:: sub_subsection()


   .. py:method:: subsection()


   .. py:attribute:: dagger


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the return_citations
         function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:attribute:: name


.. py:class:: Ditch(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Ditch'



      .. py:attribute:: verbose_name_plural
         :value: 'Ditchs'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: ditch


   .. py:attribute:: name


.. py:class:: Dog(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Dog'



      .. py:attribute:: verbose_name_plural
         :value: 'Dogs'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: dog


   .. py:attribute:: name


.. py:class:: Donkey(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Donkey'



      .. py:attribute:: verbose_name_plural
         :value: 'Donkeies'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: donkey


   .. py:attribute:: name


.. py:class:: Earth_rampart(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Earth_rampart'



      .. py:attribute:: verbose_name_plural
         :value: 'Earth_ramparts'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: earth_rampart


   .. py:attribute:: name


.. py:class:: Elephant(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Elephant'



      .. py:attribute:: verbose_name_plural
         :value: 'Elephants'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: elephant


   .. py:attribute:: name


.. py:class:: Fortified_camp(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Fortified_camp'



      .. py:attribute:: verbose_name_plural
         :value: 'Fortified_camps'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: fortified_camp


   .. py:attribute:: name


.. py:class:: Gunpowder_siege_artillery(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Gunpowder_siege_artillery'



      .. py:attribute:: verbose_name_plural
         :value: 'Gunpowder_siege_artilleries'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: gunpowder_siege_artillery


   .. py:attribute:: name


.. py:class:: Handheld_firearm(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Handheld_firearm'



      .. py:attribute:: verbose_name_plural
         :value: 'Handheld_firearms'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: handheld_firearm


   .. py:attribute:: name


.. py:class:: Helmet(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Helmet'



      .. py:attribute:: verbose_name_plural
         :value: 'Helmets'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: helmet


   .. py:attribute:: name


.. py:class:: Horse(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Horse'



      .. py:attribute:: verbose_name_plural
         :value: 'Horses'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: horse


   .. py:attribute:: name


.. py:class:: Iron(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Iron'



      .. py:attribute:: verbose_name_plural
         :value: 'Irons'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: iron


   .. py:attribute:: name


.. py:class:: Javelin(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Javelin'



      .. py:attribute:: verbose_name_plural
         :value: 'Javelins'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: javelin


   .. py:attribute:: name


.. py:class:: Laminar_armor(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Laminar_armor'



      .. py:attribute:: verbose_name_plural
         :value: 'Laminar_armors'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: laminar_armor


   .. py:attribute:: name


.. py:class:: Leather_cloth(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Leather_cloth'



      .. py:attribute:: verbose_name_plural
         :value: 'Leather_cloths'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: leather_cloth


   .. py:attribute:: name


.. py:class:: Limb_protection(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Limb_protection'



      .. py:attribute:: verbose_name_plural
         :value: 'Limb_protections'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: limb_protection


   .. py:attribute:: name


.. py:class:: Long_wall(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'long_wall'



      .. py:attribute:: verbose_name_plural
         :value: 'Long walls'




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


   .. py:attribute:: long_wall_from


   .. py:attribute:: long_wall_to


   .. py:attribute:: name


.. py:class:: Merchant_ships_pressed_into_service(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Merchant_ships_pressed_into_service'



      .. py:attribute:: verbose_name_plural
         :value: 'Merchant_ships_pressed_into_services'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: merchant_ships_pressed_into_service


   .. py:attribute:: name


.. py:class:: Moat(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Moat'



      .. py:attribute:: verbose_name_plural
         :value: 'Moats'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: moat


   .. py:attribute:: name


.. py:class:: Modern_fortification(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Modern_fortification'



      .. py:attribute:: verbose_name_plural
         :value: 'Modern_fortifications'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: modern_fortification


   .. py:attribute:: name


.. py:class:: Plate_armor(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Plate_armor'



      .. py:attribute:: verbose_name_plural
         :value: 'Plate_armors'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: plate_armor


.. py:class:: Polearm(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Polearm'



      .. py:attribute:: verbose_name_plural
         :value: 'Polearms'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: polearm


.. py:class:: Scaled_armor(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Scaled_armor'



      .. py:attribute:: verbose_name_plural
         :value: 'Scaled_armors'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: scaled_armor


.. py:class:: Self_bow(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Self_bow'



      .. py:attribute:: verbose_name_plural
         :value: 'Self_bows'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: self_bow


.. py:class:: Settlements_in_a_defensive_position(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Settlements_in_a_defensive_position'



      .. py:attribute:: verbose_name_plural
         :value: 'Settlements_in_a_defensive_positions'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: settlements_in_a_defensive_position


.. py:class:: Shield(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Shield'



      .. py:attribute:: verbose_name_plural
         :value: 'Shields'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: shield


.. py:class:: Sling(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Sling'



      .. py:attribute:: verbose_name_plural
         :value: 'Slings'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: sling


.. py:class:: Sling_siege_engine(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Sling_siege_engine'



      .. py:attribute:: verbose_name_plural
         :value: 'Sling_siege_engines'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: sling_siege_engine


.. py:class:: Small_vessels_canoes_etc(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Small_vessels_canoes_etc'



      .. py:attribute:: verbose_name_plural
         :value: 'Small_vessels_canoes_etcs'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: small_vessels_canoes_etc


.. py:class:: Spear(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Spear'



      .. py:attribute:: verbose_name_plural
         :value: 'Spears'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: spear


.. py:class:: Specialized_military_vessel(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Specialized_military_vessel'



      .. py:attribute:: verbose_name_plural
         :value: 'Specialized_military_vessels'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: specialized_military_vessel


.. py:class:: Steel(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Steel'



      .. py:attribute:: verbose_name_plural
         :value: 'Steels'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: steel


.. py:class:: Stone_walls_mortared(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Stone_walls_mortared'



      .. py:attribute:: verbose_name_plural
         :value: 'Stone_walls_mortareds'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: stone_walls_mortared


.. py:class:: Stone_walls_non_mortared(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Stone_walls_non_mortared'



      .. py:attribute:: verbose_name_plural
         :value: 'Stone_walls_non_mortareds'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: stone_walls_non_mortared


.. py:class:: Sword(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Sword'



      .. py:attribute:: verbose_name_plural
         :value: 'Swords'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: sword


.. py:class:: Tension_siege_engine(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Tension_siege_engine'



      .. py:attribute:: verbose_name_plural
         :value: 'Tension_siege_engines'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: tension_siege_engine


.. py:class:: War_club(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'War_club'



      .. py:attribute:: verbose_name_plural
         :value: 'War_clubs'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: war_club


.. py:class:: Wood_bark_etc(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Wood_bark_etc'



      .. py:attribute:: verbose_name_plural
         :value: 'Wood_bark_etcs'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: wood_bark_etc


.. py:class:: Wooden_palisade(*args, **kwargs)

   Bases: :py:obj:`seshat.apps.core.models.SeshatCommon`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['year_from', 'year_to']



      .. py:attribute:: verbose_name
         :value: 'Wooden_palisade'



      .. py:attribute:: verbose_name_plural
         :value: 'Wooden_palisades'




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


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: show_nga()


   .. py:method:: show_value()


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


   .. py:attribute:: wooden_palisade


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


