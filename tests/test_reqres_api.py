import pytest
import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

class TestReqresAPI:

    def test_01_get_users_list_successful(self):
        """
        API-01: Successful GET request to /users?page=2
        Validates: HTTP 200, pagination metadata, and array of user objects with exact schema.
        """
        response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)
        
        # 1. Status Code Assertion
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
        
        # 2. Response Body Schema & Type Assertions
        body = response.json()
        assert isinstance(body, dict), "Response body is not a JSON object"
        
        # Top-level keys shape
        required_keys = ["page", "per_page", "total", "total_pages", "data", "support"]
        for key in required_keys:
            assert key in body, f"Missing key '{key}' in response body"
            
        assert isinstance(body["page"], int) and body["page"] == 2
        assert isinstance(body["data"], list), "'data' must be an array"
        assert len(body["data"]) > 0, "'data' array should not be empty"

        # Item schema validation
        user_schema = ["id", "email", "first_name", "last_name", "avatar"]
        for user in body["data"]:
            for ukey in user_schema:
                assert ukey in user, f"Missing user field '{ukey}' in user item: {user}"
            assert isinstance(user["id"], int)
            assert "@" in user["email"], f"Invalid email format: {user['email']}"
            assert user["avatar"].startswith("http"), f"Invalid avatar URL: {user['avatar']}"

    def test_02_create_user_post_successful(self):
        """
        API-02: Successful POST request to create a user /users
        Validates: HTTP 201 Created, echoed fields, auto-generated ID, and ISO timestamp.
        """
        payload = {
            "name": "Vishwa Vijay Kumar",
            "job": "Junior QA Automation Engineer"
        }
        response = requests.post(f"{BASE_URL}/users", headers=HEADERS, json=payload)
        
        # 1. Status Code Assertion
        assert response.status_code == 201, f"Expected 201 Created but got {response.status_code}"
        
        # 2. Response Body Shape Assertions
        body = response.json()
        assert isinstance(body, dict)
        assert body.get("name") == payload["name"]
        assert body.get("job") == payload["job"]
        assert "id" in body and body["id"] is not None
        assert "createdAt" in body and isinstance(body["createdAt"], str)
        assert len(body["createdAt"]) > 10, "Invalid createdAt timestamp"

    def test_03_post_register_missing_password_negative(self):
        """
        API-03: Negative POST request with missing password payload to /register
        Validates: HTTP 400 Bad Request and exact error message payload shape.
        """
        payload = {
            "email": "sydney@fife"
            # Missing password deliberately
        }
        response = requests.post(f"{BASE_URL}/register", headers=HEADERS, json=payload)
        
        # 1. Status Code Assertion
        assert response.status_code == 400, f"Expected 400 Bad Request but got {response.status_code}"
        
        # 2. Response Body Shape Assertion
        body = response.json()
        assert isinstance(body, dict)
        assert "error" in body, "Expected 'error' key in response"
        assert body["error"] == "Missing password", f"Unexpected error message: {body.get('error')}"

    def test_04_get_single_user_not_found(self):
        """
        API-04: Negative GET request for non-existent resource /users/23
        Validates: HTTP 404 Not Found and empty response body shape {}.
        """
        response = requests.get(f"{BASE_URL}/users/23", headers=HEADERS)
        
        # 1. Status Code Assertion
        assert response.status_code == 404, f"Expected 404 Not Found but got {response.status_code}"
        
        # 2. Response Body Shape Assertion
        body = response.json()
        assert body == {}, f"Expected empty dictionary for 404 but got {body}"

    def test_05_update_user_put_successful(self):
        """
        API-05: Successful PUT request to update user /users/2
        Validates: HTTP 200 OK and updatedAt timestamp.
        """
        payload = {
            "name": "Vishwa Vijay Kumar",
            "job": "Lead QA Engineer"
        }
        response = requests.put(f"{BASE_URL}/users/2", headers=HEADERS, json=payload)
        
        assert response.status_code == 200
        body = response.json()
        assert body.get("name") == payload["name"]
        assert body.get("job") == payload["job"]
        assert "updatedAt" in body
