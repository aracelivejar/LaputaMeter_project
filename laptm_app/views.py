from django.http import HttpResponse
from django.template import loader


def laptm_app(request):
    template = loader.get_template('laptmhtml.html')
    return HttpResponse(template.render())
