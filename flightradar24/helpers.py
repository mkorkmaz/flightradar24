# -*- coding: utf-8 -*-

import requests


def api_request(end_point, proxies=None):
    request_base_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "accept": "application/jsoN",
        "accept-language": "en-EN",
        "cache-control": "max-age=0",
        "origin": "https://www.flightradar24.com",
        "referer": "https://www.flightradar24.com/"

    }
    r = requests.get(end_point, headers=request_base_headers, proxies=proxies)
    print(end_point, r.headers, r.text)
    if r.status_code is 402:
        raise RuntimeError("Request to " + end_point + " requires payment")
    if r.status_code is 403:
        raise RuntimeError("Request to " + end_point + " is Forbidden")
    if r.status_code is 404:
        raise RuntimeError("Request to " + end_point + " is NotFound")
    if r.status_code is 500:
        raise RuntimeError("Request to " + end_point + " returns InternalServerError")
    return r.json()
