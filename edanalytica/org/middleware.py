class OrgMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user and request.user.is_authenticated:
            from org.models import Org
            org =  Org.objects.filter(users=request.user).first()
            request.org = org

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response