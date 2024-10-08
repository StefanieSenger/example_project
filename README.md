# example_project

This example_project aimed to be a minimal reproducible for a possible issue with sphinx-gallery when running building examples in parallel. The issue arose in [scikit-learn PR #29614](https://github.com/scikit-learn/scikit-learn/pull/29614#issuecomment-2334083838) and seems instable. I don't manage to re-create it in here, though.

The structure of example_project mimics a basic setup of a dynamically modifiable import statement (represented by both `source/module/__init__.py` and `source/enable_hello_world.py`) for a function `hello_world()` residing in `source/module/_hello_world.py`.


### notes:

install project:
`pip install -e .`

building sphinx_gallery:
`sphinx-build -b html doc doc/build -j 1`

clean build docs:
`rm -rf doc/build/ doc/auto_examples/ doc/sg_execution_times.rst`

link to PEP 562:
https://peps.python.org/pep-0562/
