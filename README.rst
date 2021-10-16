========================
sphinxcontrib-prefectviz
========================

.. image:: https://travis-ci.org/sphinx-contrib/sphinxcontrib-prefectviz.svg?branch=master
    :target: https://travis-ci.org/sphinx-contrib/sphinxcontrib-prefectviz

A Sphinx extension to add Prefect flow visualizations.

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

Long story short:

.. code-block:: rst

    .. flowviz:: module.submodule.flow

**An example:**

First of all, you have to make sure that your prefect flow(s) can be imported by your Sphinx project.
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

    @tast
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
