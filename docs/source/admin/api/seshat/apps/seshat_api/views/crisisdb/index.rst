seshat.apps.seshat_api.views.crisisdb
=====================================

.. py:module:: seshat.apps.seshat_api.views.crisisdb


Classes
-------

.. autoapisummary::

   seshat.apps.seshat_api.views.crisisdb.AgriculturalPopulationViewSet
   seshat.apps.seshat_api.views.crisisdb.ArableLandPerFarmerViewSet
   seshat.apps.seshat_api.views.crisisdb.ArableLandViewSet
   seshat.apps.seshat_api.views.crisisdb.CrisisConsequenceViewSet
   seshat.apps.seshat_api.views.crisisdb.CropFailureEventViewSet
   seshat.apps.seshat_api.views.crisisdb.DiseaseOutbreakViewSet
   seshat.apps.seshat_api.views.crisisdb.DroughtEventViewSet
   seshat.apps.seshat_api.views.crisisdb.ExternalConflictSideViewSet
   seshat.apps.seshat_api.views.crisisdb.ExternalConflictViewSet
   seshat.apps.seshat_api.views.crisisdb.FamineEventViewSet
   seshat.apps.seshat_api.views.crisisdb.GDPPerCapitaViewSet
   seshat.apps.seshat_api.views.crisisdb.GrossGrainSharedPerAgriculturalPopulationViewSet
   seshat.apps.seshat_api.views.crisisdb.HumanSacrificeViewSet
   seshat.apps.seshat_api.views.crisisdb.InternalConflictViewSet
   seshat.apps.seshat_api.views.crisisdb.LocustEventViewSet
   seshat.apps.seshat_api.views.crisisdb.MilitaryExpenseViewSet
   seshat.apps.seshat_api.views.crisisdb.NetGrainSharedPerAgriculturalPopulationViewSet
   seshat.apps.seshat_api.views.crisisdb.PowerTransitionViewSet
   seshat.apps.seshat_api.views.crisisdb.SilverInflowViewSet
   seshat.apps.seshat_api.views.crisisdb.SilverStockViewSet
   seshat.apps.seshat_api.views.crisisdb.SocioeconomicTurmoilEventViewSet
   seshat.apps.seshat_api.views.crisisdb.SurplusViewSet
   seshat.apps.seshat_api.views.crisisdb.TotalPopulationViewSet
   seshat.apps.seshat_api.views.crisisdb.USLocationViewSet
   seshat.apps.seshat_api.views.crisisdb.USViolenceDataSourceViewSet
   seshat.apps.seshat_api.views.crisisdb.USViolenceSubtypeViewSet
   seshat.apps.seshat_api.views.crisisdb.USViolenceViewSet


Module Contents
---------------

.. py:class:: AgriculturalPopulationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Agricultural Populations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ArableLandPerFarmerViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Arable Land Per Farmers.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ArableLandViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Arable Lands.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CrisisConsequenceViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Crisis Consequences.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CropFailureEventViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Crop Failure Events.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: DiseaseOutbreakViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Disease Outbreaks.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: DroughtEventViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Drought Events.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ExternalConflictSideViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing External Conflict Sides.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ExternalConflictViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing External Conflicts.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: FamineEventViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Famine Events.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: GDPPerCapitaViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing GDP Per Capitas.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: GrossGrainSharedPerAgriculturalPopulationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Gross Grain Shared Per Agricultural Populations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: HumanSacrificeViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Human Sacrifices.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: InternalConflictViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Internal Conflicts.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: LocustEventViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Locust Events.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: MilitaryExpenseViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Military Expenses.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: NetGrainSharedPerAgriculturalPopulationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Net Grain Shared Per Agricultural Populations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PowerTransitionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Power Transitions.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SilverInflowViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Silver Inflows.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SilverStockViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Silver Stocks.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SocioeconomicTurmoilEventViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Socioeconomic Turmoil Events.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SurplusViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Surpluses.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: TotalPopulationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Total Populations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: USLocationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing US Locations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: USViolenceDataSourceViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing US Violence Data Sources.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: USViolenceSubtypeViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing US Violence Subtypes.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: USViolenceViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing US Violence.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


