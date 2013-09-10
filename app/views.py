# Create your views here.

import datetime
import json
from dateutil.rrule import rrule, DAILY

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from app.models import Day

def home(request):
  return render_to_response('index_home.jade', {})

def app(request):
  if request.user.is_authenticated():
    user = request.user
    print 'user is logged in', user.username
    user = User.objects.get(id=user.id)  # was being annoying.

    now = datetime.datetime.now()

    days = list(get_user_days(user))
    days.sort(key=lambda day: day.date)

    days_since_last_sunday = user.date_joined.weekday() + 2
    last_sunday_date = (user.date_joined - datetime.timedelta(days=days_since_last_sunday)).date()

    weeks = []
    for day in days:
      if day.date <= last_sunday_date:
        continue
      if len(weeks) == 0 or len(weeks[-1]['days']) == 7:
        week = {
          'start_date': str(day.date),
          'virtue': 'T',
          'days': []
        }
        weeks.append(week)

      week = weeks[-1]
      day_dict = {
          'date': str(day.date),
          'temperance': day.temperance,
          'silence': day.silence,
          'order': day.order,
          'resolution': day.resolution,
          'frugality': day.frugality,
          'industry': day.industry,
          'sincerity': day.sincerity,
          'justice': day.justice,
          'moderation': day.moderation,
          'cleanliness': day.cleanliness,
          'tranquility': day.tranquillity,
          'chastity': day.chastity,
          'humility': day.humility
      }
      week['days'].append(day_dict)

    virtues = [
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
    # weeks since year began, mod 13 b/c there's 13, minus 10 so that it starts this week! =D
    current_virtue_index = now.isocalendar()[1] % 13 - 10
    current_virtue = virtues[current_virtue_index]

    context = {
      'user': user,
      'now': now,
      'weeks': json.dumps(weeks),
      'weekdays': [
        {'letter': 'S', 'number': 0},
        {'letter': 'M', 'number': 1},
        {'letter': 'T', 'number': 2},
        {'letter': 'W', 'number': 3},
        {'letter': 'R', 'number': 4},
        {'letter': 'F', 'number': 5},
        {'letter': 'S', 'number': 6},
      ],
      'virtues': virtues,
      'current_virtue': current_virtue,
    }
    return render_to_response('index_app.jade', context)

def index(request):
  if request.user.is_authenticated():
    return app(request)
  else:
    return home(request)


def logged_in(request):
  print 'in logged_in with ', request

  return HttpResponseRedirect('/')

@csrf_exempt
def update_virtue(request, date):
  if request.method != 'POST':
    return HttpResponse("0")

  user = request.user

  virtue = request.POST['virtue']
  value = request.POST['value']

  real_date = datetime.datetime.strptime(date, "%d%m%Y").date()
  day, __ = Day.objects.get_or_create(user=user, date=real_date)

  setattr(day, virtue, value)
  day.save()
  return HttpResponse("1")


def get_user_days(user):
  # Get all the days between today and 10 days before
  # user signed up
  days = list(user.days.all())

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
