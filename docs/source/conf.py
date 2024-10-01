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
current_version = os.getenv('CURRENT_VERSION', None)  # Gets the version being built
versions_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'versions'))

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

# Use global _templates directory for all versions
templates_path = ['_templates']
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
        'image_light': os.path.join('_static', 'iac-hms-logo-light.png'),
        'image_dark': os.path.join('_static', 'iac-hms-logo-dark.png'),
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
# Always include the main static path
html_static_path = [os.path.abspath('_static')]

# If a specific version is being built, prepend its static path
if current_version:
    master_doc = 'index'  # Ensure correct starting point
    version_source_dir = os.path.abspath(os.path.join('versions', current_version))
    sys.path.insert(0, version_source_dir)  # Add the version directory to the Python path
    
    # Add version-specific static path if it exists
    version_static_path = os.path.join(version_source_dir, '_static')
    if os.path.isdir(version_static_path):
        html_static_path.insert(0, version_static_path)  # Prepend to include version-specific files
        print(f"Added {version_static_path} to html_static_path")

# -- Automatically detect and display versions ------------------------------
versions = []
if os.path.isdir(versions_dir):
    versions = [d for d in os.listdir(versions_dir) if os.path.isdir(os.path.join(versions_dir, d))]

# Make the versions available to the templates with the correct base path
html_context = {
    'versions': [{'name': v, 'url': f'{base_url}versions/{v}/html/index.html'} for v in versions],
}
