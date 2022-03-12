from unittest import TestCase, main
from unittest.mock import patch, call


# 기본적인 mock 이해하기 -> 아래 처럼 patch를 통해 mocking 해주고 싶은 함수를 선택한다.
# 15번을 보면 hello 객체는 return_value로 값을 가지는 것을 확인할 수 있다.
def hello():
    return "Hello!"


class TestMe(TestCase):

    @patch("test.hello", return_value="Mock!!")
    def test_hello(self, mock_hello):
        self.assertEqual(hello(), "Mock!!")
        self.assertIs(hello, mock_hello)
        mock_hello.assert_called_once_with()


if __name__ == "__main__":
    main()
