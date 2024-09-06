from source import module
from source.module.hello_world import hello_world

setattr(module, "hello_world", hello_world)
module.__all__ += ["hello_world"]

print("hello_world has been enabled.")