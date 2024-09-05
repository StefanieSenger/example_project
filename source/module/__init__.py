__all__ = []

def __getattr__(name):
    print(f"name: {name}")
    print(f"__name__: {__name__}")
    if name=="hello_world":
        raise ImportError("hello_world wasn't enabled.")
    
    raise AttributeError(f"module {__name__} has no attribute {name}")
