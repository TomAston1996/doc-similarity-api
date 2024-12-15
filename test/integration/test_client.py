'''
Root Integration Test
Author: Tom Aston
'''

#external dependencies
from fastapi.testclient import TestClient


def test_client(client: TestClient):
    '''
    Test root
    '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == 'server is running'