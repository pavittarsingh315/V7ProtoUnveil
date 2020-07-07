from django.http import Http404

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func