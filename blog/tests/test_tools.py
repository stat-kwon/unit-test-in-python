from unittest import TestCase, mock
from unittest.mock import patch, PropertyMock

from blog.myapp import tools
from blog.myapp.tools import function_to_test
from blog.utils.subpakage import foobar


class TestClass(TestCase):
    def test_normal_call_pass(self):
        with mock.patch("blog.myapp.tools.foobar") as mock_foobar:
            mock_foobar.return_value = "something"
            retval = function_to_test(1, 2)
        self.assertEqual("somethingxyz", retval)
        mock_foobar.assert_called_with(1, 4)

    @patch.object(tools, 'foobar', return_value='something') # 실제 선언되는 부분의 경로로 mock 지정을 해줘야 함
    def test_normal_call(self, mock_data):
        retval = function_to_test(1, 2)
        self.assertEqual("somethingxyz", retval)

''' 
여기부분이 특히 중요!!!!!!!!!! 깨닳는데 2일걸림... 하ㅏㅏㅏㅏ
기본 원칙은 object가 검색되는 위치에 패치를 적용한다는 것
object가 정의된 위치와 반드시 같은 위치일 필요는 없음

The key is to do the patching in the right namespace. 
The basic principle is that you patch where an object is looked up, 
which is not necessarily the same place as where it is defined.
'''