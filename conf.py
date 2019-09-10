# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from recommonmark.parser import CommonMarkParser

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

master_doc = "index"

# Source in Markdown

source_parsers = {".md": "recommonmark.parser.CommonMarkParser"}

source_suffix = [".rst", ".md"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_title = "Python Issue Management"


def setup(app):
    app.add_stylesheet("css/custom.css")


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "font_family": "Roboto",
    "body_max_width": "auto",
    "page_width": "80%",
    "code_font_size": "0.8em",
    "fixed_sidebar": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_sidebars = {}

html_sidebars = {"**": ["globaltoc.html", "searchbox.html"]}

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "willingc",  # Username
    "github_repo": "docs-issue-tracker",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": ".",  # Path in the checkout to the docs root,
    "theme_show_relbar_top": True,
    "theme_show_relbar_bottom": True,
}

