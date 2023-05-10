import unittest
from EasyBroker import EasyBrokerAPI
from test import TestEasyBrokerAPIReader

if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEasyBrokerAPIReader)

    # Run the test suite
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # If all tests pass, call the main function to run the API
    if result.wasSuccessful():

        # If all tests pass, call the EasyBrokerAPIReader to read properties
        api_key = "l7u502p8v46ba3ppgvj5y2aad50lb9"
        eb_api = EasyBrokerAPI(api_key)
        properties, titles = eb_api.get_properties()
        for x, prop in enumerate(properties):
            print("Titles from user: ", x+1)
            for title in titles:
                print(title, ": ", prop[title])
            print()

    else:
        print("Tests failed, please fix them before running the API")
