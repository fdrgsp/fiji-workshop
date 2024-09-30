[![CC BY 4.0][cc-by-shield]][cc-by]  
This work is licensed under a  
[Creative Commons Attribution 4.0 International License][cc-by].  

[cc-by]: http://creativecommons.org/licenses/by/4.0/  
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg  

# Workshop Materials Template

This repository provides a template to host workshop materials using Sphinx to generate HTML documentation from reStructuredText (reST) files. You can use it to organize your workshop presentations, exercises, and materials in a structured and versioned manner.

## Folder Structure

The repository uses the following structure for organizing multiple workshop versions, each with its own content and slides:
    
```plaintext
workshop-name/
├── docs/
│   ├── build/
│   ├── source/
│   │   ├── _templates/
│   │   ├── versions/
│   │       ├── 2024_01_30/
|   |           ├── _static/
│   │               ├── 01_slide.pdf
│   │               ├── 02_slide.pdf
│   |               └── ...
|   |           ├── 01_slide.rst
│   │           ├── 02_slide.rst
│   │           ├── make.bat
│   │           ├── Makefile
│   |           ├── conf.py
│   │           └── ...
│   │       ├── 2024_02_15/
|   |           ├── _static/
│   │               ├── 01_slide.pdf
│   │               ├── 02_slide.pdf
│   |               └── ...
│   │           ├── make.bat
│   │           ├── Makefile
│   |           ├── conf.py
│   │           └── ...
│   │       └── ...
│   ├── build_versions.sh
└── ...
```

Each folder in `versions/` corresponds to a specific workshop version, with its own set of slides and content.

## Instructions

### 1. Create a new repository and clone this one

First, create a new repository on the IAC-HMS github to host your workshop materials. Then, to clone this repository, download the content of this repository as ZIP, or run:

```bash
git clone https://github.com/HMS-IAC/workshop-template.git
```

### 2. Install dependencies

To install the necessary Python dependencies, run:

```bash
conda create -n fiji-workshop python=3.11
conda activate fiji-workshop
pip install -U sphinx pydata_sphinx_theme sphinx_copybutton
```

### 3. Customize the template

1. Update each `conf.py` file in the `source/versions` folder with the name of your workshop and your name.

```python
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
```

### 4. Add your content

1. Add your slides as PDF files in the `_static` folder of each version.
2. Add your content as reStructuredText (reST) files in the `source/versions` folder of each version.

### 5. Build the documentation

This bash script will build the documentation for each version in the `source/versions` folder, as well as creating a entry index.html file to redirect to the latest version of the workshop i.e. the most recent one.

```bash
sh docs/build_versions.sh
```

It's good practice to start from a clean /build folder. To do so, run:

```bash
cd docs
make clean
cd ..
```

### 6. Publish the documentation

Save in a temporary folder the content of the `docs/build` folder. Then, manually add – or override the existing content – the content of the `docs/build` folder to the root of the `gh-pages` branch of your repository. Make sure your `gh-pages` branch contains a .nojekyll file to prevent GitHub from ignoring the `_static` folder.

```bash
git checkout -b gh-pages
git add .
git commit -m "Add workshop materials"
git push origin gh-pages
```

### 7. Enable GitHub Pages

Go to the settings of your repository, and under the GitHub Pages section, select the `gh-pages` branch as the source for your GitHub Pages.