from datetime import datetime

import pytest

from youtube.tutorial7.myapp.student import Student


@pytest.fixture
def dummy_student():
    return Student("nikhil", datetime(2000, 1, 1), "coe", 20)


@pytest.fixture # name, credits만 변경되는 Student 객체를 만들고 싶을 때 factory 패턴을 이용한다.
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student