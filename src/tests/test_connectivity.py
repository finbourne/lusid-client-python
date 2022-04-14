import certifi
import pytest as pytest
import ssl
import urllib3

test_urls = [
    "https://www.howsmyssl.com/a/check",

    #
    #   enable the following url with your specific LUSID client code e.g.
    #   https://myco.lusid.com/api/api/metadata/versions
    #

    # "https://<enter your LUSID client code>.lusid.com/api/api/metadata/versions",
]


def test_cert_store():
    print(certifi.where())


@pytest.mark.parametrize("url", test_urls)
def test_connection(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers={"Accept": "application/json"})

    assert r.status == 200

    print(r.data)


@pytest.mark.parametrize("url", test_urls)
def test_connection_no_ssl_verification(url):
    http = urllib3.PoolManager(cert_reqs='CERT_NONE')
    r = http.request('GET', url, headers={"Accept": "application/json"})

    assert r.status == 200

    print(r.data)


@pytest.mark.parametrize("url", test_urls)
def test_connection_with_proxy(url):
    proxy_url = "http://127.0.0.1:8888"
    proxy_user = "user"
    proxy_password = "password"
    # proxy_user = None
    # proxy_password = None

    proxy_headers = urllib3.util.make_headers(proxy_basic_auth=f"{proxy_user}:{proxy_password}") if proxy_user is not None or proxy_password is not None else None
    http = urllib3.ProxyManager(
        proxy_url=proxy_url,
        proxy_headers=proxy_headers
    )

    r = http.request('GET', url, headers={"Accept": "application/json"})

    assert r.status == 200

    print(r.data)


@pytest.mark.parametrize("url", test_urls)
def test_connection_with_proxy_no_ssl_verification(url):

    proxy_url = "http://127.0.0.1:8888"
    proxy_user = "user"
    proxy_password = "password"
    # proxy_user = None
    # proxy_password = None

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    proxy_headers = urllib3.util.make_headers(proxy_basic_auth=f"{proxy_user}:{proxy_password}") if proxy_user is not None or proxy_password is not None else None

    http = urllib3.ProxyManager(
        proxy_url=proxy_url,
        proxy_headers=proxy_headers,
        proxy_ssl_context=ctx
    )

    r = http.request('GET', url, headers={"Accept": "application/json"})

    assert r.status == 200

    print(r.data)
