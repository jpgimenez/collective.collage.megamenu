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
            rows.each(function() {
                var columns = $(this).find('ul');
                columns.css('width', biggestRow/columns.length);
            });
			//Set width adding 15 + 15 px (left and right padding)
            biggestRow += 30;
			sub.css({'width' :biggestRow});
			$(this).find(".collage-row:last").css({'margin':'0'});
			
		} else { //If row does not exist...
			
			//$(this).calcSubWidth();
			//Set Width
			//sub.css({'width' : rowWidth});
			
		}
        var wWidth = $(window).width();
        sub.css('left', 0);
        var difWidth = wWidth-(sub.offset().left+biggestRow+19+20); //19px = scrollbar + 20px=padding
        if(difWidth<0) {
                sub.css('left', difWidth);
        } else {
                sub.css('left', 0);
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
 
    var megamenu = $('ul#portal-megamenu');
	megamenu.find('li .sub').css({'opacity':'0'});
	// Bind over/out and click events of li.top-level
	megamenu.find('li.top-level').hoverIntent(config).click(megaHoverOver).
	    // and Bind click event of their links
	    find('a').click(function(event) {
	        if($(this).closest('li').find('.sub').length>0) {
	            event.preventDefault();
	        }
	    });
 
    megamenu.find('a[rel=deferred]').each(function() {
        $(this).parent().load(this.href);
    });
 
 
});
