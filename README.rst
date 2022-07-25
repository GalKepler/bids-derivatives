========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - Documentation
      - |docs|
    * - Code
      - | |made-with-python| |code-style| |imports|
        | |pre-commit|
    * - Tests
      - | |github-actions| |requires|
        | |codecov| |code-quality| |python-quality|
    * - Packaging
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/bids_derivatives/badge/?style=flat
    :target: https://bids_derivatives.readthedocs.io/
    :alt: Documentation Status

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with%20Python-v3.9-blue.svg?style=flat
    :target: https://www.python.org/
    :alt: Made with Python

.. |code-style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code style

.. |imports| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: Imports

.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://pre-commit.com/
    :alt: Pre-commit

.. |code-quality| image:: https://app.codacy.com/project/badge/Grade/660ff8ebe55d4ecbaa043bc5216a1d30
    :target: https://lgtm.com/projects/g/GalBenZvi/bids-derivatives/context:python
    :alt: Code quality: Python

.. |python-quality| image:: https://img.shields.io/lgtm/grade/python/g/GalBenZvi/bids-derivatives.svg
    :target: https://www.codacy.com/gh/GalBenZvi/bids-derivatives/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=GalBenZvi/bids-derivatives&amp;utm_campaign=Badge_Grade
    :alt: Code quality

.. |github-actions| image:: https://github.com/GalBenZvi/bids-derivatives/actions/workflows/github-workflow.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/GalBenZvi/bids-derivatives/actions

.. |requires| image:: https://requires.io/github/GalBenZvi/bids-derivatives/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/GalBenZvi/bids-derivatives/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/GalBenZvi/bids-derivatives/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/GalBenZvi/bids-derivatives

.. |version| image:: https://badge.fury.io/py/bids-derivatives.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/bids-derivatives

.. |wheel| image:: https://img.shields.io/pypi/wheel/bids-derivatives.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/bids-derivatives

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/bids-derivatives.svg
    :alt: Supported versions
    :target: https://pypi.org/project/bids-derivatives

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/bids-derivatives.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/bids-derivatives

.. |commits-since| image:: https://img.shields.io/github/commits-since/GalBenZvi/bids-derivatives/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/GalBenZvi/bids-derivatives/compare/v0.0.1...main



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
