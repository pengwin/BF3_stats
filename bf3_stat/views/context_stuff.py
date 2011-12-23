__author__ = 'pengwin4'

from django.template import loader,RequestContext
from django.http import HttpResponse

image_url = "http://dl.dropbox.com/u/48383441/images/bf3"

def custom_processor(request):
    """
    Custom context processor that provides addition info
    """
    return { 'image_url' : image_url}

def my_render_to_response(request, template, data_dict={}):
    """
    My implementation of render_to_response with custom context processor
    """
    template = loader.get_template(template)
    context = RequestContext(request,data_dict,processors=[custom_processor])
    return HttpResponse(template.render(context))
  