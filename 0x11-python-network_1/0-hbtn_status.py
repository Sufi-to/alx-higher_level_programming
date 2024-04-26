#!/usr/bin/python3
"""
Script that fetches a url and display the results in a given
format
"""
if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        print("Body response:")
        print(f"\t- type: {type(response.read())}")
        content = response.read()
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {response.msg}")
