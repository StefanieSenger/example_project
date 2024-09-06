from source import module
import pytest

def test_raising_importerror():
# test that ImportError raised if hello_worlds is no enabled:
    with pytest.raises(ImportError) as message:
        module.hello_world()
    print(message)

def test_hello_world_enabling():
    from source import enable_hello_world
    module.hello_world()


test_raising_importerror()
test_hello_world_enabling()