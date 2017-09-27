# x = RequestsParameters.from_curl


def get_method(*curl_args, **curl_kwargs):
    return request or


def get_auth(*curl_args, **curl_kwargs):
    pass


def get_cert(*curl_args, **curl_kwargs):
    pass


def get_cookies(*curl_args, **curl_kwargs):
    pass


def get_data(*curl_args, **curl_kwargs):
    pass


def get_files(*curl_args, **curl_kwargs):
    pass


def get_headers(*curl_args, **curl_kwargs):
    pass


def get_params(*curl_args, **curl_kwargs):
    pass


def get_proxies(*curl_args, **curl_kwargs):
    pass


def get_timeout(*curl_args, **curl_kwargs):
    pass


def get_verify(*curl_args, **curl_kwargs):
    pass


REQUEST_PARAMETERS = [
    ('method', 'request')
    ('url', 'url')
    ('allow_redirects', 'location')
    ('auth', get_auth)
    ('cert', get_cert)
    ('cookies', get_cookies)
    ('data', get_data)
    ('files', get_files)
    ('headers', get_headers)
    ('json', None)
    ('params', get_params)
    ('proxies', get_proxies)
    ('stream', None)
    ('timeout', get_timeout)
    ('verify', get_verify)
]
