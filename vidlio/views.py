from django.http import HttpResponse


def home(request):
    html = "<html><body><a href=\"/signup\">REGISTER</a></br><a href=\"/signin\">LOGIN</a></br><a href=\"/admin\">ADMIN PANEL</a></body></html>"
    return HttpResponse(html)