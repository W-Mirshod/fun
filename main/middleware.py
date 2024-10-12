from django.conf import settings

from django.shortcuts import redirect


class LoginRequiredMiddleware:
    """
    Middleware to require login for all views except the Django admin page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (request.path.startswith('/admin-page/') or request.path.startswith('/auth/login/')
                or request.path.startswith('/auth/login/')):
            return self.get_response(request)

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        response = self.get_response(request)
        return response
