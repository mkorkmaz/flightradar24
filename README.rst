flightradar24.py
===============

|Travis|_ |Codacy|_

.. |Travis| image:: https://api.travis-ci.org/mkorkmaz/flightradar24.svg?branch=master
.. _Travis: https://api.travis-ci.org/mkorkmaz/flightradar24

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/8c51d54a63c44c88839d07f61848df6d
.. _Codacy: https://www.codacy.com/app/mehmet/flightradar24/

Data library for Flightadar24.com written in Python 3.


Installing flightradar24.py
=====================

.. code-block:: bash

    pip3 install flightradar24


Getting airports list

.. code-block:: python

    import flightradar24
    fr = flightradar24.Api()
    airlines = fr.get_airports()

Getting airlines list

.. code-block:: python

    import flightradar24
    fr = flightradar24.Api()
    airlines = fr.get_airlines()

Getting flights list

.. code-block:: python

    import flightradar24
    airline = 'THY' # Turkish Airlines
    fr = flightradar24.Api()
    flights = fr.get_flights(airline)


Getting flight details

.. code-block:: python

    import flightradar24
    flight_id = 'TK1' # Turkish Airlines' Istanbul - New York flight
    fr = flightradar24.Api()
    flight = fr.get_flight(flight_id)


Notes
=====

* flightradar24.py will not follow the `semantic versioning scheme <http://semver.org/>`_ until the version 1.0.0. So there may be BC breaks.


Credits
=======

* `Mehmet Korkmaz <http://github.com/mkorkmaz>`_


