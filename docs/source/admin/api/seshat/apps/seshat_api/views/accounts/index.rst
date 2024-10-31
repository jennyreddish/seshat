seshat.apps.seshat_api.views.accounts
=====================================

.. py:module:: seshat.apps.seshat_api.views.accounts


Classes
-------

.. autoapisummary::

   seshat.apps.seshat_api.views.accounts.ProfileViewSet
   seshat.apps.seshat_api.views.accounts.SeshatExpertViewSet
   seshat.apps.seshat_api.views.accounts.SeshatTaskViewSet


Module Contents
---------------

.. py:class:: ProfileViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ReadOnlyModelViewSet`


   A viewset for viewing user profiles.


   .. py:attribute:: lookup_field
      :value: 'user__username'



   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: SeshatExpertViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ModelViewSet`


   A viewset for viewing and editing Seshat Experts.


   .. py:attribute:: lookup_field
      :value: 'user__username'



   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


.. py:class:: SeshatTaskViewSet(**kwargs)

   Bases: :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPISerializer`, :py:obj:`seshat.apps.seshat_api.views._mixins.MixinSeshatAPIAuth`, :py:obj:`rest_framework.viewsets.ReadOnlyModelViewSet`


   A viewset for viewing Seshat Tasks.


   .. py:attribute:: fields
      :value: '__all__'



   .. py:attribute:: model


   .. py:attribute:: pagination_class


   .. py:attribute:: permissions_dict


