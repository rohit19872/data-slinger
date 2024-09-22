from .auth import Auth

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Create an instance of Auth once when the middleware is initialized
        self.auth = Auth()

    def __call__(self, request):
        # Attach the already created class instance to the request object
        request.auth = self.auth

        # Pass the request to the next middleware/view
        response = self.get_response(request)
        return response