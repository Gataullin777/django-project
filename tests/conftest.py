import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture()
def student_factory():
    def factory(**kwargs):
        return baker.make("Student", make_m2m=True,  **kwargs)
    return factory


@pytest.fixture()
def course_factory():
    def factory(**kwargs):
        return baker.make("Course",  make_m2m=True, **kwargs)
    return factory



