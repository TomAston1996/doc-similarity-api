'''
Document Router Integration Test
Author: Tom Aston
'''

#external dependencies
from fastapi.testclient import TestClient


def test_create_document(client: TestClient):
    '''
    Test creating a document record
    '''
    response = client.post(
        '/document',
        json={'title': 'test', 'content': 'test'}
    )

    response_json = response.json()

    assert response.status_code == 200
    assert response_json['id'] > 0
    assert response_json['title'] == 'test'
    assert response_json['content'] == 'test'
