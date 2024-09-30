import os
import sys

# -- Customizable Project Settings -------------------------------------------
project = 'workshop-template'
copyright = '2024, Antoine A. Ruzette'
author = 'Antoine A. Ruzette'
release = '0.0.1'
html_title = 'Template for IAC workshops'

# URLs
iac_url = "https://iac.hms.harvard.edu/"
github_url = "https://github.com/HMS-IAC"
repository_name = os.getenv('GITHUB_REPOSITORY', 'hms-iac/workshop-template').split('/')[-1]
base_url = f"/{repository_name}/" if repository_name else "/"

# Version-specific handling
current_version = os.getenv('CURRENT_VERSION', None)
versions_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../versions'))

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

# Logos and branding
html_logo = "_static/iac-hms-logo-light.png"
html_logo_dark = "_static/iac-hms-logo-dark.png"

# Use global _templates directory for all versions
templates_path = ['../../_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = 'pydata_sphinx_theme'

# Sidebar settings for navigation
html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar_versions.html"],
}

# Theme options, including light/dark mode logos and switcher
html_theme_options = {
    'logo': {
        'text': 'Template for IAC workshops',
        'image_light': html_logo,
        'image_dark': html_logo_dark,
    },
    'navbar_end': ['navbar-icon-links', 'theme-switcher'],
    'theme_switcher': True,
    'icon_links': [
        {
            "name": "IAC",
            "url": iac_url,
            "icon": "fa-solid fa-globe",
        },
        {
            "name": "GitHub",
            "url": github_url,
            "icon": "fa-brands fa-github",
        }
    ],
}

# -- Version-Specific Handling -----------------------------------------------
if current_version:
    master_doc = 'index'
    version_source_dir = os.path.abspath(f"versions/{current_version}")
    sys.path.insert(0, version_source_dir)
    html_static_path = [os.path.join(version_source_dir, '_static')] if os.path.isdir(os.path.join(version_source_dir, '_static')) else []
    html_static_path.append('_static')  # Always include the main static path
else:
    master_doc = 'index'
    html_static_path = ['_static']

# -- Automatically detect and display versions ------------------------------
versions = []
if os.path.isdir(versions_dir):
    versions = [d for d in os.listdir(versions_dir) if os.path.isdir(os.path.join(versions_dir, d))]

# Make the versions available to the templates with the correct base path
html_context = {
    'versions': [{'name': v, 'url': f'{base_url}versions/{v}/html/index.html'} for v in versions],
}
