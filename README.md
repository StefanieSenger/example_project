# example_project

This example_project aims to be a minimal reproducible for a possible issue with sphinx-gallery when running the 'builder-inited' event with sphinx when the sphinx-gallery is build in parallel. The issue arised in scikit-learn [PR #29614](https://github.com/scikit-learn/scikit-learn/pull/29614#issuecomment-2332319250). I don't manage to re-create it in here, though.

The structure of example_project mimics a basic setup of a dynamically modifiable import statement (represented by both `source/module/__init__.py` and `source/enable_hello_world.py`) for a function residing in `source/module/hello_world.py`.


### notes:

install project:
pip install -e .

building sphinx_gallery:
sphinx-build -M html doc build

building the part that is failing in scikit-learn:
sphinx-build -b linkcheck doc build

delete build docs:
rm -rf build/ doc/auto_examples/

link to PEP 562:
https://peps.python.org/pep-0562/
