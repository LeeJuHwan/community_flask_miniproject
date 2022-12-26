/*
	Fractal by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			xlarge:   [ '1281px',  '1680px' ],
			large:    [ '981px',   '1280px' ],
			medium:   [ '737px',   '980px'  ],
			small:    [ '481px',   '736px'  ],
			xsmall:   [ '361px',   '480px'  ],
			xxsmall:  [ null,      '360px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Mobile?
		if (browser.mobile)
			$body.addClass('is-mobile');
		else {

			breakpoints.on('>medium', function() {
				$body.removeClass('is-mobile');
			});

			breakpoints.on('<=medium', function() {
				$body.addClass('is-mobile');
			});

		}

	// Scrolly.
		$('.scrolly')
			.scrolly({
				speed: 1500
			});

})(jQuery);

var Target = document.getElementById("clock");
var Target_apm = document.getElementById("apm");
function clock() {
    var time = new Date();
    var hours = time.getHours();
    var minutes = time.getMinutes();
    var seconds = time.getSeconds();
    var AmPm ="AM";
    if(hours > 12){   
        var AmPm ="PM";
        hours %= 12;
    }

    Target.innerText = 
    `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}`;

    Target_apm.innerText = `${AmPm}`;

}

clock();
setInterval(clock, 1000); // 1초마다 실행


document.querySelectorAll('.logoutButton').forEach(button => {
	button.state = 'default'
  
	// function to transition a button from one state to the next
	let updateButtonState = (button, state) => {
	  if (logoutButtonStates[state]) {
		button.state = state
		for (let key in logoutButtonStates[state]) {
		  button.style.setProperty(key, logoutButtonStates[state][key])
		}
	  }
	}
  
	// mouse hover listeners on button
	button.addEventListener('mouseenter', () => {
	  if (button.state === 'default') {
		updateButtonState(button, 'hover')
	  }
	})
	button.addEventListener('mouseleave', () => {
	  if (button.state === 'hover') {
		updateButtonState(button, 'default')
	  }
	})
  
	// click listener on button
	button.addEventListener('click', () => {
	  if (button.state === 'default' || button.state === 'hover') {
		button.classList.add('clicked')
		updateButtonState(button, 'walking1')
		setTimeout(() => {
		  button.classList.add('door-slammed')
		  updateButtonState(button, 'walking2')
		  setTimeout(() => {
			button.classList.add('falling')
			updateButtonState(button, 'falling1')
			setTimeout(() => {
			  updateButtonState(button, 'falling2')
			  setTimeout(() => {
				updateButtonState(button, 'falling3')
				setTimeout(() => {
				  button.classList.remove('clicked')
				  button.classList.remove('door-slammed')
				  button.classList.remove('falling')
				  updateButtonState(button, 'default')
				}, 1000)
			  }, logoutButtonStates['falling2']['--walking-duration'])
			}, logoutButtonStates['falling1']['--walking-duration'])
		  }, logoutButtonStates['walking2']['--figure-duration'])
		}, logoutButtonStates['walking1']['--figure-duration'])
	  }
	})
  })
  
  const logoutButtonStates = {
	'default': {
	  '--figure-duration': '100',
	  '--transform-figure': 'none',
	  '--walking-duration': '100',
	  '--transform-arm1': 'none',
	  '--transform-wrist1': 'none',
	  '--transform-arm2': 'none',
	  '--transform-wrist2': 'none',
	  '--transform-leg1': 'none',
	  '--transform-calf1': 'none',
	  '--transform-leg2': 'none',
	  '--transform-calf2': 'none'
	},
	'hover': {
	  '--figure-duration': '100',
	  '--transform-figure': 'translateX(1.5px)',
	  '--walking-duration': '100',
	  '--transform-arm1': 'rotate(-5deg)',
	  '--transform-wrist1': 'rotate(-15deg)',
	  '--transform-arm2': 'rotate(5deg)',
	  '--transform-wrist2': 'rotate(6deg)',
	  '--transform-leg1': 'rotate(-10deg)',
	  '--transform-calf1': 'rotate(5deg)',
	  '--transform-leg2': 'rotate(20deg)',
	  '--transform-calf2': 'rotate(-20deg)'
	},
	'walking1': {
	  '--figure-duration': '300',
	  '--transform-figure': 'translateX(11px)',
	  '--walking-duration': '300',
	  '--transform-arm1': 'translateX(-4px) translateY(-2px) rotate(120deg)',
	  '--transform-wrist1': 'rotate(-5deg)',
	  '--transform-arm2': 'translateX(4px) rotate(-110deg)',
	  '--transform-wrist2': 'rotate(-5deg)',
	  '--transform-leg1': 'translateX(-3px) rotate(80deg)',
	  '--transform-calf1': 'rotate(-30deg)',
	  '--transform-leg2': 'translateX(4px) rotate(-60deg)',
	  '--transform-calf2': 'rotate(20deg)'
	},
	'walking2': {
	  '--figure-duration': '400',
	  '--transform-figure': 'translateX(17px)',
	  '--walking-duration': '300',
	  '--transform-arm1': 'rotate(60deg)',
	  '--transform-wrist1': 'rotate(-15deg)',
	  '--transform-arm2': 'rotate(-45deg)',
	  '--transform-wrist2': 'rotate(6deg)',
	  '--transform-leg1': 'rotate(-5deg)',
	  '--transform-calf1': 'rotate(10deg)',
	  '--transform-leg2': 'rotate(10deg)',
	  '--transform-calf2': 'rotate(-20deg)'
	},
	'falling1': {
	  '--figure-duration': '1600',
	  '--walking-duration': '400',
	  '--transform-arm1': 'rotate(-60deg)',
	  '--transform-wrist1': 'none',
	  '--transform-arm2': 'rotate(30deg)',
	  '--transform-wrist2': 'rotate(120deg)',
	  '--transform-leg1': 'rotate(-30deg)',
	  '--transform-calf1': 'rotate(-20deg)',
	  '--transform-leg2': 'rotate(20deg)'
	},
	'falling2': {
	  '--walking-duration': '300',
	  '--transform-arm1': 'rotate(-100deg)',
	  '--transform-arm2': 'rotate(-60deg)',
	  '--transform-wrist2': 'rotate(60deg)',
	  '--transform-leg1': 'rotate(80deg)',
	  '--transform-calf1': 'rotate(20deg)',
	  '--transform-leg2': 'rotate(-60deg)'
	},
	'falling3': {
	  '--walking-duration': '500',
	  '--transform-arm1': 'rotate(-30deg)',
	  '--transform-wrist1': 'rotate(40deg)',
	  '--transform-arm2': 'rotate(50deg)',
	  '--transform-wrist2': 'none',
	  '--transform-leg1': 'rotate(-30deg)',
	  '--transform-leg2': 'rotate(20deg)',
	  '--transform-calf2': 'none'
	}
  }
  