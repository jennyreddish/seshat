seshat.apps.core.models
=======================

.. py:module:: seshat.apps.core.models


Attributes
----------

.. autoapisummary::

   seshat.apps.core.models.AA
   seshat.apps.core.models.AP
   seshat.apps.core.models.APS
   seshat.apps.core.models.AS
   seshat.apps.core.models.A_TO_P
   seshat.apps.core.models.Certainty
   seshat.apps.core.models.NFY
   seshat.apps.core.models.POLITY_TAG_CHOICES
   seshat.apps.core.models.PP
   seshat.apps.core.models.PS
   seshat.apps.core.models.P_TO_A
   seshat.apps.core.models.Tags
   seshat.apps.core.models.U
   seshat.apps.core.models.UU
   seshat.apps.core.models.WORLD_REGION_CHOICES


Classes
-------

.. autoapisummary::

   seshat.apps.core.models.Capital
   seshat.apps.core.models.Citation
   seshat.apps.core.models.Cliopatria
   seshat.apps.core.models.Country
   seshat.apps.core.models.GADMCountries
   seshat.apps.core.models.GADMProvinces
   seshat.apps.core.models.GADMShapefile
   seshat.apps.core.models.Macro_region
   seshat.apps.core.models.Nga
   seshat.apps.core.models.Ngapolityrel
   seshat.apps.core.models.Polity
   seshat.apps.core.models.Reference
   seshat.apps.core.models.Religion
   seshat.apps.core.models.ScpThroughCtn
   seshat.apps.core.models.Section
   seshat.apps.core.models.SeshatComment
   seshat.apps.core.models.SeshatCommentPart
   seshat.apps.core.models.SeshatCommon
   seshat.apps.core.models.SeshatPrivateComment
   seshat.apps.core.models.SeshatPrivateCommentPart
   seshat.apps.core.models.Seshat_region
   seshat.apps.core.models.Subsection
   seshat.apps.core.models.Variablehierarchy


Functions
---------

.. autoapisummary::

   seshat.apps.core.models.give_me_a_color_for_expert
   seshat.apps.core.models.return_citations_for_comments
   seshat.apps.core.models.return_citations_plus_for_comments
   seshat.apps.core.models.return_number_of_citations_for_comments
   seshat.apps.core.models.return_number_of_citations_plus_for_comments


Module Contents
---------------

.. py:class:: Capital(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a capital.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['is_verified']




   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: alternative_names


   .. py:attribute:: current_country


   .. py:attribute:: is_verified


   .. py:attribute:: latitude


   .. py:attribute:: longitude


   .. py:attribute:: name


   .. py:attribute:: note


   .. py:attribute:: url_on_the_map


   .. py:attribute:: year_from


   .. py:attribute:: year_to


.. py:class:: Citation(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a specific citation.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: constraints


      .. py:attribute:: ordering
         :value: ['-modified_date']




   .. py:method:: full_citation_display()

      Returns a string of the full citation. If the citation has a title, it
      is included in the string. If the citation has a creator, it is
      included in the string. If the citation has a year, it is included in
      the string. If the citation has a page_from, it is included in the
      string. If the citation has a page_to, it is included in the string.

      :returns: A string of the full citation.
      :rtype: str



   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: save(*args, **kwargs)

      Saves the citation to the database.

      :param \*args: Additional arguments.
      :param \*\*kwargs: Additional keyword arguments.

      :raises IntegrityError: If the citation cannot be saved to the database.

      :returns: None



   .. py:method:: zoteroer()

      Returns the Zotero link for the citation.

      :returns: The Zotero link for the citation.
      :rtype: str



   .. py:property:: citation_short_title
      Returns a short title for the citation. If the title is longer than
      40 characters, it is truncated. If the title is not provided, a default
      title is returned.

      :returns: A short title for the citation.
      :rtype: str


   .. py:attribute:: created_date


   .. py:attribute:: id


   .. py:attribute:: modified_date


   .. py:attribute:: page_from


   .. py:attribute:: page_to


   .. py:attribute:: ref


.. py:class:: Cliopatria(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing Cliopatria polity borders dataset.


   .. py:attribute:: area


   .. py:attribute:: colour


   .. py:attribute:: components


   .. py:attribute:: end_year


   .. py:attribute:: geom


   .. py:attribute:: id


   .. py:attribute:: member_of


   .. py:attribute:: name


   .. py:attribute:: polity_end_year


   .. py:attribute:: polity_start_year


   .. py:attribute:: seshat_id


   .. py:attribute:: simplified_geom


   .. py:attribute:: start_year


   .. py:attribute:: wikipedia_name


.. py:class:: Country(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a country.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: unique_together
         :value: ('name',)



      .. py:attribute:: verbose_name
         :value: 'country'



      .. py:attribute:: verbose_name_plural
         :value: 'countries'




   .. py:attribute:: name


   .. py:attribute:: polity


.. py:class:: GADMCountries(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a country (GADM).


   .. py:attribute:: COUNTRY


   .. py:attribute:: geom


.. py:class:: GADMProvinces(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a province (GADM).


   .. py:attribute:: COUNTRY


   .. py:attribute:: ENGTYPE_1


   .. py:attribute:: NAME_1


   .. py:attribute:: geom


.. py:class:: GADMShapefile(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   



   .. py:attribute:: CC_1


   .. py:attribute:: CC_2


   .. py:attribute:: CC_3


   .. py:attribute:: CC_4


   .. py:attribute:: CC_5


   .. py:attribute:: CONTINENT


   .. py:attribute:: COUNTRY


   .. py:attribute:: DISPUTEDBY


   .. py:attribute:: ENGTYPE_1


   .. py:attribute:: ENGTYPE_2


   .. py:attribute:: ENGTYPE_3


   .. py:attribute:: ENGTYPE_4


   .. py:attribute:: ENGTYPE_5


   .. py:attribute:: GID_0


   .. py:attribute:: GID_1


   .. py:attribute:: GID_2


   .. py:attribute:: GID_3


   .. py:attribute:: GID_4


   .. py:attribute:: GID_5


   .. py:attribute:: GOVERNEDBY


   .. py:attribute:: HASC_1


   .. py:attribute:: HASC_2


   .. py:attribute:: HASC_3


   .. py:attribute:: ISO_1


   .. py:attribute:: NAME_0


   .. py:attribute:: NAME_1


   .. py:attribute:: NAME_2


   .. py:attribute:: NAME_3


   .. py:attribute:: NAME_4


   .. py:attribute:: NAME_5


   .. py:attribute:: NL_NAME_1


   .. py:attribute:: NL_NAME_2


   .. py:attribute:: NL_NAME_3


   .. py:attribute:: REGION


   .. py:attribute:: SOVEREIGN


   .. py:attribute:: SUBCONT


   .. py:attribute:: TYPE_1


   .. py:attribute:: TYPE_2


   .. py:attribute:: TYPE_3


   .. py:attribute:: TYPE_4


   .. py:attribute:: TYPE_5


   .. py:attribute:: UID


   .. py:attribute:: VALIDFR_1


   .. py:attribute:: VALIDFR_2


   .. py:attribute:: VALIDFR_3


   .. py:attribute:: VALIDFR_4


   .. py:attribute:: VARNAME_0


   .. py:attribute:: VARNAME_1


   .. py:attribute:: VARNAME_2


   .. py:attribute:: VARNAME_3


   .. py:attribute:: VARNAME_4


   .. py:attribute:: VARREGION


   .. py:attribute:: geom


.. py:class:: Macro_region(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a macro region.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['name']




   .. py:attribute:: name


.. py:class:: Nga(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a NGA.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['name']




   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: capital_city


   .. py:attribute:: fao_country


   .. py:attribute:: latitude


   .. py:attribute:: longitude


   .. py:attribute:: name


   .. py:attribute:: nga_code


   .. py:attribute:: subregion


   .. py:attribute:: world_region


.. py:class:: Ngapolityrel(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a relationship between a NGA and a polity.


   .. py:attribute:: is_home_nga


   .. py:attribute:: name


   .. py:attribute:: nga_party


   .. py:attribute:: polity_party


   .. py:attribute:: year_from


   .. py:attribute:: year_to


.. py:class:: Polity(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a polity.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['long_name']



      .. py:attribute:: unique_together
         :value: ('name',)



      .. py:attribute:: verbose_name
         :value: 'polity'



      .. py:attribute:: verbose_name_plural
         :value: 'polities'




   .. py:method:: clean()

      Verifies a number of conditions on the start and end years of the polity.

      :raises ValidationError: If the start year is greater than the end year.
      :raises ValidationError: If the end year is greater than the current year.
      :raises ValidationError: If the start year is greater than the current year.

      :returns: None



   .. py:attribute:: created_date


   .. py:attribute:: end_year


   .. py:attribute:: general_description


   .. py:attribute:: home_nga


   .. py:attribute:: home_seshat_region


   .. py:attribute:: long_name


   .. py:attribute:: modified_date


   .. py:attribute:: name


   .. py:attribute:: new_name


   .. py:attribute:: polity_tag


   .. py:attribute:: private_comment


   .. py:attribute:: private_comment_n


   .. py:attribute:: shapefile_name


   .. py:attribute:: start_year


.. py:class:: Reference(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model Representing a reference.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['-created_date', 'title']



      .. py:attribute:: unique_together
         :value: ('zotero_link',)




   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: created_date


   .. py:attribute:: creator


   .. py:attribute:: item_type


   .. py:attribute:: long_name


   .. py:attribute:: modified_date


   .. py:property:: reference_short_title
      Returns a short title for the reference. If the title is longer than
      60 characters, it is truncated. If the title is not provided, a default
      title is returned.

      :returns: A short title for the reference.
      :rtype: str


   .. py:attribute:: title


   .. py:attribute:: url_link


   .. py:attribute:: year


   .. py:attribute:: zotero_link


.. py:class:: Religion(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a religion.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['name']




   .. py:attribute:: name


   .. py:attribute:: religion_family


   .. py:attribute:: religion_genus


   .. py:attribute:: religion_name


.. py:class:: ScpThroughCtn(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a through model for the many-to-many relationship between
   a comment part and a citation.


   .. py:attribute:: citation


   .. py:attribute:: parent_paragraphs


   .. py:attribute:: seshatcommentpart


.. py:class:: Section(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a section.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: unique_together
         :value: ('name',)




   .. py:attribute:: name


.. py:class:: SeshatComment(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a comment.


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:method:: zoteroer()

      Returns the Zotero link for the comment.

      :returns: The Zotero link for the comment.
      :rtype: str



   .. py:attribute:: text


.. py:class:: SeshatCommentPart(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a part of a comment.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['comment_order', 'modified_date']




   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: citation_index


   .. py:property:: citations_count
      Returns the number of citations for a comment.

      :returns: The number of citations for a comment.
      :rtype: int


   .. py:property:: citations_count_plus
      Returns the number of citations for a comment.

      :returns: The number of citations for a comment.
      :rtype: int


   .. py:attribute:: comment


   .. py:attribute:: comment_citations


   .. py:attribute:: comment_citations_plus


   .. py:attribute:: comment_curator


   .. py:attribute:: comment_order


   .. py:attribute:: comment_part_text


   .. py:property:: display_citations
      Display the citations of the model instance.

      :noindex:

      .. note::

         The method is a property, and an alias for the
         return_citations_for_comments function.

      :returns: The citations of the model instance, separated by comma.
      :rtype: str


   .. py:property:: display_citations_plus
      Returns a string of all the citations for a comment.

      :noindex:

      .. note::

         The method is a property, and an alias for the
         return_citations_for_comments function.

      :returns: A string of all the citations for a comment.
      :rtype: str


   .. py:attribute:: modified_date


.. py:class:: SeshatCommon(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a common Seshat model.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: abstract
         :value: True



      .. py:attribute:: ordering
         :value: ['polity']




   .. py:attribute:: citations


   .. py:attribute:: comment


   .. py:attribute:: created_date


   .. py:attribute:: curator


   .. py:attribute:: description


   .. py:attribute:: drb_reviewed


   .. py:attribute:: expert_reviewed


   .. py:attribute:: finalized


   .. py:attribute:: is_disputed


   .. py:attribute:: is_uncertain


   .. py:attribute:: modified_date


   .. py:attribute:: name


   .. py:attribute:: note


   .. py:attribute:: polity


   .. py:attribute:: private_comment


   .. py:attribute:: tag


   .. py:attribute:: year_from


   .. py:attribute:: year_to


.. py:class:: SeshatPrivateComment(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a private comment.


   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: text


.. py:class:: SeshatPrivateCommentPart(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a part of a private comment.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['created_date', 'last_modified_date']




   .. py:method:: get_absolute_url()

      Returns the url to access a particular instance of the model.

      :noindex:

      :returns: A string of the url to access a particular instance of the model.
      :rtype: str



   .. py:attribute:: created_date


   .. py:attribute:: is_done


   .. py:attribute:: last_modified_date


   .. py:attribute:: private_comment


   .. py:attribute:: private_comment_owner


   .. py:attribute:: private_comment_part_text


   .. py:attribute:: private_comment_reader


.. py:class:: Seshat_region(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a Seshat region.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: ordering
         :value: ['mac_region__name', 'name']




   .. py:attribute:: mac_region


   .. py:attribute:: name


   .. py:attribute:: subregions_list


.. py:class:: Subsection(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a subsection.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: unique_together
         :value: ('name', 'section')




   .. py:attribute:: name


   .. py:attribute:: section


.. py:class:: Variablehierarchy(*args, **kwargs)

   Bases: :py:obj:`django.contrib.gis.db.models.Model`


   Model representing a variable hierarchy.


   .. py:class:: Meta

      :noindex:


      .. py:attribute:: unique_together
         :value: ('name', 'section', 'subsection')




   .. py:attribute:: explanation


   .. py:attribute:: is_verified


   .. py:attribute:: name


   .. py:attribute:: section


   .. py:attribute:: subsection


.. py:function:: give_me_a_color_for_expert(value)

   Returns a color for a given expert.

   :param value: The id of the expert.
   :type value: int

   :returns: A color for the expert.
   :rtype: str


.. py:function:: return_citations_for_comments(self)

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


.. py:function:: return_citations_plus_for_comments(self)

   Returns a string of all the citations for a comment.

   :returns: A string of all the citations for a comment.
   :rtype: str


.. py:function:: return_number_of_citations_for_comments(self)

   Returns the number of citations for a comment.

   :returns: The number of citations for a comment.
   :rtype: int


.. py:function:: return_number_of_citations_plus_for_comments(self)

   Returns the number of citations for a comment.

   :returns: The number of citations for a comment.
   :rtype: int


.. py:data:: AA
   :value: 'A'


.. py:data:: AP
   :value: 'A;P'


.. py:data:: APS
   :value: 'A;P*'


.. py:data:: AS
   :value: 'A*'


.. py:data:: A_TO_P
   :value: 'A~P'


.. py:data:: Certainty

.. py:data:: NFY
   :value: 'NFY'


.. py:data:: POLITY_TAG_CHOICES
   :value: (('LEGACY', 'Equinox 2020 Polities'), ('POL_AFR_EAST', 'NEW East African Polities'),...


.. py:data:: PP
   :value: 'P'


.. py:data:: PS
   :value: 'P*'


.. py:data:: P_TO_A
   :value: 'P~A'


.. py:data:: Tags
   :value: (('TRS', 'Confident'), ('SSP', 'Suspected'), ('IFR', 'Inferred'))


.. py:data:: U
   :value: 'U'


.. py:data:: UU
   :value: 'U*'


.. py:data:: WORLD_REGION_CHOICES
   :value: (('Europe', 'Europe'), ('Southwest Asia', 'Southwest Asia'), ('Africa', 'Africa'), ('Central...


