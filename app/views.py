# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
  print 'hi'
  return HttpResponse('Hello World')