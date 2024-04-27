#!/usr/bin/python3
"""
script that takes in a letter and sends a post request to
a URL with a letter as a parameter
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) >= 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
