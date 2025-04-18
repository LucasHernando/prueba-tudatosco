def build_jwt_data(user):
    roles = user.roles  # user.roles -> relación con UserRoles
    permissions = set()
    for role in roles:
        for perm in role.permissions:
            permissions.add(perm.name)
    return {
        "roles": [r.name for r in roles],
        "permissions": list(permissions)
    }
