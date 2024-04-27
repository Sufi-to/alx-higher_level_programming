#!/usr/bin/python3
""" Script that fetches a URL using requests package"""
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
