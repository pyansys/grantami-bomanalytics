ansys-grantami-bomanalytics
###########################

Project Overview
----------------
This project is part of the larger PyAnsys effort to facilitate the use
of Ansys technologies directly from within Python.

The Granta MI Restricted Substances solution includes a REST API for
evaluating compliance of products, assemblies, specifications and
materials against legislations. This package abstracts automatically-
generated code into an easy-to-use client library.


Installation
------------
Install ansys-grantami-bomanalytics with:

.. code::

   pip install ansys-grantami-bomanalytics

Alternatively, clone and install with:

.. code::

   git clone https://github.com/pyansys/grantami-bomanalytics
   cd grantami-bomanalytics
   pip install .


Documentation
-------------
See `Granta MI BoM Analytics Documentation <https://grantami.docs.pyansys.com>`_
for more details.


Usage
-----
Here's a brief example of how the package works:

.. code:: python

    # Connect and query the Granta service.

    >>> from pprint import pprint
    >>> from ansys.grantami.bomanalytics import Connection, queries
    >>> cxn = Connection("http://my_grantami_server/mi_servicelayer").with_autologon().connect()
    >>> query = (
    ...     queries.MaterialImpactedSubstancesQuery()
    ...     .with_material_ids(['plastic-abs-pvc-flame'])
    ...     .with_legislations(['REACH - The Candidate List'])
    ... )

    # Print out the result from the query.

    >>> result = cxn.run(query)
    >>> pprint(result.impacted_substances)
    [<ImpactedSubstance: {"cas_number": 10108-64-2, "percent_amount": 1.9}>,
     <ImpactedSubstance: {"cas_number": 107-06-2, "percent_amount": None}>,
     <ImpactedSubstance: {"cas_number": 115-96-8, "percent_amount": 15.0}>,
    ...


Testing
-------
See `Contributing <https://grantami.docs.pyansys.com/contributing>`_
for more details.


License
-------
The library is provided under the terms of the MIT license, you can find
the license text in the LICENSE file at the root of the repository.
