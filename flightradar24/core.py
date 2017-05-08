#!/usr/bin/python3
# -*- coding: utf-8 -*-
from .helpers import *
import time

class Api:
    """Flight Radar 24 API"""

    balanceJsonUrl = 'https://www.flightradar24.com/balance.json'
    balanceUrl = None
    baseUrl = 'https://www.flightradar24.com'
    apiUrl = 'https://api.flightradar24.com/common/v1'
    liveDataUrl = 'https://data-live.flightradar24.com'

    metaDataEndPoints = {
        'airports': '/_json/airports.php',
        'airlines': '/_json/airlines.php',
        'zones': '/js/zones.js.php'
    }

    realTimeDataEndPoints = {
        'flight': '/flight/list.json?&fetchBy=flight&page=1&limit=25&query=',  # add flight number e.g: TK1
        'flights': '/zones/fcgi/feed.js?airline=!'
    }

    def __init__(self):
        response = api_request(self.balanceJsonUrl)
        tmp_weight = 0
        tmp_uri = None
        for uri, weight in response.items():
            if weight > tmp_weight:
                tmp_uri = uri
                tmp_weight = weight
        self.balanceUrl = tmp_uri

    def get_airports(self):
        return api_request(self.baseUrl + self.metaDataEndPoints['airports'])

    def get_airlines(self):
        return api_request(self.baseUrl + self.metaDataEndPoints['airlines'])

    def get_flights(self, airline):
        endpoint = self.liveDataUrl + self.realTimeDataEndPoints['flights']+airline+'&_='+str(time.time())
        return api_request(endpoint)

    def get_flight(self, flight_id):
        endpoint = self.apiUrl + self.realTimeDataEndPoints['flight']+flight_id
        return api_request(endpoint)
    def get_zones(self):
        return api_request(self.baseUrl + self.metaDataEndPoints['zones'])

