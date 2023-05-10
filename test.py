import unittest
from EasyBroker import EasyBrokerAPI


class TestEasyBrokerAPIReader(unittest.TestCase):

    def test_read_properties(self):
        # Instantiate EasyBrokerAPIReader with API credentials
        api_reader = EasyBrokerAPI("l7u502p8v46ba3ppgvj5y2aad50lb9")

        # Call read_properties method to get list of properties
        properties, titles = api_reader.get_properties()

        # Assert that the properties list is not empty
        self.assertGreater(len(properties), 0)


if __name__ == '__main__':
    unittest.main()
