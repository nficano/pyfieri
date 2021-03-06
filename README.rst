=======
PyFieri
=======

.. image:: https://img.shields.io/pypi/v/pyfieri.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/pyfieri/

.. image:: https://img.shields.io/pypi/dm/pyfieri.svg
  :alt: Pypi downloads per month
  :target: https://pypi.python.org/pypi/pyfieri/

Description
===========

Spice up that boring Slack channel or HipChat room with PyFieri! PyFieri is an
easy to use Python library that randomly generates Guy Fieri menu items. Some
example include:

- "Jamaican me crazy tuna rolls with kung pao onion rings, $18.75."
- "Nuthin' fancy pastrami quesadilla with volcano mayo, $21."
- "Philly-style applewood bacon fajitas with Santa Rosa-style queso blanco, $17 (lunch only)."
- "Oven roasted elk sliders with roasted garlic onion strips, $48."

Requirements
============

- Python 2.6+ (2.7 or 3.4 recommended)
- PIP (for some installation methods)
- GIT (for some installation methods)

Installation
============

If you are on Mac OS X or Linux, chances are that one of the following two
commands will work for you:

Using PIP via PyPI

.. code:: bash

    pip install pyfieri

Using PIP via Github

.. code:: bash

    pip install git+git://github.com/nficano/pyfieri#egg=pyfieri

Adding to your ``requirements.txt`` file (run ``pip install -r requirements.txt`` afterwards)

.. code:: bash

    git+ssh://git@github.com/nficano/pyfieri#egg=pyfieri

Manually via GIT

.. code:: bash

    git clone git://github.com/NFicano/pyfieri pyfieri
    cd pyfieri
    python setup.py install


Command-Line Usage
==================

.. code:: bash

   $ pyfieri
