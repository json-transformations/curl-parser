"""
string w/ no leading dashes: argument

when building check to see if the name is a keyword or built-in
"""
MULTIPLE = {'action': 'append'}

CURL_PARAMETERS = [
    'command',
    'url',
    'anyauth',
    ('-a', '--append'),
    '--basic',
    '--cacert',
    '--capath',
    ('-E', '--cert'),
    '--cert-status',
    ('--cert-type'),
    '--ciphers',
    '--compressed',
    ('-K', '--config'),
    '--connect-timeout',
    '--connect-to',
    ('-C', '--continue-at'),
    ('-b', '--cookie'),
    ('-c', '--cookie-jar'),
    '--create-dirs',
    '--crlf',
    '--crlfile',
    ('-d', '--data'),
    '--data-raw',
    '--data-ascii',
    '--data-binary',
    '--data-urlencode',
    '--delegation',
    '--digest',
    '--disable-eprt',
    '--disable-epsv',
    '--dns-servers',
    '--dns-interface',
    '--dns-ipv4-addr',
    '--dns-ipv6-addr',
    ('-D', '--dump-header'),
    '--egd-file',
    '--engine',
    '--expect100-timeout',
    ('-f', '--fail'),
    '--false-start',
    ('-F', '--form'),
    '--form-string',
    '--ftp-account',
    '--ftp-alternative-to-user',
    '--ftp-create-dirs',
    '--ftp-method',
    '--ftp-pasv',
    ('-P', '--ftp-port'),
    '--ftp-skip-pasv-ip',
    '--ftp-pret',
    '--ftp-ssl-ccc',
    '--ftp-ssl-ccc-mode',
    '--ftp-ssl-control',
    ('-G', '--get'),
    ('-g', '--globoff'),
    ('-H', '--header', MULTIPLE),
    ('-I', '--head'),
    ('-h', '--help'),
    '--hostpubmd5',
    ('-0', '--http1.0'),
    '--http1.1',
    '--http2',
    '--http2-prior-knowledge',
    '--ignore-content-length',
    ('-i', '--include'),
    ('-k', '--insecure'),
    '--interface',
    ('-4', '--ipv4'),
    ('-6', '--ipv6'),
    ('-j', '--junk-session-cookies'),
    '--keepalive-time',
    '--key'
    '--key-type'
    '--krb'
    '--libcurl'
    '--limit-rate'
    ('-l', '--list-only'),
    '--local-port'
    ('-L', '--location'),
    '--location-trusted'
    '--login-options'
    ('-M', '--manual'),
    '--mail-from',
    '--mail-rcpt',
    '--mail-auth'
    '--max-filesize'
    '--max-redirs'
    ('-m, --max-time'),
    '--metalink'
    '--negotiate'
    ('-n, --netrc'),
    '--netrc-optional',
    '--netrc-file',
    ('-:', '--next'),
    '--no-alpn',
    ('-N', '--no-buffer'),
    '--no-keepalive',
    '--no-npn',
    '--no-sessionid',
    '--noproxy',
    '--ntlm',
    '--ntlm-wb',
    '--oauth2-bearer',
    ('-o', '--output'),
    '--pass',
    '--path-as-is',
    '--pinnedpubkey',
    '--post301',
    '--post302',
    '--post303',
    ('-#', '--progress-bar'),
    '--proto',
    '--proto-default',
    '--proto-redir',
    ('-x', '--proxy'),
    '--proxy-anyauth',
    '--proxy-basic',
    '--proxy-digest',
    '--proxy-negotiate',
    '--proxy-ntlm',
    '--proxy-header',
    '--proxy-service-name',
    '--service-name',
    ('-U', '--proxy-user'),
    '--proxy1.0',
    ('-p', '--proxytunnel'),
    '--pubkey KEY',
    ('-Q', '--quote CMD'),
    '--random-file',
    ('-r', '--range'),
    '--raw',
    ('-e', '--referer'),
    ('-J', '--remote-header-name'),
    ('-O', '--remote-name'),
    '--remote-name-all',
    ('-R', '--remote-time'),
    ('-X', '--request'),
    '--resolve',
    '--retry',
    '--retry-delay',
    '--retry-max-time',
    '--sasl-ir',
    ('-S', '--show-error'),
    ('-s', '--silent'),
    '--socks4',
    '--socks4a',
    '--socks5',
    '--socks5-hostname',
    '--socks5-gssapi-service',
    '--socks5-gssapi-nec',
    ('-Y', '--speed-limit'),
    ('-y', '--speed-time'),
    '--ssl',
    '--ssl-reqd',
    ('-2', '--sslv2'),
    ('-3', '--sslv3'),
    '--ssl-allow-beast',
    '--ssl-no-revoke',
    '--stderr',
    '--tcp-nodelay',
    '--tcp-fastopen',
    ('-t', '--telnet-option'),
    '--tftp-blksize',
    '--tftp-no-options',
    ('-z', '--time-cond'),
    ('-1', '--tlsv1'),
    '--tlsv1.0',
    '--tlsv1.1',
    '--tlsv1.2',
    '--trace',
    '--trace-ascii',
    '--trace-time',
    '--tr-encoding',
    ('-T', '--upload-file'),
    '--url',
    ('-B', '--use-ascii'),
    ('-u', '--user'),
    '--tlsuser',
    '--tlspassword',
    '--tlsauthtype',
    '--unix-socket',
    ('-A', '--user-agent'),
    ('-v', '--verbose'),
    ('-V', '--version'),
    ('-w', '--write-out'),
    '--xattr',
    ('-q', '--disable')
]
