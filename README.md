# example_project

install project:
pip install -e .

building sphinx_gallery:
sphinx-build -M html doc build

or, for just the failing part:
sphinx-build -b linkcheck doc build

testing with ipython:
from source import module
module.hello_world.py
from source import enable_hello_world
module.hello_world.py

link to PEP 562:
https://peps.python.org/pep-0562/
