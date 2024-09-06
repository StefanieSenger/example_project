__all__ = []

def __getattr__(name):
    if name=="hello_world":
        raise ImportError("hello_world wasn't enabled.")
    
    raise AttributeError(f"module {__name__} has no attribute {name}")
