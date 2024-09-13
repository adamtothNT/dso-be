import sys
import os
import pytest
from app import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_receive_message(client):
    # Simulate sending a POST request with a message
    response = client.post('/api/message', json={'message': 'Hello World'})
    assert response.status_code == 200
    assert response.get_json()['response'] == 'Received and stored: Hello World'


def test_get_messages(client):
    # Simulate retrieving stored messages
    response = client.get('/api/messages')
    assert response.status_code == 200
    # Check that the response is a list (could add more assertions as needed)
    assert isinstance(response.get_json(), list)
