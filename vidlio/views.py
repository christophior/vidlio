from django.http import HttpResponse

def home(request):
    html = "<html><body><a href=\"/register\">REGISTER</a></br><a href=\"/login\">LOGIN</a></body></html>"
    return HttpResponse(html)