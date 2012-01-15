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
		    'graphHeroPosition': 0,
		    'graphPoints': [],
		    'graphImages': {},
		    'data': {},
		    'userName': '',
		    'currentSection': 'everyone',
		    'graphOverallMax': 0
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

			if( canvas.getContext )
			{
			    //setInterval( run , 33 );
			}
			
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