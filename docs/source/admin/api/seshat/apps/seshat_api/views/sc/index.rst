seshat.apps.seshat_api.views.sc
===============================

.. py:module:: seshat.apps.seshat_api.views.sc


Classes
-------

.. autoapisummary::

   seshat.apps.seshat_api.views.sc.AdministrativeLevelViewSet
   seshat.apps.seshat_api.views.sc.AreaMeasurementSystemViewSet
   seshat.apps.seshat_api.views.sc.ArticleViewSet
   seshat.apps.seshat_api.views.sc.BridgeViewSet
   seshat.apps.seshat_api.views.sc.BurialSiteViewSet
   seshat.apps.seshat_api.views.sc.CalendarViewSet
   seshat.apps.seshat_api.views.sc.CanalViewSet
   seshat.apps.seshat_api.views.sc.CeremonialSiteViewSet
   seshat.apps.seshat_api.views.sc.CommunalBuildingViewSet
   seshat.apps.seshat_api.views.sc.CourierViewSet
   seshat.apps.seshat_api.views.sc.CourtViewSet
   seshat.apps.seshat_api.views.sc.DebtAndCreditStructureViewSet
   seshat.apps.seshat_api.views.sc.DrinkingWaterSupplySystemViewSet
   seshat.apps.seshat_api.views.sc.EnclosureViewSet
   seshat.apps.seshat_api.views.sc.EntertainmentBuildingViewSet
   seshat.apps.seshat_api.views.sc.ExaminationSystemViewSet
   seshat.apps.seshat_api.views.sc.FastestIndividualCommunicationViewSet
   seshat.apps.seshat_api.views.sc.FictionViewSet
   seshat.apps.seshat_api.views.sc.FoodStorageSiteViewSet
   seshat.apps.seshat_api.views.sc.ForeignCoinViewSet
   seshat.apps.seshat_api.views.sc.FormalLegalCodeViewSet
   seshat.apps.seshat_api.views.sc.FullTimeBureaucratViewSet
   seshat.apps.seshat_api.views.sc.GeneralPostalServiceViewSet
   seshat.apps.seshat_api.views.sc.GeometricalMeasurementSystemViewSet
   seshat.apps.seshat_api.views.sc.HistoryViewSet
   seshat.apps.seshat_api.views.sc.IndigenousCoinViewSet
   seshat.apps.seshat_api.views.sc.IrrigationSystemViewSet
   seshat.apps.seshat_api.views.sc.JudgeViewSet
   seshat.apps.seshat_api.views.sc.KnowledgeOrInformationBuildingViewSet
   seshat.apps.seshat_api.views.sc.LargestCommunicationDistanceViewSet
   seshat.apps.seshat_api.views.sc.LengthMeasurementSystemViewSet
   seshat.apps.seshat_api.views.sc.ListsTablesAndClassificationViewSet
   seshat.apps.seshat_api.views.sc.MarketViewSet
   seshat.apps.seshat_api.views.sc.MeritPromotionViewSet
   seshat.apps.seshat_api.views.sc.MilitaryLevelViewSet
   seshat.apps.seshat_api.views.sc.MinesOrQuarryViewSet
   seshat.apps.seshat_api.views.sc.MnemonicDeviceViewSet
   seshat.apps.seshat_api.views.sc.NonPhoneticWritingViewSet
   seshat.apps.seshat_api.views.sc.NonwrittenRecordViewSet
   seshat.apps.seshat_api.views.sc.OccupationalComplexityViewSet
   seshat.apps.seshat_api.views.sc.OtherMeasurementSystemViewSet
   seshat.apps.seshat_api.views.sc.OtherSpecialPurposeSiteViewSet
   seshat.apps.seshat_api.views.sc.OtherUtilitarianPublicBuildingViewSet
   seshat.apps.seshat_api.views.sc.PaperCurrencyViewSet
   seshat.apps.seshat_api.views.sc.PhilosophyViewSet
   seshat.apps.seshat_api.views.sc.PhoneticAlphabeticWritingViewSet
   seshat.apps.seshat_api.views.sc.PolityPopulationViewSet
   seshat.apps.seshat_api.views.sc.PolityTerritoryViewSet
   seshat.apps.seshat_api.views.sc.PopulationOfTheLargestSettlementViewSet
   seshat.apps.seshat_api.views.sc.PortViewSet
   seshat.apps.seshat_api.views.sc.PostalStationViewSet
   seshat.apps.seshat_api.views.sc.PracticalLiteratureViewSet
   seshat.apps.seshat_api.views.sc.PreciousMetalViewSet
   seshat.apps.seshat_api.views.sc.ProfessionalLawyerViewSet
   seshat.apps.seshat_api.views.sc.ProfessionalMilitaryOfficerViewSet
   seshat.apps.seshat_api.views.sc.ProfessionalPriesthoodViewSet
   seshat.apps.seshat_api.views.sc.ProfessionalSoldierViewSet
   seshat.apps.seshat_api.views.sc.RAViewSet
   seshat.apps.seshat_api.views.sc.ReligiousLevelViewSet
   seshat.apps.seshat_api.views.sc.ReligiousLiteratureViewSet
   seshat.apps.seshat_api.views.sc.RoadViewSet
   seshat.apps.seshat_api.views.sc.SacredTextViewSet
   seshat.apps.seshat_api.views.sc.ScientificLiteratureViewSet
   seshat.apps.seshat_api.views.sc.ScriptViewSet
   seshat.apps.seshat_api.views.sc.SettlementHierarchyViewSet
   seshat.apps.seshat_api.views.sc.SourceOfSupportViewSet
   seshat.apps.seshat_api.views.sc.SpecialPurposeHouseViewSet
   seshat.apps.seshat_api.views.sc.SpecialPurposeSiteViewSet
   seshat.apps.seshat_api.views.sc.SpecializedGovernmentBuildingViewSet
   seshat.apps.seshat_api.views.sc.StoreOfWealthViewSet
   seshat.apps.seshat_api.views.sc.SymbolicBuildingViewSet
   seshat.apps.seshat_api.views.sc.TimeMeasurementSystemViewSet
   seshat.apps.seshat_api.views.sc.TokenViewSet
   seshat.apps.seshat_api.views.sc.TradingEmporiaViewSet
   seshat.apps.seshat_api.views.sc.UtilitarianPublicBuildingViewSet
   seshat.apps.seshat_api.views.sc.VolumeMeasurementSystemViewSet
   seshat.apps.seshat_api.views.sc.WeightMeasurementSystemViewSet
   seshat.apps.seshat_api.views.sc.WrittenRecordViewSet


Module Contents
---------------

.. py:class:: AdministrativeLevelViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Administrative Levels.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: AreaMeasurementSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Area Measurement Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ArticleViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Articles.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: BridgeViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Bridges.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: BurialSiteViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Burial Sites.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CalendarViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Calendars.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CanalViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Canals.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CeremonialSiteViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Ceremonial Sites.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CommunalBuildingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Communal Buildings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CourierViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Couriers.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: CourtViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Courts.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: DebtAndCreditStructureViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Debt and Credit Structures.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: DrinkingWaterSupplySystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Drinking Water Supply Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: EnclosureViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Enclosures.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: EntertainmentBuildingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Entertainment Buildings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ExaminationSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Examination Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: FastestIndividualCommunicationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Fastest Individual Communications.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: FictionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Fictions.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: FoodStorageSiteViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Food Storage Sites.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ForeignCoinViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Foreign Coins.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: FormalLegalCodeViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Formal Legal Codes.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: FullTimeBureaucratViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Full Time Bureaucrats.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: GeneralPostalServiceViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing General Postal Services.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: GeometricalMeasurementSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Geometrical Measurement Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: HistoryViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Histories.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: IndigenousCoinViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Indigenous Coins.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: IrrigationSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Irrigation Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: JudgeViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Judges.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: KnowledgeOrInformationBuildingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Knowledge or Information Buildings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: LargestCommunicationDistanceViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Largest Communication Distances.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: LengthMeasurementSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Length Measurement Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ListsTablesAndClassificationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Lists, Tables, and Classifications.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: MarketViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Markets.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: MeritPromotionViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Merit Promotions.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: MilitaryLevelViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Military Levels.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: MinesOrQuarryViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Mines or Quarries.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: MnemonicDeviceViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Mnemonic Devices.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: NonPhoneticWritingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Non-Phonetic Writings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: NonwrittenRecordViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Nonwritten Records.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: OccupationalComplexityViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Occupational Complexities.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: OtherMeasurementSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Other Measurement Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: OtherSpecialPurposeSiteViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Other Special Purpose Sites.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: OtherUtilitarianPublicBuildingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Other Utilitarian Public Buildings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PaperCurrencyViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Paper Currencies.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PhilosophyViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Philosophies.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PhoneticAlphabeticWritingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Phonetic Alphabetic Writings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PolityPopulationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Polity Populations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PolityTerritoryViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Polity Territories.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PopulationOfTheLargestSettlementViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Population of the Largest Settlements.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PortViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Ports.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PostalStationViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Postal Stations.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PracticalLiteratureViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Practical Literatures.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: PreciousMetalViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Precious Metals.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ProfessionalLawyerViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Professional Lawyers.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ProfessionalMilitaryOfficerViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Professional Military Officers.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ProfessionalPriesthoodViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Professional Priesthoods.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ProfessionalSoldierViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Professional Soldiers.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: RAViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing RAs.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: ReligiousLevelViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Religious Levels.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ReligiousLiteratureViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Religious Literatures.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: RoadViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Roads.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SacredTextViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Sacred Texts.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ScientificLiteratureViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Scientific Literatures.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: ScriptViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Scripts.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SettlementHierarchyViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Settlement Hierarchies.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SourceOfSupportViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Sources of Support.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SpecialPurposeHouseViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Special Purpose Houses.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SpecialPurposeSiteViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Special Purpose Sites.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SpecializedGovernmentBuildingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Specialized Government Buildings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: StoreOfWealthViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Stores of Wealth.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: SymbolicBuildingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Symbolic Buildings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: TimeMeasurementSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Time Measurement Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: TokenViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Tokens.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: TradingEmporiaViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Trading Emporias.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: UtilitarianPublicBuildingViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Utilitarian Public Buildings.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: VolumeMeasurementSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Volume Measurement Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: WeightMeasurementSystemViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Weight Measurement Systems.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


.. py:class:: WrittenRecordViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.FilterBackends`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Written Records.


   .. py:attribute:: filterset_class


   .. py:attribute:: model


   .. py:attribute:: pagination_class


