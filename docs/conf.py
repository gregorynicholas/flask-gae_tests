# -*- coding: utf-8 -*-
#
# documentation build configuration file, created by
# sphinx-quickstart on thu dec  6 14:38:14 2012.
#
# this file is execfile()d with the current directory set to its containing dir
#
# note that not all possible configuration values are present in this
# autogenerated file.
#
# all configuration values have a default; values that are commented out
# serve to show the default.


# -- path configuration -------------------------------------------------------

import os
import sys
# if extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here. if the directory is relative to the
# documentation root, use os.path.abspath to make it absolute:
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'flask'

try:
  # a hack to see if the app engine sdk is loaded..
  import yaml
except ImportError:
  import dev_appserver
  dev_appserver.fix_sys_path()


# -- general configuration ----------------------------------------------------

# if your documentation needs a minimal sphinx version, state here
# needs_sphinx = '1.0'

# add any Sphinx extension module names here, as strings.
# they can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']

# add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# the suffix of source filenames.
source_suffix = '.rst'

# the encoding of source files.
# source_encoding = 'utf-8-sig'

# the master toctree document.
master_doc = 'index'

# General information about the project.
project = u'flask-funktional-gae'
copyright = u'2013, gregory nicholas'

# the version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# the short x.y version.
version = '0.0.1'
# the full version, including alpha/beta/rc tags.
release = '0.0.1-alpha'


# language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# there are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# list of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# the rest default role (used for this markup: `text`) to use for all documents
# default_role = none

# if true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# if true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# if true, sectionauthor and moduleauthor directives will be shown in the
# output. they are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# a list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- options for html output --------------------------------------------------

html_theme = 'flask_small'

# theme options are theme-specific and customize the look and feel of a theme
# further.  see docs for a list of options available for each theme.
# html_theme_options = {}

# add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# the name for this set of sphinx documents.  if none, it defaults to
# "<project> v<release> documentation".
# html_title = None

# a shorter title for the navigation bar.  default is the same as html_title.
# html_short_title = None

# the name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# the name of an image file (within the static path) to use as favicon of the
# docs.  this file should be a windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. they are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# if not '', a 'last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# if true, smartypants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# if false, no module index is generated.
html_domain_indices = False

# if false, no index is generated.
html_use_index = False

# if true, the index is split into individual pages for each letter.
html_split_index = False

# if true, links to the rest sources are added to the pages.
html_show_sourcelink = True
html_show_sphinx = False

# if true, "(c) copyright ..." is shown in the html footer. default is true.
html_show_copyright = True

# if true, an opensearch description file will be output, and all pages will
# contain a <link> tag referring to it.  the value of this option must be the
# base url from which the finished html is served.
# html_use_opensearch = ''

html_file_suffix = None

# output file base name for html help builder.
htmlhelp_basename = 'flask-funktional-gae-doc'
