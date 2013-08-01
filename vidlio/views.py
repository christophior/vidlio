from django.http import HttpResponse

def home(request):
    html = "<html><body>Home page.</body></html>"
    return HttpResponse(html)