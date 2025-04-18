from views.user_views import UserAPI, LoginAPI
from views.role_views import RoleAPI
from views.event_views import EventAPI
from views.session_views import SessionAPI
from views.registration_views import RegisterAPI
from views.role_permission_views import RolePermissionAPI
from views.user_role_views import UserRoleAPI

def register_routes(app):
    # Rutas de usuarios
    user_view = UserAPI.as_view('user_api')
    app.add_url_rule('/api/users', view_func=user_view, methods=['POST'])
    app.add_url_rule("/api/users", view_func=user_view, methods=["GET"])
    

    # Rutas de login
    login_view = LoginAPI.as_view('login_api')
    app.add_url_rule('/api/login', view_func=login_view, methods=['POST'])
    
    
    role_view = RoleAPI.as_view("role_api")
    app.add_url_rule("/api/roles", defaults={"role_id": None}, view_func=role_view, methods=["GET"])
    app.add_url_rule("/api/roles", view_func=role_view, methods=["POST"])
    app.add_url_rule("/api/roles/<int:role_id>", view_func=role_view, methods=["GET", "PUT", "DELETE"])
    
    
    event_view = EventAPI.as_view("event_api")
    app.add_url_rule("/api/events", defaults={"event_id": None}, view_func=event_view, methods=["GET"])
    app.add_url_rule("/api/events", view_func=event_view, methods=["POST"])
    app.add_url_rule("/api/events/<int:event_id>", view_func=event_view, methods=["GET", "PUT", "DELETE"])
    
    
    session_view = SessionAPI.as_view('session_api')
    app.add_url_rule('/api/sessions', defaults={'session_id': None}, view_func=session_view, methods=['GET'])
    app.add_url_rule('/api/sessions', view_func=session_view, methods=['POST'])
    app.add_url_rule('/api/sessions/<int:session_id>', view_func=session_view, methods=['GET', 'PUT', 'DELETE'])
    
    
    registration_view = RegisterAPI.as_view('registration_api')
    app.add_url_rule('/api/registrations', defaults={'user_id': None}, view_func=registration_view, methods=['GET'])
    app.add_url_rule('/api/registrations', view_func=registration_view, methods=['POST'])
    app.add_url_rule('/api/registrations/<int:user_id>', view_func=registration_view, methods=['GET', 'DELETE'])
    
    
    role_permissions_view = RolePermissionAPI.as_view('role_permissions_api')
    app.add_url_rule('/api/role_permissions', view_func=role_permissions_view, methods=['POST', 'DELETE'])
    
    role_users_view = UserRoleAPI.as_view('role_users_api')
    app.add_url_rule('/api/role_users', defaults={'role_id': None}, view_func=role_users_view, methods=['GET'])
    app.add_url_rule('/api/role_users', view_func=role_users_view, methods=['POST', 'DELETE'])
    
    
    
    
    