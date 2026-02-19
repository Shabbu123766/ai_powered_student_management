import pytest
from fastapi.testclient import TestClient
from main import app
from database import students

@pytest.fixture(autouse=True)
def clear_students():
    students.clear()


@pytest.fixture
def client():
    return TestClient(app)


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}



def test_create_student(client):
    payload = {
        "name": "Abhi",
        "age": 22,
        "grade": "A",
        "email": "abhi@gmail.com"
    }

    response = client.post("/students", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Student created"
    assert response.json()["student"]["name"] == "Abhi"
    assert response.json()["student"]["age"] == 22



def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert "students" in response.json()



def test_update_student(client):
    
    payload = {
        "name": "Rahul",
        "age": 20,
        "grade": "B",
        "email": "rahul@gmail.com"
    }

    create_response = client.post("/students", json=payload)
    student_id = create_response.json()["student"]["id"]

    
    updated_payload = {
        "name": "Rahul Updated",
        "age": 21,
        "grade": "A",
        "email": "rahul@gmail.com"
    }

    update_response = client.put(f"/students/{student_id}", json=updated_payload)

    assert update_response.status_code == 200
    assert update_response.json()["message"] == "Student updated"
    assert update_response.json()["student"]["name"] == "Rahul Updated"
    assert update_response.json()["student"]["age"] == 21



def test_delete_student(client):
    
    payload = {
        "name": "Delete Me",
        "age": 23,
        "grade": "C",
        "email": "delete@gmail.com"
    }

    create_response = client.post("/students", json=payload)
    student_id = create_response.json()["student"]["id"]

    
    delete_response = client.delete(f"/students/{student_id}")

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Student deleted"

    
    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 404



def test_feedback_positive(client):
    payload = {
        "text": "This is a great student"
    }

    response = client.post("/feedback", json=payload)

    assert response.status_code == 200
    assert response.json()["analysis"]["sentiment"] == "Positive"



def test_search_student(client):
    response = client.get("/search?query=Abhi")

    
    assert response.status_code in [200, 404]
