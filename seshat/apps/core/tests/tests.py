class ModelTest(TestCase):
    """Test case for the models."""

    def test_video_shapefile_creation(self):
        """Test the creation of a VideoShapefile instance."""
        video_shapefile = VideoShapefile.objects.create(
            geom=square,
            name="Test shape",
            polity="Test polity",
            seshat_id="Test seshat_id",
            area=100.0,
            start_year=2000,
            end_year=2020,
            polity_start_year=2000,
            polity_end_year=2020,
            colour="#FFFFFF"
        )
        self.assertIsInstance(video_shapefile, VideoShapefile)
        self.assertEqual(video_shapefile.name, "Test shape")

    def test_gadm_shapefile_creation(self):
        """Test the creation of a GADMShapefile instance."""
        gadm_shapefile = GADMShapefile.objects.create(
            geom=square,
            UID=123456789,
            NAME_0="Test shape"
        )
        self.assertIsInstance(gadm_shapefile, GADMShapefile)
        self.assertEqual(gadm_shapefile.NAME_0, "Test shape")

    def test_gadm_countries_creation(self):
        """Test the creation of a GADMCountries instance."""
        gadm_countries = GADMCountries.objects.create(
            geom=square,
            COUNTRY="Test Country"
        )
        self.assertIsInstance(gadm_countries, GADMCountries)
        self.assertEqual(gadm_countries.COUNTRY, "Test Country")

    def test_gadm_provinces_creation(self):
        """Test the creation of a GADMProvinces instance."""
        gadm_provinces = GADMProvinces.objects.create(
            geom=square,
            NAME_1="Test Province"
        )
        self.assertIsInstance(gadm_provinces, GADMProvinces)
        self.assertEqual(gadm_provinces.NAME_1, "Test Province")


class ViewTest(TestCase):
    """Test case for the views."""

    def setUp(self):
        """Set up the test client for the views."""
        self.client = Client()

    def test_map_view_initial(self):
        """Test the initial map view."""
        response = self.client.get(reverse('world_map'))
        self.assertEqual(response.status_code, 200)

    def test_map_view_all(self):
        """Test the map view with all data."""
        response = self.client.get(reverse('world_map_all'))
        self.assertEqual(response.status_code, 200)

    def test_provinces_and_countries_view(self):
        """Test the provinces and countries view."""
        response = self.client.get(reverse('provinces_and_countries'))
        self.assertEqual(response.status_code, 200)