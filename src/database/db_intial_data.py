from flask.cli import with_appcontext
import click


def register_commands(app):
    @app.cli.command("seed")
    @with_appcontext
    def seed_data():
        
        from datetime import datetime, timedelta
        from werkzeug.security import generate_password_hash
        from database.db_sqlalchemy import db
        from models.user_model import User
        from models.role_model import Role 
        from models.user_role_model import UserRoles
        from models.permission_model import Permission
        from models.role_permission_model import RolePermission
        from models.event_model import Event
        from models.session_model import Session
        from models.attendance_model import Attendance
        from utils.objects_model import Permissions
        
        
        
        # Usuarios
        user1 = User(email="admin@example.com", password=generate_password_hash("admin123"))
        user2 = User(email="organizer@example.com", password=generate_password_hash("organizer123"))
        user3 = User(email="assistant@example.com", password=generate_password_hash("assistant123"))

        # Roles
        admin_role = Role(name="ADMIN")
        organizer_role = Role(name="ORGANIZER")
        assistant_role = Role(name="ASSISTANT")

        db.session.add_all([user1, user2, user3, admin_role, organizer_role, assistant_role])
        db.session.commit()

        # Asignación de roles a usuarios
        db.session.add_all([
            UserRoles(user_id=user1.id, role_id=admin_role.id),
            UserRoles(user_id=user2.id, role_id=organizer_role.id),
            UserRoles(user_id=user3.id, role_id=assistant_role.id),
        ])

        # Permisos
        permission_objects = []
        for perm in Permissions.__dict__:
            if not perm.startswith("__") and not callable(getattr(Permissions, perm)):
                permission_objects.append(Permission(name=getattr(Permissions, perm)))
        db.session.add_all(permission_objects)
        db.session.commit()

        # Asignación lógica de permisos
        admin_permissions = permission_objects
        organizer_permissions = [p for p in permission_objects if "event" in p.name or "session" in p.name]
        assistant_permissions = [p for p in permission_objects if "registration" in p.name or "session" in p.name]

        db.session.add_all([
            *[RolePermission(role_id=admin_role.id, permission_id=p.id) for p in admin_permissions],
            *[RolePermission(role_id=organizer_role.id, permission_id=p.id) for p in organizer_permissions],
            *[RolePermission(role_id=assistant_role.id, permission_id=p.id) for p in assistant_permissions],
        ])
        db.session.commit()

        # Eventos
        estados = ['programmed', 'in_progress', 'completed', 'canceled']
        events = []
        for i, estado in enumerate(estados):
            event = Event(
                title=f"Evento {i+1}",
                description=f"Descripción del evento {i+1}",
                status=estado,
                capacity=100,
                start_date=datetime.utcnow() + timedelta(days=i),
                end_date=datetime.utcnow() + timedelta(days=i, hours=4),
                created_by=user2.id
            )
            events.append(event)

        db.session.add_all(events)
        db.session.commit()

        # Sesiones
        sessions = []
        for i, event in enumerate(events):
            session = Session(
                title=f"Sesión {i+1}",
                description=f"Descripción de la sesión {i+1}",
                start_time=event.start_date + timedelta(hours=1),
                end_time=event.start_date + timedelta(hours=3),
                capacity=50,
                room=f"Aula {i+1}",
                event_id=event.id,
                speaker_id=user3.id
            )
            sessions.append(session)

        db.session.add_all(sessions)
        db.session.commit()

        # Asistencias
        attendances = [
            Attendance(user_id=user3.id, session_id=session.id) for session in sessions
        ]
        db.session.add_all(attendances)
        db.session.commit()

        print("✅ Datos de prueba insertados correctamente.")