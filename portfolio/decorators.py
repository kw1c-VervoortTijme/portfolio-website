from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def in_editor_group(user):
    return user.groups.filter(name='Editors').exists() or user.is_superuser

def group_required(group_names):
    """Decorator that checks if a user is in required groups"""
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    return view_func(request, *args, **kwargs)
                if isinstance(group_names, str):
                    groups = [group_names]
                else:
                    groups = group_names
                if request.user.groups.filter(name__in=groups).exists():
                    return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapper
    return decorator
