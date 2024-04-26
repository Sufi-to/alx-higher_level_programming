#!/usr/bin/python3
"""
Script that takes in a URL and an email and sends a POST request to
the passed URL with an email as a parameter and display response body
"""
if __name__ == "__main__":
    from sys import argv
    import urllib.parse as parse
    import urllib.request
    values = {"email": argv[2]}
    data = parse.urlencode(values).encode("ascii")
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        x = response.read().decode('utf-8')
    print(x)
