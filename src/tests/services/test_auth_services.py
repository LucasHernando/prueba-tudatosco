import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import pytest
from http import HTTPStatus
from services.user_services import AuthServices
from utils.objects_model import Attributes, MessagesUsersServices

@pytest.fixture
def auth_service():
    return AuthServices()

def test_service_user_create_success(monkeypatch, auth_service):
    user_data = {
        Attributes.EMAIL_ATTRIBUTE: "test@example.com",
        Attributes.PASSWORD_ATTRIBUTE: "password123"
    }

    class MockUser:
        email = user_data[Attributes.EMAIL_ATTRIBUTE]

    monkeypatch.setattr(auth_service.user_querys, "create_user", lambda data: MockUser())

    result = auth_service.service_user_create(user_data.copy())

    assert result.status == HTTPStatus.CREATED
    assert result.message == MessagesUsersServices.CREATION_USER
    assert result.data[0][Attributes.ID_ATTRIBUTE] == user_data[Attributes.EMAIL_ATTRIBUTE]

def test_service_user_create_validation_error(auth_service):
    invalid_data = {
        Attributes.EMAIL_ATTRIBUTE: "bad_email",
        Attributes.PASSWORD_ATTRIBUTE: ""
    }

    result = auth_service.service_user_create(invalid_data.copy())

    assert result.status == HTTPStatus.BAD_REQUEST
    assert result.message == MessagesUsersServices.ERROR_VALIDATE_CREATE_USER
    assert Attributes.ERROR_ATTRIBUTE in result.errors[0]

def test_validate_login_success(monkeypatch, auth_service):
    user_data = {
        Attributes.EMAIL_ATTRIBUTE: "user@example.com",
        Attributes.PASSWORD_ATTRIBUTE: "password123"
    }

    class MockUser:
        password = "$2b$12$KIXL8Z0Mb1kQ9mCm2gqVReXbD1.QNymLflqGp1ufThK9mEeYJdpNe"
        email = user_data[Attributes.EMAIL_ATTRIBUTE]
        id = 1

    monkeypatch.setattr(auth_service.user_querys, "get_user_by_email", lambda email: MockUser())
    monkeypatch.setattr("services.user_services.check_password_hash", lambda h, p: True)
    monkeypatch.setattr("services.user_services.create_access_token", lambda **kwargs: "fake-token")
    monkeypatch.setattr("services.user_services.build_jwt_data", lambda user: {"roles": []})

    result = auth_service.validate_login(user_data)

    assert result.status == HTTPStatus.OK
    assert "access_token" in result.data

def test_validate_login_fail(monkeypatch, auth_service):
    user_data = {
        Attributes.EMAIL_ATTRIBUTE: "user@example.com",
        Attributes.PASSWORD_ATTRIBUTE: "wrongpass"
    }

    monkeypatch.setattr(auth_service.user_querys, "get_user_by_email", lambda email: None)

    result = auth_service.validate_login(user_data)

    assert result.status == HTTPStatus.NOT_FOUND
    assert result.message == MessagesUsersServices.CREDENTIALS_INVALID

def test_service_detail_user_events_success(monkeypatch, auth_service):
    class MockRegistration:
        def __init__(self, event):
            self.event = event

    class MockUser:
        email = "test@example.com"
        active = True
        roles = ["ADMIN"]
        registrations = [MockRegistration(event="Evento 1")]

    monkeypatch.setattr("services.user_services.get_jwt_identity", lambda: 1)

    monkeypatch.setattr(auth_service.user_querys, "get_user_by_id", lambda uid: MockUser())

    class MockSchema:
        def dump(self, user_data):
            return {"email": user_data["email"]}

    monkeypatch.setattr("services.user_services.user_detail_schema", MockSchema())

    result = auth_service.serivce_detail_user_events()

    assert result.status == HTTPStatus.OK
    assert result.data["email"] == "test@example.com"



def test_service_detail_user_events_not_found(monkeypatch, auth_service):
    monkeypatch.setattr("services.user_services.get_jwt_identity", lambda: 999)
    monkeypatch.setattr(auth_service.user_querys, "get_user_by_id", lambda uid: None)

    result = auth_service.serivce_detail_user_events()

    assert result.status == HTTPStatus.NOT_FOUND
    assert Attributes.USER_ATTRIBUTE
