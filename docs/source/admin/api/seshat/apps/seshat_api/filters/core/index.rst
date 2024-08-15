seshat.apps.seshat_api.filters.core
===================================

.. py:module:: seshat.apps.seshat_api.filters.core


Classes
-------

.. autoapisummary::

   seshat.apps.seshat_api.filters.core.CapitalFilter
   seshat.apps.seshat_api.filters.core.CitationFilter
   seshat.apps.seshat_api.filters.core.CountryFilter
   seshat.apps.seshat_api.filters.core.GADMCountriesFilter
   seshat.apps.seshat_api.filters.core.GADMProvincesFilter
   seshat.apps.seshat_api.filters.core.GADMShapefileFilter
   seshat.apps.seshat_api.filters.core.MacroRegionFilter
   seshat.apps.seshat_api.filters.core.NGAFilter
   seshat.apps.seshat_api.filters.core.NGAPolityRelationsFilter
   seshat.apps.seshat_api.filters.core.PolityFilter
   seshat.apps.seshat_api.filters.core.PrivateCommentFilter
   seshat.apps.seshat_api.filters.core.PrivateCommentsPartFilter
   seshat.apps.seshat_api.filters.core.ReferenceFilter
   seshat.apps.seshat_api.filters.core.ReligionFilter
   seshat.apps.seshat_api.filters.core.ScpThroughCtnFilter
   seshat.apps.seshat_api.filters.core.SectionFilter
   seshat.apps.seshat_api.filters.core.SeshatCommentFilter
   seshat.apps.seshat_api.filters.core.SeshatCommentPartFilter
   seshat.apps.seshat_api.filters.core.SeshatRegionFilter
   seshat.apps.seshat_api.filters.core.SubsectionFilter
   seshat.apps.seshat_api.filters.core.VariableHierarchyFilter
   seshat.apps.seshat_api.filters.core.VideoShapefileFilter


Module Contents
---------------

.. py:class:: CapitalFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: CitationFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



   .. py:attribute:: reference_creator_contains


   .. py:attribute:: reference_title_contains


   .. py:attribute:: reference_year_gte


   .. py:attribute:: reference_year_lte


.. py:class:: CountryFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



   .. py:attribute:: polity_name_contains


.. py:class:: GADMCountriesFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: GADMProvincesFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: GADMShapefileFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: MacroRegionFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: NGAFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: NGAPolityRelationsFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



   .. py:attribute:: nga_name_contains


   .. py:attribute:: polity_name_contains


.. py:class:: PolityFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



   .. py:attribute:: home_nga_code


   .. py:attribute:: home_nga_name_contains


   .. py:attribute:: home_seshat_region_contains


   .. py:attribute:: max_nga_latitude


   .. py:attribute:: max_nga_longitude


   .. py:attribute:: min_nga_latitude


   .. py:attribute:: min_nga_longitude


.. py:class:: PrivateCommentFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: PrivateCommentsPartFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: ReferenceFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: ReligionFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: ScpThroughCtnFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: SectionFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: SeshatCommentFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: SeshatCommentPartFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: SeshatRegionFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



.. py:class:: SubsectionFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



   .. py:attribute:: section_name_contains


.. py:class:: VariableHierarchyFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



   .. py:attribute:: section_name_contains


   .. py:attribute:: subsection_name_contains


.. py:class:: VideoShapefileFilter(data=None, queryset=None, *, request=None, prefix=None)

   Bases: :py:obj:`django_filters.rest_framework.FilterSet`


   .. py:class:: Meta

      .. py:attribute:: fields


      .. py:attribute:: model



