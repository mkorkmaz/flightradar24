flightradar24.py
================


[![Travis](https://api.travis-ci.org/mkorkmaz/flightradar24.svg?branch=master)](https://travis-ci.org/mkorkmaz/flightradar24)
[![Codacy](https://api.codacy.com/project/badge/Grade/8c51d54a63c44c88839d07f61848df6d)](https://www.codacy.com/app/mehmet/flightradar24/) [![Coveralls](https://coveralls.io/repos/github/mkorkmaz/flightradar24/badge.svg?branch=master)](https://coveralls.io/github/mkorkmaz/flightradar24?branch=master) [![Scrutinizer](https://scrutinizer-ci.com/g/mkorkmaz/flightradar24/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/mkorkmaz/flightradar24/?branch=master)

Data library for Flightadar24.com written in Python 3.

If you want to use  the data collected using this library commercially, You need to subscribe to Business Plan. See details at  `https://www.flightradar24.com/premium/ <https://www.flightradar24.com/premium/>`_


Installing flightradar24.py
===========================

```bash
pip3 install flightradar24
````

Getting airports list

```python
import flightradar24
fr = flightradar24.Api()
airports = fr.get_airports()
```

Getting airlines list

```python
import flightradar24
fr = flightradar24.Api()
airlines = fr.get_airlines()
```

Getting flights list

```python
import flightradar24
airline = 'THY' # Turkish Airlines
fr = flightradar24.Api()
flights = fr.get_flights(airline)
```

Getting flight details

```python
import flightradar24
flight_id = 'TK1' # Turkish Airlines' Istanbul - New York flight
fr = flightradar24.Api()
flight = fr.get_flight(flight_id)
```

Notes
=====

* flightradar24.py will not follow the `semantic versioning scheme <http://semver.org/>`_ until the version 1.0.0. So there may be BC breaks.


Credits
=======

* `Mehmet Korkmaz <http://github.com/mkorkmaz>`_


