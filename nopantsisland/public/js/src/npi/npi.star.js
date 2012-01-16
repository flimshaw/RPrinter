define( 'npi/star', 
	['jquery', 'underscore', 'npi'],
	function( $, _ ) {
	    
	    var Star = {
		'evt': {

		},
		'defaults': {
		    'canvasSupported': true
		},
		'cfg': {
		    'img': null,
			'id': ''
		    }
		},
		'publicFn': {
		    'init': function( options ) {
				console.log("NEW STAR YO.");
				if ( options ) {
				    _.extend( Star.cfg, Star.defaults, options, Star.cfg );
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
	
	return Star.publicFn;
      }
);