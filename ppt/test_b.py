from unittest import mock

from ppt import b

@mock.patch.object(b, 'MyClass')
def test_func(mock_my_class):
    b.my_func()