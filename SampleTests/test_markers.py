# https://docs.pytest.org/en/7.1.x/how-to/skipping.html

import pytest
import sys
"""
used to set metadata on the unit tests functions so that pytest
has some extra information on hw to execute unit tests
"""


def add(*args):
    res = 0
    for i in args:
        res += i
    return res


# @pytest.mark.skip(reason="just wanna skip it")
def test_add_num():
    print(add(6, 3))
    assert add(6, 3) == 9


# used to pass or ignore it based on condition
# @pytest.mark.skipif(sys.version_info < (2,0), reason="skip it if python version 3.7 or less")
# @pytest.mark.skipif(True, reason="just wanna skip it")
@pytest.mark.skipif(False, reason="just wanna skip it")
def test_add_num_1():
    print(add(6, 3))
    assert add(6, 3) == 9


# wn we know tests cn throw exception, we wanna let go
# if cond is satisfied & exception is thrown then ignore it
# i.e test will not fail just get skipped
@pytest.mark.xfail(sys.platform=='win32', reason="just wanna skip it")
def test_xfail():
    # XFail: mark test functions as expected to fail (correct)
    print("test xfail")
