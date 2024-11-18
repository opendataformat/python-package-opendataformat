# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenDataFormat'
copyright = '2024, Tom Hartl, Xiaoyao Han'
author = 'Tom Hartl, Xiaoyao Han'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',            
    'sphinx.ext.napoleon',           
    'sphinx.ext.viewcode',           
    'sphinx_autodoc_typehints',]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Point to package
import os
import sys
sys.path.insert(0, os.path.abspath('../opendataformat'))
