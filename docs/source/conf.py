import os
import sys

# -- Project information -----------------------------------------------------
project = 'workshop-template'
copyright = '2024, Antoine A. Ruzette'
author = 'Antoine A. Ruzette'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/iac-hms-logo.png"
html_title = 'Template for IAC workshops'

html_theme_options = {
    'logo': {
        'text': 'Template for IAC workshops',
        'image_light': '_static/iac-hms-logo-light.png',
        'image_dark': '_static/iac-hms-logo-dark.png',
    },
    'navbar_end': ['navbar-icon-links', 'theme-switcher'],
    "theme_switcher": True,
    "icon_links": [
        {
            "name": "IAC",
            "url": "https://iac.hms.harvard.edu/",
            "icon": "fa-solid fa-globe",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/HMS-IAC",
            "icon": "fa-brands fa-github",
        }
    ],
}

# Sidebar settings for navigation
html_sidebars = {
    "**": ["sidebar-nav-bs", "versions.html"],
}

# -- Version-Specific Handling -----------------------------------------------
# Detect the current version being built via the environment variable
current_version = os.getenv('CURRENT_VERSION', None)

# Ensure that we set the master document based on the version being built
if current_version:
    # Set the master_doc to the index.rst file in the specific version folder
    master_doc = f"index"  # We keep it as "index", but we're controlling the source directory directly
    # Set the version-specific source directory
    source_suffix = ['.rst', '.md']
    version_source_dir = os.path.abspath(f"versions/{current_version}")
    sys.path.insert(0, version_source_dir)  # Make sure Sphinx is pointed to the correct version directory
    # Ensure the version-specific static path is included
    html_static_path = [f"versions/{current_version}/_static", '_static']
else:
    # Default behavior for the main build
    master_doc = 'index'
    html_static_path = ['_static']

# -- Configurations for displaying versions ----------------------------------
# Define the path to the versions directory
versions_dir = os.path.join(os.path.dirname(__file__), 'versions')

# Collect all version directories
versions = []
if os.path.isdir(versions_dir):
    versions = [d for d in os.listdir(versions_dir) if os.path.isdir(os.path.join(versions_dir, d))]

# Make the versions available to the templates
html_context = {
    'versions': [{'name': v, 'url': f'/versions/{v}/index.html'} for v in versions],
}
