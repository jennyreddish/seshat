seshat.apps.seshat_api.views.core
=================================

.. py:module:: seshat.apps.seshat_api.views.core


Classes
-------

.. autoapisummary::

   seshat.apps.seshat_api.views.core.CapitalViewSet
   seshat.apps.seshat_api.views.core.CitationViewSet
   seshat.apps.seshat_api.views.core.CliopatriaViewSet
   seshat.apps.seshat_api.views.core.CountryViewSet
   seshat.apps.seshat_api.views.core.GADMCountriesViewSet
   seshat.apps.seshat_api.views.core.GADMProvincesViewSet
   seshat.apps.seshat_api.views.core.GADMShapefileViewSet
   seshat.apps.seshat_api.views.core.MacroRegionViewSet
   seshat.apps.seshat_api.views.core.NGAPolityRelationsViewSet
   seshat.apps.seshat_api.views.core.NGAViewSet
   seshat.apps.seshat_api.views.core.PolityViewSet
   seshat.apps.seshat_api.views.core.PrivateCommentsPartsViewSet
   seshat.apps.seshat_api.views.core.PrivateCommentsViewSet
   seshat.apps.seshat_api.views.core.ReferenceViewSet
   seshat.apps.seshat_api.views.core.RegionViewSet
   seshat.apps.seshat_api.views.core.ReligionViewSet
   seshat.apps.seshat_api.views.core.ScpThroughCtnViewSet
   seshat.apps.seshat_api.views.core.SectionViewSet
   seshat.apps.seshat_api.views.core.SeshatCommentPartViewSet
   seshat.apps.seshat_api.views.core.SeshatCommentViewSet
   seshat.apps.seshat_api.views.core.SubsectionViewSet
   seshat.apps.seshat_api.views.core.VariableHierarchyViewSet


Module Contents
---------------

.. py:class:: CapitalViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Capitals.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CitationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Citations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CliopatriaViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Cliopatria Shapefiles.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CountryViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Countries.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: GADMCountriesViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing GADM Countries.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: GADMProvincesViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing GADM Provinces.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: GADMShapefileViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing GADM Shapefiles.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: MacroRegionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Macro Regions.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: NGAPolityRelationsViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing NGA Polity Relations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: NGAViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing NGAs, Natural Geographic Areas.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PolityViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Polities.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: search_fields
      :value: ['@long_name', '@new_name']



.. py:class:: PrivateCommentsPartsViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Seshat Private Comment Parts.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: PrivateCommentsViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Seshat Private Comments.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: ReferenceViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing References.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: RegionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Regions.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ReligionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Religions.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ScpThroughCtnViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Seshat Comment Parts' relations to
   Citations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: SectionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Sections.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SeshatCommentPartViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Seshat Comment Parts.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: SeshatCommentViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Seshat Comments.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: SubsectionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Subsections.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: VariableHierarchyViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Variable Hierarchies.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


