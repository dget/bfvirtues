# Create your views here.

import datetime
from dateutil.rrule import rrule, DAILY

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from app.models import Day

def index(request):
  if request.user.is_authenticated():
    user = request.user
    print 'user is logged in', user.username
    user = User.objects.get(id=user.id)  # was being annoying.

    now = datetime.datetime.now()

    days = get_user_days(user)

    context = {
      'user': user,
      'now': now,
    }
    return render_to_response('index_app.jade', context)
  else:
    return render_to_response('index.jade', {})


def logged_in(request):
  print 'in logged_in with ', request

  return HttpResponseRedirect('/')


def get_user_days(user):
  days = user.days.all()

  if not days:
    today = datetime.date.today()
    # http://stackoverflow.com/a/1622052/1048433
    most_recent_sunday = today - datetime.timedelta(days=today.weekday() - 1)
    for date in rrule(DAILY, dtstart=most_recent_sunday, until=today):
      pass

  return days