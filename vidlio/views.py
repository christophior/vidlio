from django.http import HttpResponse
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


def home(request):
    html = "<html><body><a href=\"/register\">REGISTER</a></br><a href=\"/login\">LOGIN</a></br><a href=\"/admin\">ADMIN PANEL</a></body></html>"
    return HttpResponse(html)


# @login_required
# def get_profile(request):
#     url = request.user.profile.url


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail