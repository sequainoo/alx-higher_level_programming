$(function() {
  const urlBase = 'https://fourtonfish.com/hellosalut/?lang=';
  $('input#btn_translate').on('click', () => {
    const lang = $('input#language_code').val();
    $.get(urlBase + lang, (data, textStatus) => {
      $('div#hello').text(data.hello);
    });
  });
  $('input#language_code').on('keypress', (event) => {
    if(event.which == 13) {
      const lang = $('input#language_code').val();
      $.get(urlBase + lang, (data, textStatus) => {
        $('div#hello').text(data.hello);
      });
    }
  });
});
