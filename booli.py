import requests
import dotenv
import time
import random
import string
import hashlib
import os
import json

from os.path import join, dirname
from dotenv import load_dotenv

import urllib.parse as urlparse
from urllib.parse import urlencode

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Booli:
    def __init__(self):
        self.url = 'https://api.booli.se/sold'

    def __get_sold__(self, area):
        timestamp = str(int(time.time()))
        unique = ''.join(random.choice('abcdefgijklnopqrstuvwxyz1234567890') for i in range(16))
        string_to_hash = str(os.environ.get('callerId') + timestamp + os.environ.get('key') + unique).encode('utf-8')
        hash_string = hashlib.sha1(string_to_hash)
        params = {
            'q': area,
            'key': os.environ.get('key'),
            'callerId': os.environ.get('callerId'), 'time': timestamp,
            'unique': unique, 'hash': hash_string.hexdigest()}
        url_parts = list(urlparse.urlparse(self.url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)

        url_parts[4] = urlencode(query)
        r = requests.get(urlparse.urlunparse(url_parts))
        sold_apartments = json.loads(r.content.decode('utf-8'))
        pass

    def train(self, area):
        sold_list = self.__get_sold__(area)
        pass

    def predict(self, house):
        pass
