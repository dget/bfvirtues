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
      'weekdays': [
        {'letter': 'S'},
        {'letter': 'M'},
        {'letter': 'T'},
        {'letter': 'W'},
        {'letter': 'R'},
        {'letter': 'F'},
        {'letter': 'S'},
      ],
      'virtues': [
        {'name': 'Temperance', 'description': 'Eat not to dullness; drink not to elevation.'},
        {'name': 'Silence', 'description': 'Speak not but what may benefit others or yourself; avoid trifling conversation.'},
        {'name': 'Order', 'description': 'Let all your things have their places; let each part of your business have its time.'},
        {'name': 'Resolution', 'description': 'Resolve to perform what you ought; perform without fail what you resolve.'},
        {'name': 'Frugality', 'description': 'Make no expense but to do good to others or yourself; i.e., waste nothing.'},
        {'name': 'Industry', 'description': 'Lose no time; be always employ\'d in something useful; cut off all unnecessary actions.'},
        {'name': 'Sincerity', 'description': 'Use no hurtful deceit; think innocently and justly, and, if you speak, speak accordingly.'},
        {'name': 'Justice', 'description': 'Wrong none by doing injuries, or omitting the benefits that are your duty.'},
        {'name': 'Moderation', 'description': 'Avoid extremes; forbear resenting injuries so much as you think they deserve.'},
        {'name': 'Cleanliness', 'description': 'Tolerate no uncleanliness in body, cloaths, or habitation.'},
        {'name': 'Tranquillity', 'description': 'Be not disturbed at trifles, or at accidents common or unavoidable.'},
        {'name': 'Chastity', 'description': 'Rarely use venery but for health or offspring, never to dullness, weakness, or the injury of your own or another\'s peace or reputation.'},
        {'name': 'Humility', 'description': 'Imitate Jesus and Socrates.'},
      ]
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

    currently_checked_date = currently_checked_date + datetime.timedelta(days=1)

  return days
