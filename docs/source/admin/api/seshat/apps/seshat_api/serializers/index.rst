seshat.apps.seshat_api.serializers
==================================

.. py:module:: seshat.apps.seshat_api.serializers


Attributes
----------

.. autoapisummary::

   seshat.apps.seshat_api.serializers.SESHAT_API_DEPTH


Classes
-------

.. autoapisummary::

   seshat.apps.seshat_api.serializers.GeneralSerializer


Module Contents
---------------

.. py:class:: GeneralSerializer(instance=None, data=empty, **kwargs)

   Bases: :py:obj:`rest_framework.serializers.ModelSerializer`


   A serializer for all models across the API.


   .. py:class:: Meta

      .. py:attribute:: depth


      .. py:attribute:: fields
         :value: '__all__'



      .. py:attribute:: model
         :value: None




.. py:data:: SESHAT_API_DEPTH
   :value: 3


   Defines the depth of recursive serialization across all models.

