class PermissionManager:
    def __init__(self):
        self.permissions = {}

    def set_permission(self, user_role, feature, allowed):
        if user_role not in self.permissions:
            self.permissions[user_role] = {}
        self.permissions[user_role][feature] = allowed

    def check_permission(self, user_role, feature):
        return self.permissions.get(user_role, {}).get(feature, False)

    def get_permissions(self, user_role):
        return self.permissions.get(user_role, {})