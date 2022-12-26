const toggleBtn = document.querySelector('.navbar-toggle');
const menu = document.querySelector('.sidebar_to_row');

toggleBtn.addEventListener('click',() => {
    menu.classList.toggle('active');
});

// $(document).ready(function(){
//     $(".sub").hide();
//     $(".content").click(function(){
//         $(".sub",this).slideToggle("fast");
//     });
// });

( function( $ ) {
    $('.cate ul').hide();
    $('.cate .menu .subopen').click(function() {
      if($(this).hasClass('active')){
         $(this).parent().next().slideUp('slow');
         $(this).removeClass('active');
      }else{
        $('.accordion').find('.active').parent().next().slideUp('slow');
        $('.accordion').find('.active').removeClass('active');
        $(this).parent().next().slideDown('slow');
        $(this).addClass('active');
      }     
     
     });
  })( jQuery );



// $(".top_menu").click(function() {
//     $(this).next(".bottom_menu").stop().slideToggle(300);
//     $(this).toggleClass('on').siblings(".bottom_menu").removeClass('on');
//     $(this).next(".bottom_menu").siblings(".bottom_menu").slideUp(300); // 1개씩 펼치기
// });




// $('.hamburger-button').click(function(event){
//     event.preventDefault();
//     $(this).toggleClass('active');
// });


// 	// <![CDATA[  <-- For SVG support
// 	if ('WebSocket' in window) {
// 		(function () {
// 			function refreshCSS() {
// 				var sheets = [].slice.call(document.getElementsByTagName("link"));
// 				var head = document.getElementsByTagName("head")[0];
// 				for (var i = 0; i < sheets.length; ++i) {
// 					var elem = sheets[i];
// 					var parent = elem.parentElement || head;
// 					parent.removeChild(elem);
// 					var rel = elem.rel;
// 					if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
// 						var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
// 						elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
// 					}
// 					parent.appendChild(elem);
// 				}
// 			}
// 			var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
// 			var address = protocol + window.location.host + window.location.pathname + '/ws';
// 			var socket = new WebSocket(address);
// 			socket.onmessage = function (msg) {
// 				if (msg.data == 'reload') window.location.reload();
// 				else if (msg.data == 'refreshcss') refreshCSS();
// 			};
// 			if (sessionStorage && !sessionStorage.getItem('IsThisFirstTime_Log_From_LiveServer')) {
// 				console.log('Live reload enabled.');
// 				sessionStorage.setItem('IsThisFirstTime_Log_From_LiveServer', true);
// 			}
// 		})();
// 	}
// 	else {
// 		console.error('Upgrade your browser. This Browser is NOT supported WebSocket for Live-Reloading.');
// 	}
// 	// ]]>