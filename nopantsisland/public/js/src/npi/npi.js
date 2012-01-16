// FIXME -> this file should probably done without jquery and backbone, and all the intro code should be moved to it's own module
define( 'npi', 
	['underscore', 'npi/sky'],
	function( _, sky ) {
	    
	    var NPI = {
		'publicFn': {
		    'init': function( bodyClass ) {
			NPI.privateFn.setup( bodyClass );
		    }
		},
		'privateFn': {
		    'setup': function( bodyClass ) {
			// eventually, bodyClass can be used to load different setup functions depending on the page.  kinda hacky.
			sky.init();
			console.log("activated");
		    }
		}
	    };
	    
	    return NPI.publicFn;
	}
      );
