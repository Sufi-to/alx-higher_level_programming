#!/usr/bin/python3
"""
script that takes my github credentials and uses the Github
API to display my id
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth
    itsme = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=itsme)
    print(res.json().get("id"))
