#!/usr/bin/python3
"""this script takes 2 arguments to solve this challenge:
Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
The first argument will be the repository name
The second argument will be the owner name"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'\
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print('{}: {}'.format(sha, author_name))
