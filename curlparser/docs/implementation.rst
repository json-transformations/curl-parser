method
    method for the new :class:`Request` object.

url
    URL for the new :class:`Request` object.

params
    (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.

data
    (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes, or file-like object to send
    in the body of the :class:`Request`.

json
    (optional) json data to send in the body of the :class:`Request`.

headers
    (optional) Dictionary of HTTP Headers to send with the :class:`Request`.

cookies
    (optional) Dict or CookieJar object to send with the :class:`Request`.

files
    (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
    ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
    or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
    defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
    to add for the file.

auth
    (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.

timeout
    (optional) How many seconds to wait for the server to send data
    before giving up, as a float, or a :ref:`(connect timeout, read
    timeout) <timeouts>` tuple.

allow_redirects
    (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool

proxies:
    (optional) Dictionary mapping protocol to the URL of the proxy.

verify
    (optional) Either a boolean, in which case it controls whether we verify
    the server's TLS certificate, or a string, in which case it must be a path
    to a CA bundle to use. Defaults to ``True``.

stream
    (optional) if ``False``, the response content will be immediately downloaded.

cert
    (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.