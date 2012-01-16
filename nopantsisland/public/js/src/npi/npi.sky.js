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
			'gold': 0,
			'stars': []
		    }
		},
		'publicFn': {
		    'init': function( options ) {
				console.log("canvas loaded.");
				if ( options ) {
				    _.extend( Sky.cfg, Sky.defaults, options, Sky.cfg );
				}
				Sky.cfg.stars = new Array();
				
				canvas = document.getElementById("bgCanvas");
				canvas.width = document.width;
				canvas.height = document.height;
				canvasW = canvas.width;
				canvasH = canvas.height;
				if( canvas.getContext('2d') )
				{
				    Sky.cfg.ctx = canvas.getContext('2d');
				    setInterval( Sky.publicFn.run , 33 );
					star_interval = setInterval(Sky.publicFn.updateStarData, 1000)
				}
				
		    },
		    'manageTwitterStars': function(results){
				twitter_names_images_src = {
					"ashleyluvspizza": "/images/homepage/star_ah.png",
					"flimshaw": "/images/homepage/star_ch.png"
				}
				
				$.each(results, function(i, obj) {
					// iterate through current stars, see if already extant
					// none of this works because i don't know how to make classes.  i feel so foolish.
			/*	   var dupe = 0;
				   $.each(Sky.cfg.stars, function(i, star) {
				   	if (star.cfg.id == obj.id) {
				   		// it's a duplicate gtfo
				   		dupe = 1;
				   	}
				   })
				     if (!dupe) {
				     	var img = new Image();
				     	img.src = twitter_names_images_src[obj.from_user]
				   
				   		new_star = new Star(img, obj.id);
				      	Sky.cfg.stars.push(new_star)
				    	Sky.cfg.stars.push(img);
				    }
					$.each(Sky.cfg.stars, function(i, s){
						
						Sky.cfg.ctx.drawImage(s, Math.random()*canvas.width, Math.random()*canvas.height);
					})
				*/
				
				
				});
			},
		    'updateStarData': function() {
			// for now just load in twitter.  eventually maybe create a wee factory to talk to all the different inputs.
				$.ajax({
					url: 'http://search.twitter.com/search.json?q=from%3Aflimshaw OR from%3Aashleyluvspizza', 
					dataType: "jsonp",
				    type: 'GET',
				    crossDomain: true,
				    success: function(r) {
					// this should be in a Star class that i don't know how to add
						Sky.publicFn.manageTwitterStars(r.results)
					
					}
				});
			},
		    'run': function() {
				var colors = Sky.cfg.gradientValues;
				
				if(colors.gold < 1) {
				    colors.gold += .01;
				} else {
				    colors.gold = 1;
				    if(colors.red < 1) {
					colors.red += .01;
				    } else {
					colors.red = 0;
					colors.gold = 0;
				    }
				}
            	
				if(colors.gold > 1) colors.gold = 1;
				if(colors.red > 1) colors.red = 1;
				
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