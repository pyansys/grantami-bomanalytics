import sys
import os
sys.path.insert(0, os.path.abspath('../../src'))
from ansys.granta import bom_analytics

# -- Project information -----------------------------------------------------

project = 'ansys.granta.bom_analytics'
copyright = '(c) 2021 ANSYS, Inc. All rights reserved'
author = 'ANSYS Inc.'

# The short X.Y version
release = version = bom_analytics.__version__
release = version = "0.0.dev0"

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx_autodoc_typehints',
    'sphinx.ext.autosummary',
    'notfound.extension',
    'sphinx_copybutton',
    'sphinx.ext.extlinks',
    'sphinx.ext.coverage',
    'enum_tools.autoenum',
]

# return type inline with the description.
napoleon_use_rtype = False

# static path
html_static_path = ['_static']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Copy button customization ---------------------------------------------------
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r'>>> ?|\.\.\. '
copybutton_prompt_is_regexp = True


# -- Options for HTML output -------------------------------------------------
# html_theme = 'pyansys_sphinx_theme'
# html_logo = 'https://docs.pyansys.com/_static/pyansys-logo-black-cropped.png'
# html_theme_options = {
#     "github_url": "https://github.com/pyansys/granta-bom-analytics",
#     "show_prev_next": False
# }

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pybomanalyticsdoc'


# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pyansys.tex', 'ansys.granta.bom_analytics Documentation',
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ansys.granta.bom_analytics', 'ansys.granta.bom_analytics Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ansys.granta.bom_analytics', 'ansys.granta.bom_analytics Documentation',
     author, 'ansys.granta.bom_analytics', 'Python interface to the Granta MI Restricted Substances module',
     'Engineering Software'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
