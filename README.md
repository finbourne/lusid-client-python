![LUSID_by_Finbourne](https://content.finbourne.com/LUSID_repo.png)

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
$ python -m unittest discover -v
```

macOS/linux:

```
$ PYTHONPATH=$(pwd):$(pwd)/tests python -m unittest discover -v
```
