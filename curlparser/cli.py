import argparse
import json
import sys

from .core import parse_curl_command

parser = argparse.ArgumentParser()
parser.parse_args()
command = sys.stdin.read()
result = parse_curl_command(command)
print(json.dumps(result))
