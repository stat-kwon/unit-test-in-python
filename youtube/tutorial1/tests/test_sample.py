from youtube.tutorial1.myapp.sample import add


# function의 prefix를 test_로 시작해야 terminal에서 pytest로 인식한다.
def test_add_num():
    assert add(1, 2) == 4


def test_add_str():
    assert add("a", "b") == "ab"


# class로 group을 니만들 수 있는데 이 때도 prefix가 Test여야 한다.
class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"
