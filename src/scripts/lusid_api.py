import sys
from pathlib import Path

from lusid import ScopesApi
from lusid.utilities import ApiClientFactory


def main(argv):

    #   create an ApiFactory configured with the api credentials
    secrets_file = Path(__file__).parent.parent.joinpath('secrets.json')
    api_factory = ApiClientFactory(api_secrets_filename=secrets_file)

    #   create an api and call a function on it
    scopes_api = api_factory.build(ScopesApi)
    scopes = scopes_api.list_scopes()

    for scope in scopes.values:
        print(scope)


if __name__ == "__main__":
    main(sys.argv)
