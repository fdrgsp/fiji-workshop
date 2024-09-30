[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

# Template to host workshop materials

This repository uses Sphinx to generate documentation from reStructuredText (reST) files. 

## Getting started

To modify the content of this repository, follow these steps:


1. **Create a repository in the IAC-HMS organization**. e.g. fiji-workshop. 

2. **Clone the repository**: Clone this repository to your local machine using VSCode or Git.

    ```bash
    git clone https://github.com/HMS-IAC/<workshop-name>.git
    ```

3. **Create an environment**: For example, using conda. 
    ```bash
    conda create -n fiji-workshop python=3.11
    conda activate fiji-workshop
    ```

4. **Install Sphinx and extensions**: `pydata` is the Sphinx theme used. 

    ```bash
    pip install -U sphinx pydata_sphinx_theme sphinx_copybutton
    ```

5. **Quickstart sphinx**: 

    First, create a /docs folder (e.g. mkdir docs). 

    ```bash
    sphinx-quickstart docs
    ```

    > Separate source and build directories (y/n) [n]: Write “y” (without quotes) and press Enter.
    > Project name: Write "fiji-workshop" (without quotes) and press Enter.
    > Author name(s): Write "name, name, name" (without quotes) and press Enter.
    > Project release []: e.g. write “0.1” (without quotes) and press Enter.
    > Project language [en]: Leave it empty (the default, English) and press Enter.
    

6. **Configure the build with conf.py**: Navigate to the directory containing the documentation source files.

    ```bash
    cd docs/source
    ```

    Replace the content of the `conf.py` file with the following:

    ```python

    import os
    ```

5. **Modify and build for as single version**: Edit the `.rst` files in the source directory to make changes to the documentation content. You can use any text editor to modify these files. Then, build the html files. 

    ```bash
    make clean
    ```

    ```bash
    make html
    ```

8. **HTML files**: After building the documentation, you can view the updated the HTML files located in the `docs/build/html` directory.

9. **Move the content of `docs/build/html` to root directory of gh-pages branch**: use a `tmp` folder, and drog and drop the folders (each folder contains the materials of a version) to the root of the publishing branch. 

10. **Commit and Push Changes**: After verifying that the documentation looks as expected by opening local html file, commit your changes and push them to the repository.

    ```bash
    cd ..
    git add .
    git commit -m "Update documentation"
    git push
    ```

## Additional resources

- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/): Official documentation for Sphinx.
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html): Learn the basics of reStructuredText (reST) markup language.
