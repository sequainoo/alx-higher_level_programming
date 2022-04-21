let url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function(data, textStatus) {
	console.log(data);
  const ul = $('ul#list_movies');
  for (const film of data.results) {
    $(`<li>${film.title}</li>`).appendTo(ul);
  }
});
