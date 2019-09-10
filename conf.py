# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Python Issue Tracking"
copyright = "2019, Python Core Team"
author = "Python Core Team"

# The full version, including alpha/beta/rc tags
release = "0.1"

# -- General configuration ---------------------------------------------------

extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

# Source in Markdown

import recommonmark
from recommonmark.transform import AutoStructify


def setup(app):
    app.add_config_value("recommonmark_config", {"enable_eval_rst": True}, True)
    app.add_stylesheet("custom.css")
    app.add_transform(AutoStructify)


source_parsers = {".md": "recommonmark.parser.CommonMarkParser"}

source_suffix = [".rst", ".md"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

