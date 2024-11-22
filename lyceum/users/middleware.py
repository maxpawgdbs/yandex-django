__all__ = ()
import users.models


class BestMiddlewareForDanila:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user = users.models.ProxyUser.objects.get(id=request.user.id)
            request.user = user

        return self.get_response(request)
