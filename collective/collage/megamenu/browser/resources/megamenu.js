/* Copied and adapted from http://www.sohtanaka.com/web-design/mega-drop-downs-w-css-jquery/ */

$(document).ready(function() {

	//Calculate width of all ul's
	(function($) { 
		jQuery.fn.calcSubWidth = function() {
			// Should receive a .collage-row element
			var rowWidth = 0;
			//Calculate row
			$(this).find("ul").each(function() {					
				rowWidth += $(this).width(); 
			});	
			return rowWidth;
		};
	})(jQuery); 


	(function($) {
		jQuery.fn.resetWidth = function() {
			// Should receive a .sub element
			// Show the element (opacity = 0) to set widths properly
			this.css('opacity', 0).show();
			var rows = this.find('.collage-row');
			var biggestRow = 0;	
			//Calculate each row
			rows.each(function() {							   
				var rowWidth = $(this).calcSubWidth();
				//Find biggest row
				if(rowWidth > biggestRow) {
					biggestRow = rowWidth;
				}
			});
			var maxColCount = 0;
			rows.each(function() {
				var columns = $(this).find('ul');
				var count = columns.length;
				columns.css('width', biggestRow/count);
				if(maxColCount<count) {
				    maxColCount = count;
				}
			});
			
			biggestRow += 30; //Set width adding 15 + 15 px (left and right padding)
//			biggestRow += (10*maxColCount-1)  // adding 10px pear every non-first column padding
			this.css({'width' :biggestRow});
			this.find(".collage-row:last").css({'margin':'0'});
			this.hide();
        };
    })(jQuery);
	
 
	function megaHoverOver(){
		var me = $(this);
		me.addClass('active');
		var sub = me.find('.sub');
		sub.stop().fadeTo(50, 1).show();
			
		var wWidth = $(window).width();
		sub.css('left', 0);
		var sWidth = sub.width();
		var difWidth = wWidth-(sub.offset().left+sWidth+19+20); //19px = scrollbar + 20px=padding
		if(difWidth<0) {
				sub.css('left', difWidth);
		} else {
				sub.css('left', 0);
		}
	}
	
	function megaHoverOut(){ 
		var me = $(this);
		me.removeClass('active');
		me.find(".sub").stop().fadeTo(50, 0, function() {
		  $(this).hide(); 
	  });
	}
 
 
	var config = {	
		 sensitivity: 2, // number = sensitivity threshold (must be 1 or higher)	
		 interval: 100, // number = milliseconds for onMouseOver polling interval	
		 over: megaHoverOver, // function = onMouseOver callback (REQUIRED)	
		 timeout: 100, // number = milliseconds delay before onMouseOut	
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

	// Preload sub-menues, if there are deferred dropdowns
	var deferred = megamenu.find('a[rel=deferred]');
	if(deferred.length>0) {
		megamenu.find('a[rel=deferred]').each(function() {
				$(this).parent().load(this.href, function(response, status, request) {
				// Reset width
				$(this).resetWidth();
			});
		});
 	} else {
 		// If there aren't deferred dropdowns, just reset their widths
 		megamenu.find('.sub').each(function() {
 		    $(this).resetWidth();
 		});
	}
 
});
