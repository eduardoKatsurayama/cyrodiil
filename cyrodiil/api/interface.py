from __future__ import annotations

from abc import ABC
import os
import ast

import requests

from cyrodiil.utils.constants import PLATFORM, REGIONS


class ApiRequester(ABC):
    def __init__(self, region, by_platform=True):
        self.url = f'https://{PLATFORM[region]}' \
            if by_platform else f'https://{REGIONS[region]}'

    def _get_endpoint(self, uri, kwargs):
        for key, value in kwargs.items():
            uri = uri.replace('{'+key+'}', str(value))
        return self.url + uri

    def _request(self, uri, **kwargs):
        endpoint = self._get_endpoint(uri, kwargs)
        response = requests.get(
            endpoint, headers=ast.literal_eval('{'+os.getenv('HEADERS')+'}')
        )
        
        return response.text
