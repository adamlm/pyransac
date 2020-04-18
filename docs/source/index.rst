.. pyransac documentation master file, created by
   sphinx-quickstart on Thu Apr 16 22:23:31 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Overview
========
``pyransac`` is a general-purpose random sample consensus (RANSAC) framework
written in Python. You can use it to remove outliers from your data sets
given a data model to which you expect your data to fit. For convenience, some
data models (such as a 2D straight line) are already provided. However, you are
free to define your own data models.

Installation
============
You can install ``pyransac`` using ``pip`` with the following command:

.. code-block:: shell

    $ python3 -m pip install pyransac



Getting Started
===============
After installing ``pyransac``, all you need to do is create a data model
definition (or use one of the built in models) and specify the RANSAC
algorithm parameters. From there you can call the ``find_inliers`` function
and pass in your data, model, and parameters. The function will return a list
of your inliers.

Example Program
===============
The following is a simple example of filtering data against a 2D line
model.

.. code-block:: python
   :linenos:

   import pyransac
   from pyransac import line2d

   # Create data
   inliers = [line2d.Point2D(x, x) for x in range(0, 10)]
   outliers = [line2d.Point2D(x ** 2, x + 10) for x in range(0, 5)]
   data = inliers + outliers

   # Specify our RANSAC parameters
   params = pyransac.RansacParams(samples=2,
                                  iterations=10,
                                  confidence=0.999,
                                  threshold=1)

   # Create our model object
   model = line2d.Line2D()

   # Get the inliers
   inliers = pyransac.find_inliers(points=data,
                                   model=model,
                                   params=params)

   # Compare the data sets
   print(data)
   print(inliers)

Custom Data Models
==================
All data models are derived from the ``Model`` base class. This class defines
an interface consisting of two functions: ``make_model`` and ``calc_error``.
The ``make_model`` function generates a data model from a set of data points.
The ``calc_error`` function calculates the error between a data point and the
generated model. See the ``Model`` :ref:`reference <Model>` for more
information.

You can define custom data models by extending the ``Model`` class.
``pyransac`` provides the following built-in data models:

- :ref:`Line2D <Line2D>` --- a 2-dimensional line model

Table of Contents
=================
.. toctree::
   :maxdepth: 2

   reference

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
