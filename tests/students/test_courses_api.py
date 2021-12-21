import json

import pytest
from django.test import TestCase
from model_bakery import baker
from django.urls import reverse

from students.models import Student, Course


@pytest.mark.django_db
def test_get_course_1(client, course_factory, student_factory):
    url = reverse("courses-list")

    courses = course_factory(_quantity=1)
    course_1 = courses[0]

    id_course = course_1.id
    name_course = course_1.name

    response = client.get(url, data={"id": f"{id_course}"})
    assert response.status_code == 200
    assert response.data[0]['id'] == id_course
    assert response.data[0]['name'] == name_course


# products_set = baker.prepare(Product, _quantity=5)
# history = baker.make(PurchaseHistory, products=products_set)



@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    url = reverse("courses-list")
    courses = course_factory(_quantity=5)
    response = client.get(url)
    assert response.status_code == 200
    len_data = len(response.data)
    assert len_data == 5


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    url = reverse("courses-list")
    courses = course_factory(_quantity=5)
    course_id = courses[3].id
    response = client.get(url, data={"id": course_id})
    assert response.status_code == 200
    assert response.data[0]["id"] == course_id


@pytest.mark.django_db
def test_get_course(client, course_factory):
    url = reverse("courses-list")
    courses = course_factory(_quantity=5)
    name_1_course = courses[0].name
    response = client.get(url, data={"name": f"{name_1_course}"})
    assert response.status_code == 200
    assert response.data[0]['name'] == name_1_course


@pytest.mark.django_db
def test_check_create(client):
    test_data = {
        'id': 3,
        "name": 'math'
    }
    url = reverse("courses-list")
    response = client.post(url, data=test_data)
    assert response.status_code == 201
    assert response.data["name"] == test_data["name"]


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=2)
    pk_first_course = courses[0].pk
    url = reverse("courses-detail", args=(pk_first_course,))

    print()
    response = client.patch(url, data={"name": "successfully"})

    assert response.status_code == 200
    assert response.data['name'] == "successfully"





@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=5)
    pk_first_course = courses[0].pk
    url = reverse("courses-detail", args=(pk_first_course,))

    response = client.delete(url)

    assert (response.status_code == 204 or response.status_code == 200)
    assert len(Course.objects.all()) == 4

