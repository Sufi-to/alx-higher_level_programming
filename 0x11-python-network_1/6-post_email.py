#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a Post request
to the passed URL with the email as a parameter and display body
of response
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
