========================
sphinxcontrib-prefectviz
========================

|badge:pypi-version| |badge:py-versions| |badge:black|

.. |badge:pypi-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-prefectviz.svg
   :target: https://pypi.org/project/sphinxcontrib-prefectviz
   :alt: [Latest PyPI version]
.. |badge:py-versions| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-scm.svg
   :target: https://pypi.org/project/sphinxcontrib-scm
   :alt: [Supported Python versions]
.. |badge:black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: [Code style: black]

An extension to add Prefect flow visualizations into you Sphinx documentation.

Overview
--------

This Sphinx extension allows you to add your prefect flow visualization into your Sphinx documentation using a single directive.

Installation
------------

The best way to install this extension is to install it via PyPi:

.. code-block:: shell

   pip install sphinxcontrib-prefectviz


Configuration
-------------

Add :code:`'sphinxcontrib.prefectviz'` to the extensions list in :code:`conf.py`.

.. code-block:: python

   extensions = [ 'sphinxcontrib.prefectviz' ]


Usage
-----

Use the following directive to add a flow visualization into your documentation.

.. code-block:: rst

    .. flowviz:: module.submodule.flow

Long story
**********

First of all, make sure that your prefect flow(s) can be imported by your Sphinx project.

In our case, we have to comment-in the following LOC in the top of :code:`conf.py`:

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('.'))

Let's start with the following example, our prefect flow is in the same directory with the Sphinx project:

.. code-block::

    docs
    ├── _build
    ├── conf.py
    ├── index.rst
    ├── make.bat
    ├── Makefile
    ├── _static
    ├── _templates
    └── flow.py

and the :code:`flow.py` looks like:

.. code-block:: python

    from prefect import task, Flow

    @task
    def hello_world():
        print("Hello world")

    with Flow(name="foo") as flow:
        hello_world()

Finally, add the flow visualization using the following directive:

.. code-block::

    .. flowviz:: flow.flow


Links
-----

- Source: https://github.com/sp1thas/sphinxcontrib-prefectviz
- Bugs: https://github.com/sp1thas/sphinxcontrib-prefectviz/issues
