#from IPython import embed # use embed() to start a console
import requests

from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
import urllib
from dateutil import parser
import re
import datetime


def index(request):
    # return HttpResponse('<pre>Hello world</pre>')
    org_url = request.GET.get('ical_url')
    res_url = ''
    if org_url:
        res_url = 'http://' + get_current_site(request).name + '/show?ical_url=' + urllib.quote(org_url)
    else:
        org_url = ''
    return render(request, 'index.html', {'res_url': res_url, 'org_url': org_url})


def show(request):
    #ical_url = 'http://httpbin.org/status/418'
    ical_url = request.GET.get('ical_url')
    req_ical = requests.get(ical_url)
    #return HttpResponse('<pre>' + r.text + '</pre>')
    # response = HttpResponse(req_ical)
    response = HttpResponse()
    
    copy_headers = ['content-disposition', 'content-encoding', 'date', 'content-type']
    # copy_headers = ['content-disposition', 'date', 'content-type']
    for key in copy_headers:
        response[key] = req_ical.headers[key]

    result = ''
    lines = req_ical.text.split('\r\n')
    for i in range(len(lines)-1):
        start_str = re.search("DTSTART:(.*Z)", lines[i])
        end_str = re.search("DTEND:(.*Z)", lines[i+1])

        if bool(start_str) and bool(end_str):
            start_time = parser.parse(start_str.group(1))
            end_time =  parser.parse(end_str.group(1))
            if (end_time-start_time) > datetime.timedelta(days = 4):
                new_end_time = (start_time + datetime.timedelta(hours = 2)).strftime('%Y%m%dT%H%M%SZ')
                lines[i+1] = lines[i+1].replace(end_str.group(1), new_end_time)
                lines[i+3] = lines[i+3].replace("SUMMARY:", "SUMMARY:(CUT)")
                print(lines[i+3])
        result += lines[i] + "\n"
    result += lines[len(lines)-1] + "\n"

    response.write(result)
    
    return response 


# def db(request):
#     greeting = Greeting()
#     greeting.save()
#     greetings = Greeting.objects.all()
#     return render(request, 'db.html', {'greetings': greetings})

