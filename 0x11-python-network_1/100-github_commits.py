#!/usr/bin/python3
"""
script that takes 2 arguments and print
the last 10 commits of a github rep
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    owner = argv[2]
    repo = argv[1]
    res = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(owner, repo))
    results = res.json()
    i = 0
    for result in results:
        if i < 10:
            print("{}: {}".format(
                result.get("sha"),
                result.get("commit").get("author").get("name")))
            i += 1
