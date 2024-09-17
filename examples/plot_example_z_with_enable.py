"""
==========================================================
A Python file simulating example 2 to be build in parallel
==========================================================
Second example using enable_hello_world:
"""

import time
from source import module

time.sleep(3)
from source import enable_hello_world
module.hello_world()