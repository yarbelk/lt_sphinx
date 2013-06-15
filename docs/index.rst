.. lt_sphinx documentation master file, created by
   sphinx-quickstart on Fri Jun 14 11:08:52 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to lt_sphinx's documentation!
=====================================

the code for this can be found at https://github.com/yarbelk/lt_sphinx/
-----------------------------------------------------------------------

This is a project to illustrate the use of Sphinx, through replaying the
commits.  It starts out from nothing to make a (rather silly) package with
two modules that are docummented.


The steps for getting your doccumentation  all up and running.

1. install Sphinx
2. create a directory for the docs, (i used... `docs`!)
3. run `sphinx-quickstart`
    - I would suggest saying yes to `autodoc` and `viewcode`.  if you forget
      to do this, just add `'sphinx.ext.autodoc'` and `'sphinx.ext.viewcode'`
      to `extensions`.
4. in the configuration file `conf.py`, add your package/module to the
   system path (or make sure it is in `PYTHON_PATH`)
5. write some code.  Document it, run update the `index.rst`, and write
   files for each package/module.  `sphinx-apidoc` helps with this.
6. run `make html`.  you now have docs.  submit to http://readthedocs.org/

Contents:

.. toctree::
   :maxdepth: 2

   lt_sphinx

   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
