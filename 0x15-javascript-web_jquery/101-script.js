$(function() {
  const ul = $('ul.my_list');
  $('div#add_item').on('click', () => {
    ul.append($('<li>Item</li>'));
  });
  $('div#remove_item').on('click', () => {
    $('ul.my_list :last-child').remove()
  })
  $('div#clear_list').on('click', () => {
    ul.empty();
  });
});
