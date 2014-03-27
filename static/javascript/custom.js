$(document).ready(function() {
  $('.ui.rating').rating();

  $('.ui.dropdown').dropdown();

  $('.ui.checkbox').checkbox();

  $('.remove-serie').click(function () {
    $('.basic.modal').modal('show')
  });

  $(".rating").click(function () {
    var serie_id = $(this).attr('data-serie'),
	rating = $(this).find('.active').length,
	url = '/series/' + serie_id + rating + '/';

    $.ajax({url: url, type: 'GET'});
  });
});
