#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests


def api_request(end_point):
    request_base_headers = {'User-agent': 'mkorkmaz/FR24/1.0'}
    r = requests.get(end_point, headers=request_base_headers)
    if r.status_code is 403:
        raise RuntimeError("Request to " + end_point + " is Forbidden")
    if r.status_code is 404:
        raise RuntimeError("Request to " + end_point + " is NotFound")
    if r.status_code is 404:
        raise RuntimeError("Request to " + end_point + " returns InternalServerError")
    return r.json()
