from fastapi.testclient import TestClient
from fast_zero.app import app
from http import HTTPStatus

def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app) # Arrange organização

    response = client.get('/') # Act (ação)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message' : 'Olá Mundo!'}

