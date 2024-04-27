#!/usr/bin/python3
"""
Script that fetches a url and display the results in a given
format
"""
if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print("Body response:")
        print(f"\t- type: {type(res)}")
        print(f"\t- content: {res}")
        print(f"\t- utf8 content: {res.decode('utf-8')}")
