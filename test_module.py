# content of test_module.py

import pytest
slow = pytest.mark.slow

def test_func_fast():
    pass

@slow
def test_func_slow():
    pass
