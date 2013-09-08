$(document).ready -> 
  window.week_idx = window.weeks.length - 1
  displayCurrentWeek()

  $('.ttip').tooltip
      'html': true,

  $('.popper').popover()

  $('.checkbox').click ->
    $(this).toggleClass('checked')

    value = 1
    day = "05092013"
    if $(this).html() == ''
      $(this).html('•')
    else
      $(this).html('')
    $.post '/update_virtue/' + day + "/", 
      {
        virtue: 'silence',
        value: value
      },
      (data) ->
        console.log data

row_nums = {
  'temperance': 1,
  'silence': 2,
  'order': 3,
  'resolution': 4,
  'frugality': 5,
  'industry': 6,
  'sincerity': 7,
  'justice': 8,
  'moderation': 9,
  'cleanliness': 10,
  'tranquility': 11,
  'chastity': 12,
  'humility': 13
}

displayCurrentWeek = ->
  current_week = weeks[week_idx]
  $('.checkbox').removeClass('checked').html('')

  console.log current_week
  for day in current_week['days']
    for virtue, status of day
      if virtue == 'date'
        continue
      
      if status == 1
        day_idx = new Date(day['date'] + " 12:00").getDay() + 2 # Handle indexing, extra one
        console.log day_idx, row_nums[virtue]
        $("table tr:nth-child(#{row_nums[virtue]}) td:nth-child(#{day_idx})").addClass('checked').html('•')
        
