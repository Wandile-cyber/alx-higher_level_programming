#!/usr/bin/python3
# Python script that fetches a url
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print("Body response:")
    print(f"\t- type: {type(response.read())}")
    print(f"\t- content: {response.read()}")
    print(f"\t- utf8 content: {response.read().decode()}")
