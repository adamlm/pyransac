![](https://github.com/MeelonUsk/pyransac/workflows/Continuous%20Integration/badge.svg)
[![codecov](https://codecov.io/gh/MeelonUsk/pyransac/branch/master/graph/badge.svg)](https://codecov.io/gh/MeelonUsk/pyransac)
[![Documentation Status](https://readthedocs.org/projects/pyransac/badge/?version=latest)](https://pyransac.readthedocs.io/en/latest/?badge=latest)

# `pyransac` package
This package is a general random sample consensus (RANSAC) framework. For
convenience, some data models (such as a straight line) are already provided.
However, you are free to define your own data models to remove outliers from
arbitrary data sets using arbitrary data models.

# General usage
There are two main components to this package: the RANSAC estimator and a
data model. When calling the estimation function `find_inliers`, you need to
specify the model to which you expect your data to fit.

A data model is class containing the model parameters and an error function 
against which you can test your data. Each data model must implement the
interface defined by the `Model` base class. In other words, you need to
implement the `make_model` and `calc_error` functions.

Additionally, you need to provide parameters for the RANSAC algorithm. These 
parameters are contained in the `RansacParams` class.