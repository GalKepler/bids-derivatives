========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/bids_derivatives/badge/?style=flat
    :target: https://bids_derivatives.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/GalBenZvi/bids_derivatives/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/GalBenZvi/bids_derivatives/actions

.. |requires| image:: https://requires.io/github/GalBenZvi/bids_derivatives/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/GalBenZvi/bids_derivatives/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/GalBenZvi/bids_derivatives/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/GalBenZvi/bids_derivatives

.. |version| image:: https://img.shields.io/pypi/v/bids_derivatives.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/bids_derivatives

.. |wheel| image:: https://img.shields.io/pypi/wheel/bids_derivatives.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/bids_derivatives

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/bids_derivatives.svg
    :alt: Supported versions
    :target: https://pypi.org/project/bids_derivatives

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/bids_derivatives.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/bids_derivatives

.. |commits-since| image:: https://img.shields.io/github/commits-since/GalBenZvi/bids_derivatives/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/GalBenZvi/bids_derivatives/compare/v0.0.0...main



.. end-badges

Python package for querying BIDS Apps` processed derivatives.

* Free software: Apache Software License 2.0

Installation
============

::

    pip install bids_derivatives

You can also install the in-development version with::

    pip install https://github.com/GalBenZvi/bids_derivatives/archive/main.zip


Documentation
=============


https://bids_derivatives.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
