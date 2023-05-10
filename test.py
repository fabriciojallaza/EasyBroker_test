import unittest
from EasyBroker import EasyBrokerAPI


class TestEasyBrokerAPI(unittest.TestCase):
    # Test case for successful API request
    def test_get_properties_success(self):
        # Instantiate EasyBrokerAPI with valid access token
        api = EasyBrokerAPI(access_token="l7u502p8v46ba3ppgvj5y2aad50lb9")

        # Call get_properties method
        properties, keys = api.get_properties()

        # Assert that the properties list is not empty
        self.assertGreater(len(properties), 0)

        # Assert that each property has at least one key
        for property in properties:
            self.assertGreater(len(property), 0)

    # Test case for failed API request
    def test_get_properties_failure(self):
        # Instantiate EasyBrokerAPI with invalid access token
        api = EasyBrokerAPI(access_token="123456789")

        # Call get_properties method
        properties, keys = api.get_properties()

        # Assert that the properties list is empty
        self.assertEqual(len(properties), 0)


if __name__ == '__main__':
    unittest.main()
