
$('.ttip').tooltip
    'html': true,

$('.popper').popover()

$('.checkbox').click ->
  $(this).addClass('checked')
  $(this).html('•')