from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify
from utils.objects_model import Attributes,MessagesPermissionssServices
from utils.http_response import http_response
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity
from models.user_model import User

def permission_required(required_permission):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)

            user_permissions = set()
            for role in user.roles:
                for perm in role.permissions:
                    user_permissions.add(perm.name)
                    
            if required_permission in user_permissions:
                return fn(*args, **kwargs)
            return http_response(message=MessagesPermissionssServices.ACTION_DENIED, data={}, status=HTTPStatus.FORBIDDEN, errors=[])
        return decorator
    return wrapper
