# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import shutil

# Dodaj ścieżkę do katalogu, w którym znajduje się Twój kod
sys.path.insert(0, os.path.abspath('..'))

def setup(app):
    # Skopiuj plik JSON do katalogu build, aby był dostępny podczas generowania dokumentacji
    shutil.copyfile('../jednostki.json', 'jednostki.json')


project = 'Konwerter PBL'
copyright = '2024, Oskar Zagorski'
author = 'Oskar Zagorski'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
