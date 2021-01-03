# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sys
from os.path import abspath
from pathlib import Path
from json    import dump, loads

sys.path.insert(0, abspath('.'))
sys.path.insert(0, abspath('..'))
sys.path.insert(0, abspath('../pyVHDLModel'))
#sys.path.insert(0, abspath('_extensions'))


# ==============================================================================
# Project information
# ==============================================================================
project =   "pyVHDLModel"
copyright = "2016-2021 Patrick Lehmann - Boetzingen, Germany"
author =    "Patrick Lehmann"


# ==============================================================================
# Versioning
# ==============================================================================
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
from subprocess import check_output

def _IsUnderGitControl():
	return (check_output(["git", "rev-parse", "--is-inside-work-tree"], universal_newlines=True).strip() == "true")

def _LatestTagName():
	return check_output(["git", "describe", "--abbrev=0", "--tags"], universal_newlines=True).strip()

# The full version, including alpha/beta/rc tags
version = "0.8"     # The short X.Y version.
release = "0.8.0"   # The full version, including alpha/beta/rc tags.
try:
	if _IsUnderGitControl:
		latestTagName = _LatestTagName()[1:]		# remove prefix "v"
		versionParts =  latestTagName.split("-")[0].split(".")

		version = ".".join(versionParts[:2])
		release = latestTagName   # ".".join(versionParts[:3])
except:
	pass


# ==============================================================================
# Miscellaneous settings
# ==============================================================================
# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
	"_build",
	"_themes",
	"Thumbs.db",
	".DS_Store"
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'stata-dark'


# ==============================================================================
# Restructured Text settings
# ==============================================================================
prologPath = "prolog.inc"
try:
	with open(prologPath, "r") as prologFile:
		rst_prolog = prologFile.read()
except Exception as ex:
	print("[ERROR:] While reading '{0!s}'.".format(prologPath))
	print(ex)
	rst_prolog = ""


# ==============================================================================
# Options for HTML output
# ==============================================================================
html_theme_options = {
    'home_breadcrumbs': True,
    'vcs_pageview_mode': 'blob',
}

html_context = {}
ctx = Path(__file__).resolve().parent / 'context.json'
if ctx.is_file():
	html_context.update(loads(ctx.open('r').read()))

html_theme_path = ["."]
html_theme = "_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyVHDLModelDoc'

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = "%d.%m.%Y"


# ==============================================================================
# Options for LaTeX / PDF output
# ==============================================================================
from textwrap import dedent

latex_elements = {
	# The paper size ('letterpaper' or 'a4paper').
	'papersize': 'a4paper',

	# The font size ('10pt', '11pt' or '12pt').
	#'pointsize': '10pt',

	# Additional stuff for the LaTeX preamble.
	'preamble': dedent(r"""
		% ================================================================================
		% User defined additional preamble code
		% ================================================================================
		% Add more Unicode characters for pdfLaTeX.
		% - Alternatively, compile with XeLaTeX or LuaLaTeX.
		% - https://github.com/sphinx-doc/sphinx/issues/3511
		%
		\ifdefined\DeclareUnicodeCharacter
			\DeclareUnicodeCharacter{2265}{$\geq$}
			\DeclareUnicodeCharacter{21D2}{$\Rightarrow$}
		\fi


		% ================================================================================
		"""),

	# Latex figure (float) alignment
	#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
	( master_doc,
		'pyVHDLModel.tex',
		'The pyVHDLModel Documentation',
		'Patrick Lehmann',
		'manual'
	),
]



# ==============================================================================
# Extensions
# ==============================================================================
extensions = [
# Standard Sphinx extensions
	"sphinx.ext.autodoc",
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
#	'sphinx.ext.inheritance_diagram',
	'sphinx.ext.todo',
#	'sphinx.ext.graphviz',
	'sphinx.ext.mathjax',
	'sphinx.ext.ifconfig',
	'sphinx.ext.viewcode',
#	'sphinx.ext.duration',

# SphinxContrib extensions
# 'sphinxcontrib.actdiag',
# 'sphinxcontrib.seqdiag',
# 'sphinxcontrib.textstyle',
# 'sphinxcontrib.spelling',
# 'changelog',

# BuildTheDocs extensions
#	'btd.sphinx.autoprogram',
	'btd.sphinx.graphviz',
	'btd.sphinx.inheritance_diagram',

# Other extensions
#	'DocumentMember',
	'sphinx_fontawesome',
	'sphinx_autodoc_typehints',

# local extensions (patched)
	'autoapi.sphinx',

# local extensions
#	'DocumentMember'
]

# ==============================================================================
# Sphinx.Ext.InterSphinx
# ==============================================================================
intersphinx_mapping = {
	'python':   ('https://docs.python.org/3', None),
}


# ==============================================================================
# Sphinx.Ext.AutoDoc
# ==============================================================================
# see: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autodoc_member_order = "bysource"       # alphabetical, groupwise, bysource


# ==============================================================================
# Sphinx.Ext.ExtLinks
# ==============================================================================
extlinks = {
	'issue': ('https://github.com/vhdl/pyVHDLModel/issues/%s', 'issue #'),
	'pull':  ('https://github.com/vhdl/pyVHDLModel/pull/%s', 'pull request #'),
	'src':   ('https://github.com/vhdl/pyVHDLModel/blob/master/pyMetaClasses/%s?ts=2', None),
#	'test':  ('https://github.com/vhdl/pyVHDLModel/blob/master/test/%s?ts=2', None)
}


# ==============================================================================
# Sphinx.Ext.Graphviz
# ==============================================================================
graphviz_output_format = "svg"



# ==============================================================================
# Sphinx.Ext.ToDo
# ==============================================================================
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True



# ==============================================================================
# AutoAPI.Sphinx
# ==============================================================================
autoapi_modules = {
  'pyVHDLModel':  {'output': "pyVHDLModel", "override": True}
}
