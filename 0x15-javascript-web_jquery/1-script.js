/*
script that updates the text color
of the HTML tag HEADER to red (#FF0000):
You can’t use document.querySelector
*/

const $ = window.$;
$(document).ready(function () {
  $('header').css('color', '#FF0000');
});
