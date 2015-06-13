import requests

from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse

# from .models import Greeting
from IPython import embed # use embed() to start a console
import urllib

# Create your views here.

def index(request):
    # return HttpResponse('<pre>Hello world</pre>')
    org_url = request.GET.get('ical_url')
    #res_url = url('asdf', {ical_url: urllib.quote(org_url)})
    res_url = 'http://' + get_current_site(request).name + '/show?ical_url=' + urllib.quote(org_url)
    return render(request, 'index.html', {'res_url': res_url, 'org_url': org_url})

def show(request):
    #ical_url = 'http://httpbin.org/status/418'
    ical_url = request.GET.get('ical_url')
    req_ical = requests.get(ical_url)
    #return HttpResponse('<pre>' + r.text + '</pre>')
    response = HttpResponse(req_ical)

    copy_headers = ['content-disposition', 'content-encoding', 'date', 'content-type']
    # copy_headers = ['content-disposition', 'date', 'content-type']
    for key in copy_headers:
        response[key] = req_ical.headers[key]
    return response 


# def db(request):
#     greeting = Greeting()
#     greeting.save()
#     greetings = Greeting.objects.all()
#     return render(request, 'db.html', {'greetings': greetings})

