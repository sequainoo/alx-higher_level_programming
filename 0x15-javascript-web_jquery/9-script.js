const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(function() {
  $.get(url, (data, textStatus) => {
    $('div#hello').text(data.hello);
  });
});
