# Create your views here.
from urllib import urlencode
from urllib2 import urlopen,  URLError, HTTPError
import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings

def home(request):
    html = "<html><body>Its a test</body></html>"
    return HttpResponse(html)
