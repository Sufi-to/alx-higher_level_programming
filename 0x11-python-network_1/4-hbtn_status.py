#!/usr/bin/python3
""" Script that fetches a URL using requests package"""
if __name__ == "__main__":
    import requests
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.reason}")

