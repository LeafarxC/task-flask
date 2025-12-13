import pytest
import requests

#CRUD
BAS_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
  new_task_data = {
    "title": "Test Task",
    "description": "Test Description",
    "completed": False
  }
  response = requests.post(f"{BAS_URL}/tasks", json=new_task_data)
  assert response.status_code == 201
  assert response.json()["title"] == new_task_data["title"]
  assert response.json()["description"] == new_task_data["description"]
  assert response.json()["completed"] == new_task_data["completed"]
  tasks.append(response.json())

def test_get_tasks():
  response = requests.get(f"{BAS_URL}/tasks")
  assert response.status_code == 200
  assert len(response.json()) == len(tasks)
  for i in range(len(tasks)):
    assert response.json()[i]["title"] == tasks[i]["title"]
    assert response.json()[i]["description"] == tasks[i]["description"]
    assert response.json()[i]["completed"] == tasks[i]["completed"]

def test_get_task():
  response = requests.get(f"{BAS_URL}/tasks/1")
  assert response.status_code == 200

def test_update_task():
  response = requests.put(f"{BAS_URL}/tasks/1", json={"title": "Updated Task", "description": "Updated Description", "completed": True})
  assert response.status_code == 200
  assert response.json()["title"] == "Updated Task"
  assert response.json()["description"] == "Updated Description"
  assert response.json()["completed"] == True
  tasks.remove(tasks[0])
  assert len(tasks) == 0

def test_delete_task():
  response = requests.delete(f"{BAS_URL}/tasks/1")
  assert response.status_code == 200
  assert response.json()["message"] == "Task deleted successfully"
  assert len(tasks) == 0

if __name__ == "__main__":
  pytest.main()