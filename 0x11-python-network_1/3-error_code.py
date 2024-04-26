#!/usr/bin/python3
"""
script that takes a URL and sends a request to the URL and display
the body of the response(decoded in utf-8)
"""
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.status}")
