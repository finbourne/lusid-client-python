import unittest

from lusid import ScopesApi
from lusid.utilities import ApiClientFactory
import lusid.models as models
from pathlib import Path

class ApiExample(unittest.TestCase):

    def test_api(self):

        #   create an ApiFactory configured with the api credentials
        secrets_file = Path(__file__).parent.parent.joinpath('secrets.json')
        api_factory = ApiClientFactory(api_secrets_filename=secrets_file)

        #   create an api and call a function on it
        scopes_api = api_factory.build(ScopesApi)
        scopes = scopes_api.list_scopes()

        #   verify the call was successful
        self.assertGreater(len(scopes.values), 0)
