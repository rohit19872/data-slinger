from datetime import timedelta
from django.conf import settings

class SuperuserSessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Default session expiry for non-superusers from settings
        default_timeout = settings.SESSION_COOKIE_AGE

        # Check if the user is authenticated and a superuser
        if request.user.is_authenticated:
            if request.user.is_superuser:
                request.session.set_expiry(timedelta(hours=1).total_seconds())  # 1 hour for superusers
            else:
                request.session.set_expiry(default_timeout)

        return self.get_response(request)