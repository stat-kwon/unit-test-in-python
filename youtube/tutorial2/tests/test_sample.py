import pytest

from youtube.tutorial2.myapp.sample import validate_age


def test_validate_age_valid_age():
    validate_age(10)


def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)


# 아래와 같이 할 수 있는 것을 위에서 인자를 통해 쉽게 만들 수 있다.
# def test_validate_age_invalid_age():
#     with pytest.raises(ValueError) as exc_info: # with context안에 예상하는 에러를 적어놓고 맞았을 경우 test가 통과한다.
#         # validate_age(1) #fail
#         validate_age(-1)
#     assert str(exc_info.value) == "Age cannot be less than 0"
