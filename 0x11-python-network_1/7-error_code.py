#!/usr/bin/python3
"""
script that takes in a URL and send a request to the URL and displays
the body of the response
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.get(argv[1])
    if r.status_code == 200:
        print(r.text)
    else:
        print(f"Error code: {r.status_code}")
