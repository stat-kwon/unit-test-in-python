import sys

import pytest

from youtube.tutorial3.myapp.sample import add


@pytest.mark.skip(reason="just wanna skip it")  # skip 기능을 사용할 수 있음
def test_add_num():
    assert add(1, 2) == 4


@pytest.mark.skipif(sys.version_info > (3, 7), reason="use python 3.7 or less")  # if로 specific하게 조건을 줄 수 있음
def test_add_str():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "win32", reason= "don't run on windows") # win32라면 exception을 무시하고 진행해주세요.
def test_add_list(): # sys.platform == "darwin"이기 때문에 exception은 발생했고 test fail하게 됨
    assert add([1], [2] == [1, 2])
    raise Exception()
