from django.conf import settings

from django.shortcuts import redirect


class LoginRequiredMiddleware:
    """
    Middleware to require login for all views except the Django admin page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (request.path.startswith('/admin-page/') or request.path.startswith('/auth/sign-up/')
                or request.path.startswith('/auth/login/')):
            return self.get_response(request)

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        response = self.get_response(request)
        return response


from django.utils import timezone


class SessionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store session start time when session starts
        if 'start_time' not in request.session:
            request.session['start_time'] = timezone.now().timestamp()

        # Process the view
        response = self.get_response(request)

        # Calculate total time spent at the end of the session or after certain views
        if request.user.is_authenticated:
            session_start = request.session['start_time']
            # Calculate time spent on the current request
            time_spent = int(timezone.now().timestamp() - session_start)
            # Store the time spent for the current page view
            request.session['total_time_spent'] = request.session.get('total_time_spent', 0) + time_spent

            # Optionally update start time to now for the next request
            request.session['start_time'] = timezone.now().timestamp()

        return response
