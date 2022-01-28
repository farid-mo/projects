# -*- coding: utf-8 -*-
"""
Checks if the password(s) passed in the command line
has/have been hacked so far.

Created on Wed Jan 26 20:26:46 2022

@author: Farid
"""
import requests
import hashlib
import sys


def request_api_data(querry_char):
    url = 'https://api.pwnedpasswords.com/range/' + querry_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code},'
                           ' check the api and try again!')
    return res


def get_password_eak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check if password exist in api
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    sha1password = sha1password.upper()

    # Select first 5 char
    first5_char, tail = sha1password[:5], sha1password[5:]

    # Request api
    response = request_api_data(first5_char)

    return get_password_eak_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        # Print output
        if count:
            print(f'{password} was found {count} times...'
                  'you may change your password!')
        else:
            print(f'{password} was not found...Carry on!')
    return 'Done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
