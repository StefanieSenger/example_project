# example_project

This example_project aimed to be a minimal reproducible for a possible issue with sphinx-gallery when running building examples in parallel. The issue arose in [scikit-learn PR #29614](https://github.com/scikit-learn/scikit-learn/pull/29614#issuecomment-2334083838) and seems instable. I don't manage to re-create it in here, though.

The structure of example_project mimics a basic setup of a dynamically modifiable import statement (represented by both `source/module/__init__.py` and `source/enable_hello_world.py`) for a function residing in `source/module/hello_world.py`.


### notes:

install project:
pip install -e .

building sphinx_gallery:
sphinx-build -b html doc build

clean build docs:
rm -rf build/ doc/auto_examples/ doc/sg_execution_times.rst

link to PEP 562:
https://peps.python.org/pep-0562/
