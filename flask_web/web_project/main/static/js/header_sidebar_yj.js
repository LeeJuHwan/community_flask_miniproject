const toggleBtn = document.querySelector('.navbar-toggle');
const menu = document.querySelector('.accordion');

toggleBtn.addEventListener('click',() => {
    menu.classList.toggle('active');
});

( function( $ ) {
  $('.cate ul').hide();
  $('.subopen').click(function() {
    $('.accordion').find('.active').children('ul').slideUp('slow');
    if($(this).hasClass('active')){
       $(this).removeClass('active');
    }else{
      $('.accordion').find('.active').removeClass('active');
      $(this).children('ul').slideDown('slow');
      $(this).addClass('active');
    }     
   
   });
})( jQuery );