Flight Radar 24
===============

Data library for Flight Radar 24 written in Python 3.


Installing flightradar24
=====================

.. code-block:: bash

    pip3 install flightradar24


Getting airports list

.. code-block:: python

    import flightradar24
    fr = flightradar24.Api()
    airlines = fr.get_airports()

Getting airlines

.. code-block:: python

    import flightradar24
    fr = flightradar24.Api()
    airlines = fr.get_airlines()

Getting flights list

.. code-block:: python

    import flightradar24
    fr = flightradar24.Api()
    flights = fr.get_flights('THY')


Getting flight details

.. code-block:: python

    import flightradar24
    flight_id = 'TK1'
    fr = flightradar24.Api()
    flight = fr.get_flight(flight_id)


Notes
=====

* flightradar24 will not follow the `semantic versioning scheme <http://semver.org/>`_ until the version 1.0.0. So there may be BC breaks.


Credits
=======

* `Mehmet Korkmaz <http://github.com/mkorkmaz>`_


