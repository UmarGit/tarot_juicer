from django.http import HttpResponseRedirect
from django.urls import reverse

from accounts.models import AuthToggle


def authentication_middleware(get_response):
    def middleware(request):
        auth_toggle = AuthToggle.objects.first()
        if auth_toggle:
            pass
        else:
            auth = AuthToggle.objects.create(active = False) 
            auth.save() 
        if auth_toggle :
            if auth_toggle.active:  # authentication NOT required
                if request.path == reverse('index') and request.user.is_authenticated:
                    return HttpResponseRedirect(reverse('portal'))
            else:  # authentication required
                if not request.user.is_authenticated and \
                        request.path not in [reverse('index'), reverse('register')] and \
                        not request.path.startswith(reverse('admin:index')):
                    return HttpResponseRedirect(reverse('index'))

        response = get_response(request)

        return response

    return middleware
