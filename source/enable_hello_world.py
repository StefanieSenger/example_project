from source import module

setattr(module, "hello_world", module.hello_world) # not sure how this is different from the next line, except that it leads to an earlier Error raised...
module.__all__ += ["hello_world"]

print("hello_world has been enabled.")
print(module.__all__)