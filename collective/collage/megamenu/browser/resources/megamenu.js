/* Copied and adapted from http://www.sohtanaka.com/web-design/mega-drop-downs-w-css-jquery/ */

$(document).ready(function() {
	
 
	function megaHoverOver(){
    	var me = $(this);
    	me.addClass('active');
    	var sub = me.find('.sub');
		sub.stop().fadeTo(100, 1).show();
			
		//Calculate width of all ul's
		(function($) { 
			jQuery.fn.calcSubWidth = function() {
				rowWidth = 0;
				//Calculate row
				$(this).find("ul").each(function() {					
					rowWidth += $(this).width(); 
				});	
			};
		})(jQuery); 
		
		var rows = me.find('.collage-row');
		if (rows.length > 0 ) { //If row exists...
			var biggestRow = 0;	
			//Calculate each row
			rows.each(function() {							   
				$(this).calcSubWidth();
				//Find biggest row
				if(rowWidth > biggestRow) {
					biggestRow = rowWidth;
				}
			});
			//Set width
			sub.css({'width' :biggestRow});
			$(this).find(".collage-row:last").css({'margin':'0'});
			
		} else { //If row does not exist...
			
			$(this).calcSubWidth();
			//Set Width
			sub.css({'width' : rowWidth});
			
		}
	}
	
	function megaHoverOut(){ 
	    var me = $(this);
	    me.removeClass('active');
        me.find(".sub").stop().fadeTo(100, 0, function() {
		  $(this).hide(); 
	  });
	}
 
 
	var config = {    
		 sensitivity: 2, // number = sensitivity threshold (must be 1 or higher)    
		 interval: 100, // number = milliseconds for onMouseOver polling interval    
		 over: megaHoverOver, // function = onMouseOver callback (REQUIRED)    
		 timeout: 300, // number = milliseconds delay before onMouseOut    
		 out: megaHoverOut // function = onMouseOut callback (REQUIRED)    
	};
 
	$("ul#portal-megamenu li .sub").css({'opacity':'0'});
	// Bind over/out and click events of li.top-level
	$("ul#portal-megamenu li.top-level").hoverIntent(config).click(megaHoverOver).
	    // and Bind click event of their links
	    find('a').click(function(event) {
	        if($(this).closest('li').find('.sub').length>0) {
	            event.preventDefault();
	        }
	    });
 
 
 
});
