from django.http import HttpResponse

def home(request):
<<<<<<< HEAD
    html = "<html><body><a href=\"/register\">REGISTER</a></br><a href=\"/login\">LOGIN</a></br><a href=\"/admin\">ADMIN PANEL</a></body></html>"
=======
    html = "<html><body>Home page.</body></html>"
>>>>>>> f676ec14194b28199658d4e7fe54d0db3101cf60
    return HttpResponse(html)