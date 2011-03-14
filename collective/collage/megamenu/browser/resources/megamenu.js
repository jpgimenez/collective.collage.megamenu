$(document).ready(function() {
	
 
	function megaHoverOver(){
		var me = $(this);
		var sub = me.find('.sub');
		sub.stop().fadeTo(100, 1);
			
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
		
		if ( me.find(".collage-row").length > 0 ) { //If row exists...
			var biggestRow = 0;	
			//Calculate each row
			me.find(".collage-row").each(function() {							   
				$(this).calcSubWidth();
				//Find biggest row
				if(rowWidth > biggestRow) {
					biggestRow = rowWidth;
				}
			});
			//Set width
			sub.css({'width' :biggestRow});
			me.find(".collage-row:last").css({'margin':'0'});
			
		} else { //If row does not exist...
			
			me.calcSubWidth();
			//Set Width
			sub.css({'width' : rowWidth});
			
		}
		sub.show();
	}
	
	function megaHoverOut(){ 
		var me = $(this);
		me.find(".sub").stop().fadeTo(100, 0, function() {
			$(this).hide(); 
	    });
	}
  
    $("ul#portal-megamenu li .sub").css({'opacity':'0'});
	// Create one delayedTask object for hover-in (display the menu)
	var taskOver = new $.delayedTask();
	
	$('ul#portal-megamenu li.top-level').hover(function(event) {
	        $(this).addClass('active');
			taskOver.delay(400, megaHoverOver, this, [event]);
	}, function(event) {
	        $(this).removeClass('active');
			// Create one delayedTask object for hover-out in every menu-item
			var taskOut = new $.delayedTask();
			taskOut.delay(400, megaHoverOut, this, [event]);
	}).find('a').click(function(event) {
	    if($(this).closest('li').find('.sub').length>0) {
	        event.preventDefault();
	        // Fire hover
			taskOver.delay(0, megaHoverOver, this, [event]);
	    }
	});
  
});
