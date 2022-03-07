import pytest

from youtube.tutorial1.myapp.sample import add


def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


def test_add_list():
    assert add([1, 2], [3]) == [1, 2, 3]


@pytest.mark.parametrize("a,b,c",
                         [(1, 2, 3), ("a", "b", "ab"), ([1, 2], [3], [1, 2, 3])],
                         ids=["num", "str", "list"]) # parametrize를 활용해 위의 3개 def를 하나로 표현가능하다.
def test_add(a, b, c):
    assert add(a, b) == c
