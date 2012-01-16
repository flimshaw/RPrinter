define( 'npi/sky', 
	['jquery', 'underscore', 'npi'],
	function( $, _ ) {
	    
	    var Sky = {
		'evt': {

		},
		'defaults': {
		    'canvasSupported': true
		},
		'cfg': {
		    'backupImages': [
			{ 'src': 'images/common/generic_icon_green.png' },
			{ 'src': 'images/common/generic_icon_yellow.png' },
			{ 'src': 'images/common/generic_icon_red.png' }
		    ],
		    'graphMax': 0,
		    'ctx': 0,
		    'gradientValues': {
			'red': 0,
			'blue': 1,
			'gold': 0
		    }
		},
		'publicFn': {
		    'init': function( options ) {
			console.log("canvas loaded.");
			if ( options ) {
			    _.extend( Sky.cfg, Sky.defaults, options, Sky.cfg );
			}
			canvas = document.getElementById("bgCanvas");
			canvas.width = document.width;
			canvas.height = document.height;
			canvasW = canvas.width;
			canvasH = canvas.height;
			if( canvas.getContext('2d') )
			{
			    Sky.cfg.ctx = canvas.getContext('2d');
			    setInterval( Sky.publicFn.run , 33 );
			}
		    },
		    'run': function() {
			if(Sky.cfg.gradientValues.gold < 1) {
			    Sky.cfg.gradientValues.gold += .01;
			} else {
			    Sky.cfg.gradientValues.gold = 1;
			    if(Sky.cfg.gradientValues.red < 1) {
				Sky.cfg.gradientValues.red += .01;
			    } else {
				Sky.cfg.gradientValues.red = 0;
				Sky.cfg.gradientValues.gold = 0;
			    }
			}
			var lg = Sky.cfg.ctx.createLinearGradient(0,0,0,canvas.height);
			lg.addColorStop(0,'#007eff'); // start with blue
			lg.addColorStop(1 - Sky.cfg.gradientValues.gold + Sky.cfg.gradientValues.red, '#007eff'); // our blue's length is determined by this thing
			lg.addColorStop(1 - Sky.cfg.gradientValues.red, '#fda110');
			lg.addColorStop(1, 'red');
			Sky.cfg.ctx.fillStyle = lg;
			Sky.cfg.ctx.fillRect(0, 0, canvas.width, canvas.height);
		    }
		},
		'privateFn': {
		    'setup': function( ) {

		    },
		    'run': function() {

		    }
		}

	};
	
	return Sky.publicFn;
      }
);