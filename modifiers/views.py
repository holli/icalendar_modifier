# from IPython import embed # use embed() to start a console
import requests

from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
import urllib
from dateutil import parser
import re
import datetime
import icalendar


def index(request):
    # return HttpResponse('<pre>Hello world</pre>')
    org_url = request.GET.get('ical_url')
    res_url = ''
    if org_url:
        # embed()
        org_url = org_url.replace('webcal://', 'http://')
        org_url_enc = urllib.parse.quote(org_url)
        res_url = 'http://' + get_current_site(request).name + '/show?ical_url=' + org_url_enc
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
    
    # copy_headers = ['content-disposition', 'content-encoding', 'date', 'content-type']
    copy_headers = ['content-disposition', 'date', 'content-type']
    for key in copy_headers:
        response[key] = req_ical.headers[key]

    result = ''

    # import ipdb; ipdb.set_trace()

    ical = icalendar.Calendar.from_ical(req_ical.text)
    # for it in ical.walk():
    # for it in ical.items():
    old_components = ical.subcomponents
    ical.subcomponents = []

    for sc in old_components:

        if type(sc) != icalendar.cal.Event:
            ical.subcomponents.append(sc)

        start_time = sc['DTSTART'].dt.replace(tzinfo=None)
        end_time = sc['DTEND'].dt.replace(tzinfo=None)
        # if end_time < datetime.datetime.now():
        #     continue
        if end_time > start_time + datetime.timedelta(days=3):
            modified = True
            sc.__delitem__('DTEND')
            sc.add('DTEND', start_time + datetime.timedelta(days=3))
            print("Modified DTEND: " + sc['UID'])
        if sc['DESCRIPTION'] and len(sc['DESCRIPTION']) > 300:
            modified = True
            src = sc['DESCRIPTION']
            sc.__delitem__('DESCRIPTION')
            sc.add('DESCRIPTION', src[0:190] + "..." + src[-100:-1])
            print("Modified DESC: " + sc['UID'])

        ical.subcomponents.append(sc)

    result = ical.to_ical()

    response.write(result)
    
    return response 


# def db(request):
#     greeting = Greeting()
#     greeting.save()
#     greetings = Greeting.objects.all()
#     return render(request, 'db.html', {'greetings': greetings})

