import pytest
import requests


# pytest tests\health\test_health.py -v -s

def test_health():
    response = requests.get("https://gorest.co.in/public/v2/users")
    assert response.ok == True
