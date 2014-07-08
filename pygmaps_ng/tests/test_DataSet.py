import unittest
import pygmaps_ng

"""
Unit tests for the DataSet class.
"""


class DataSetTests(unittest.TestCase):
    def setUp(self):
        self.ds = pygmaps_ng.DataSet('test')

    def test_create_dataset_with_id(self):
        self.assertEqual(self.ds.id, 'test')
        self.assertEqual(self.ds.title, 'No Title')

    def test_create_dataset_with_title(self):
        data_set = pygmaps_ng.DataSet('test', 'Test Title')
        self.assertEqual(data_set.id, 'test')
        self.assertEqual(data_set.title, 'Test Title')

    def test_add_marker(self):
        self.ds.add_marker((40.123456, -100.654321),
                           color='#FF0000',
                           title='Test Marker',
                           text="This is only a test.")
        self.assertEqual(len(self.ds.markers), 1)
        # Note, lat and lng are converted to strings when they're stored
        self.assertEqual(self.ds.markers[0]['lat'], '40.123456')
        self.assertEqual(self.ds.markers[0]['lon'], '-100.654321')
        # Leading "#" gets stripped from color
        self.assertEqual(self.ds.markers[0]['color'], 'FF0000')
        self.assertEqual(self.ds.markers[0]['title'], 'Test Marker')
        self.assertEqual(self.ds.markers[0]['text'], 'This is only a test.')

    def test_add_marker_bad_value(self):
        self.assertRaises(ValueError, self.ds.add_marker, ('this', 'is bad'))

    def test_add_line(self):
        self.ds.add_line([(0, 0), (1, 1)], "#FF0000")
        self.assertEqual(len(self.ds.lines), 1)
        self.assertEqual(self.ds.lines[0]['color'], "#FF0000")

    def test_add_line_bad_value(self):
        pass

    def test_add_polygon(self):
        pass

    def test_add_polygon_bad_value(self):
        pass

    def test_data(self):
        pass

if __name__ == '__main__':
    unittest.main()
