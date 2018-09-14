# -*- coding: utf-8 -*-

from .context import flightradar24

import unittest


class ContractTestSuite(unittest.TestCase):
    """Contact Integration test cases."""

    @staticmethod
    def test_balance_json():
        flightradar24.Api()

    @staticmethod
    def test_balance_json_with_proxy():
        proxies = {'http': 'http://196.43.235.238:53281', 'https': 'https://196.43.235.238:53281'}
        fr = flightradar24.Api(proxies=proxies)
        fr.get_airports()


    @staticmethod
    def test_airports():
        fr = flightradar24.Api()
        airports = fr.get_airports()
        assert airports['rows'] is not None
        assert len(airports['rows']) > 100  # Expect more than 100 airports
        check_jfk = 0
        for airport in airports['rows']:
            if airport['iata'] == "JFK":
                check_jfk = 1
        assert check_jfk == 1

    @staticmethod
    def test_airlines():
        fr = flightradar24.Api()
        airlines = fr.get_airlines()
        assert airlines['rows'] is not None
        assert len(airlines['rows']) > 100  # Expect more than 100 airports
        check_tk = 0
        for airline in airlines['rows']:
            if airline['ICAO'] == "THY":
                check_tk = 1
        assert check_tk == 1


    @staticmethod
    def test_flights():
        fr = flightradar24.Api()
        flights = fr.get_flights('THY')
        assert flights['full_count'] is not None
        assert flights['full_count'] > 100  # Expect more than 100 airports


    @staticmethod
    def test_flight():
        flight_id = 'TK1'
        fr = flightradar24.Api()
        flight = fr.get_flight(flight_id)
        assert flight['result']['response']['data'] is not None
        assert len(flight['result']['response']['data']) > 1  # Expect more than 100 airports
        assert flight['result']['response']['data'][0]['identification']['number']['default'] == flight_id


    @staticmethod
    def test_zones():
        fr = flightradar24.Api()
        zones = fr.get_zones()
        assert zones['europe'] is not None
        check_uk = 0
        for subzone_name, subzone_details in zones['europe']['subzones'].items():
            if subzone_name == 'uk':
                check_uk = 1
        assert check_uk == 1


if __name__ == '__main__':
    unittest.main()
