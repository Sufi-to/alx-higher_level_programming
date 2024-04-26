#!/usr/bin/python3
"""Script that sends a request to a URL and displays that value
of the "X-Request-Id"
"""
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        x = response.info()['X-Request-Id']
    print(x)
