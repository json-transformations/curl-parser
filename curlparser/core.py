"""Curl Parser.

Extensable Curl parser; maps commands to request args & kwargs.

Based on https://github.com/spulec/uncurl.
"""
import argparse
import json
import shlex
import sys

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('url')
parser.add_argument('-b', '--data-binary', dest='binary')
parser.add_argument('-d', '--data')
parser.add_argument('-m', '--max-time', dest='maxtime')
parser.add_argument('-u', '--user', dest='auth')
parser.add_argument('-H', '--header', dest='headers', action='append',
                    default=[])
parser.add_argument('-X', '--request', dest='method', default='GET')
parser.add_argument('--connect-timeout', dest='timeout')


def from_json(data):
    try:
        return json.loads(data)
    except ValueError:
        pass


def parse_curl_command(curl_cmd):
    lines = curl_cmd.splitlines()
    curl_cmd = ' '.join(i.rstrip('\ ') for i in lines)
    args = parser.parse_args(shlex.split(curl_cmd))
    headers = (i.split(':', 1) for i in args.headers)
    args.headers = {k: v.strip() for k, v in headers}
    if args.auth:
        args.auth = args.auth.split(':')
    if args.data:
        args.method, args.data = 'post', from_json(args.data)
    if args.timeout:
        args.timeout = (args.timeout, args.maxtime)
    result = vars(args)
    return result


from pprint import pprint
pprint(parse_curl_command(sys.stdin.read()))
