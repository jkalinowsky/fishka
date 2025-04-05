import pytest
from fastapi.testclient import TestClient
from fastapi import status, HTTPException
from unittest.mock import patch, MagicMock, AsyncMock
from app.main import app
from app.database import get_db
from app.views.deck_views import validate_access
from app.services.deck_service import create_deck_service
from app.services.temp_user_service import check_access
from sqlalchemy.orm import Session

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_db():
    mock_session = MagicMock(spec=Session)
    app.dependency_overrides[get_db] = lambda: mock_session
    yield mock_session
    app.dependency_overrides.clear()

@pytest.fixture
def mock_check_access():
    with patch('app.views.deck_views.check_access', return_value=(True, 'Access granted.')) as mock:
        yield mock

@pytest.fixture
def mock_validate_access():
    async def mock_validation(request, db):
        return {
            'name': '<NAME>',
            'flashcards': [],
            'session_id': 'valid_session_id',
            'folder_id': 1,
        }
    with patch('app.views.deck_views.validate_access', new=mock_validation):
        yield

@pytest.fixture
def mock_create_deck_service():
    with patch('app.services.deck_service.create_deck_service') as mock:
        yield mock

def test_create_deck_valid(client, mock_check_access, mock_validate_access, mock_create_deck_service):
    mock_create_deck_service.return_value = (True, None)

    request_data = {
        'name': '<NAME>',
        'flashcards': [],
        'session_id': 'valid_session_id',
        'folder_id': 1,
    }

    response = client.post("/create-deck", json=request_data)
    print(response.json())

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"Message": "Ok"}

#def test_create_deck_invalid(client, mock_check_access, mock_create_deck_service):