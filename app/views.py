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
  # Get all the days between today and 10 days before
  # user signed up
  days = user.days.all()

  if not days:
    used_dates = []
  used_dates = [day.date for day in days]

  today = datetime.date.today()

  # set first date checked
  currently_checked_date = user.date_joined.date() - datetime.timedelta(days=10)

  while currently_checked_date < today:
    if currently_checked_date not in used_dates:
      day = Day(user=user, date=currently_checked_date)
      day.save()

      days.append(day)

    currently_checked_date = currently_checked_date + datetime.timedelta(days=1)

  return days
