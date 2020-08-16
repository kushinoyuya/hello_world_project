from django.http import HttpResponse
from django.view.generic import TemplateView

def helloworldfunction(request):
    returnobject = HttpResponse('<h1>hello world</h1>')
    return returnobject

class HelloWorldView(TemplateView):
    template_name = 'hello.html'
