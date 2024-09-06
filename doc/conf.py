# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'example_project'
copyright = '2024, StefanieSenger'
author = 'StefanieSenger'
release = 'now'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

# _________________________________
# start of not auto-generated stuff

master_doc = 'index'

extensions = [
    'sphinx_gallery.gen_gallery',
    ]

sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
     'parallel': 2,
}


def disable_plot_gallery_for_linkcheck(app):
    if app.builder.name == "linkcheck":
        sphinx_gallery_conf["plot_gallery"] = "False"


def setup(app):
    app.connect("builder-inited", disable_plot_gallery_for_linkcheck)