from rest_framework.permissions import BasePermission

class MyPermissionEx(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET': # show only get permission apis not others
            return True
        return False