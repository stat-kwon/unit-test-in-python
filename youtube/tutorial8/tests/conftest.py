from datetime import datetime

import pytest

from youtube.tutorial8.myapp.student import Student


@pytest.fixture(params=[21, 19], ids=["eligible", "ineligible"])  # eligibel한 나이는 21 / indeligible한 나이는 19 params을 넣어준다.
def dummy_student(request):
    return Student("nikhil", datetime(2000, 1, 1), "coe", 20, request.param)


@pytest.fixture
def dummy_student2(request):
    return Student("nikhil", datetime(2000, 1, 1), "coe", 20, request.param)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits, 19)

    return _make_dummy_student
