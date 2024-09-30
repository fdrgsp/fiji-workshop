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

# Use global _templates directory for all versions
templates_path = ['../../_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/iac-hms-logo-light.png"
html_title = 'Template for IAC workshops'

html_theme_options = {
    'logo': {
        'text': 'Template for IAC workshops',
        'image_light': '_static/iac-hms-logo-light.png',
        'image_dark': '_static/iac-hms-logo-dark.png',
    },
    'navbar_end': ['navbar-icon-links', 'theme-switcher'],
    'theme_switcher': True,
    'icon_links': [
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
    "**": ["sidebar-nav-bs", "sidebar_versions.html"],
}

# -- Version-Specific Handling -----------------------------------------------
current_version = os.getenv('CURRENT_VERSION', None)

if current_version:
    master_doc = 'index'
    version_source_dir = os.path.abspath(f"versions/{current_version}")
    sys.path.insert(0, version_source_dir)
    html_static_path = [os.path.join(version_source_dir, '_static')] if os.path.isdir(os.path.join(version_source_dir, '_static')) else []
    html_static_path.append('_static')  # Always include the main static path
else:
    master_doc = 'index'
    html_static_path = ['_static']

# -- Automatically detect repository and base URL ----------------------------

# Use GITHUB_REPOSITORY or default to detecting the folder name
repository_name = os.getenv('GITHUB_REPOSITORY', 'hms-iac/workshop-template').split('/')[-1]

# Construct the base URL based on the repository name
base_url = f"/{repository_name}/" if repository_name else "/"

# -- Configurations for displaying versions ----------------------------------
versions_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../versions'))

# Collect all version directories
versions = []
if os.path.isdir(versions_dir):
    versions = [d for d in os.listdir(versions_dir) if os.path.isdir(os.path.join(versions_dir, d))]

# Make the versions available to the templates with the correct base path
html_context = {
    'versions': [{'name': v, 'url': f'{base_url}versions/{v}/html/index.html'} for v in versions],
}
