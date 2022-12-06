![LUSID_by_Finbourne](https://content.finbourne.com/LUSID_repo.png)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-client-python.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-client-python?ref=badge_shield)

This repository contains examples showing how to make calls to LUSID using the LUSID SDK via a python script or running as tests. These can be found in the `src` folder. 

# API set up

First set up your [API credentials](https://support.finbourne.com/getting-started-with-apis-sdks) (if using a `secrets.json` file place this in the `src` folder) and install the required dependencies via `pip`:

```
$ pip install -r requirements.txt
```

# Script

Run the script using the following command from the `src` folder:

```
$ python scripts/lusid_api.py
```

# Tests

Run the tests with the following command from the `src` folder:

Windows:

```
$ set PYTHONPATH=%PYTHONPATH%;%cd%;%cd%\tests
$ pytest tests\test_connectivity.py -v -rP
```

macOS/linux:

```
$ PYTHONPATH=$(pwd):$(pwd)/tests pytest tests/test_connectivity.py -v -rP
```


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-client-python.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-client-python?ref=badge_large)