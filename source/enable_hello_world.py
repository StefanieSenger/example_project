from source import module
from source.module._hello_world import hello_world

setattr(module, "hello_world", hello_world)
if "hello_world" not in module.__all__:
    module.__all__ += ["hello_world"]

print("hello_world has been enabled.")