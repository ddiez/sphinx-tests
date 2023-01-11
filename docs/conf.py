extensions = [
  "sphinx_rtd_theme",
  "sphinx.ext.autodoc",
  "sphinx.ext.autosummary",
  "nbsphinx",
  "myst_parser"
]

html_theme = "sphinx_rtd_theme"

project="sphinx-tests"

html_context = dict(
    display_github=True,      # Integrate GitHub
    github_user='ddiez',   # Username
    github_repo='sphinx-tests',     # Repo name
    github_version='main',  # Version
    conf_py_path='/',    # Path in the checkout to the docs root
)