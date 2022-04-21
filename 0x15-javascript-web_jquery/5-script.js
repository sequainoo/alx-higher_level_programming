$('div#add_item').on('click', function() {
  let li = $('<li>Item</li>');
  li.appendTo($('ul.my_list'));
});
