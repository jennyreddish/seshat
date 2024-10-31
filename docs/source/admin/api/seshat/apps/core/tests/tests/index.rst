seshat.apps.core.tests.tests
============================

.. py:module:: seshat.apps.core.tests.tests


Classes
-------

.. autoapisummary::

   seshat.apps.core.tests.tests.ShapesTest


Module Contents
---------------

.. py:class:: ShapesTest(methodName='runTest')

   Bases: :py:obj:`django.test.TestCase`


   Test case for the shape models and views.


   .. py:method:: setUp()

      Set up the test client and Polity entry for the view functions.



   .. py:method:: test_assign_categorical_variables_to_shapes()

      Test the assign_categorical_variables_to_shapes function.



   .. py:method:: test_assign_variables_to_shapes()

      Test the assign_variables_to_shapes function.



   .. py:method:: test_cliopatria_shapefile_creation()

      Test the creation of a Cliopatria instance.



   .. py:method:: test_gadm_countries_creation()

      Test the creation of a GADMCountries instance.



   .. py:method:: test_gadm_provinces_creation()

      Test the creation of a GADMProvinces instance.



   .. py:method:: test_gadm_shapefile_creation()

      Test the creation of a GADMShapefile instance.



   .. py:method:: test_get_all_polity_capitals()

      Test the get_all_polity_capitals function.



   .. py:method:: test_get_polity_capitals()

      Test the get_polity_capitals function.



   .. py:method:: test_get_polity_shape_content()

      Test the get_polity_shape_content function.



   .. py:method:: test_get_polity_shape_content_displayed_year_and_seshat_id_both_set()

      Test that a ValueError is raised if both displayed_year and seshat_id are set.



   .. py:method:: test_get_polity_shape_content_no_geometries()

      Test the get_polity_shape_content function with geometries=False.



   .. py:method:: test_get_polity_shape_content_single_seshat_id()

      Test the get_polity_shape_content function for a single polity.
      This gets run for the polity_map view.



   .. py:method:: test_get_polity_shape_content_single_year()

      Test the get_polity_shape_content function for a single year.
      This gets run when loading one year of the world map whilst waiting for the rest of the data to load.



   .. py:method:: test_get_provinces()

      Test the get_provinces function.



   .. py:method:: test_map_view_all()

      Test the map view with all data.



   .. py:method:: test_map_view_initial()

      Test the initial map view which whould redirect to a specific year.



   .. py:method:: test_polity_map()

      Test the polity_map template tag.



   .. py:method:: test_polity_map_no_content()

      Test the polity_map func when polity has no shapes associated.



   .. py:method:: test_polity_map_no_peak_year_set()

      Test the polity_map template tag for a polity that has no peak year set.



   .. py:method:: test_provinces_and_countries_view()

      Test the provinces and countries view.



