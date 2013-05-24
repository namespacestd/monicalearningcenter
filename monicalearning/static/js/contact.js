var currentTab = 0;

$(window).bind("load", function() {
	$('#init_tab').css("display", "inherit");

    $('#contact').click(function(event) {
    	if(currentTab!=0){
	    	$('.subtabs').fadeOut(2000);
	    	$('#init_tab').fadeIn(2000);
	    }
    	currentTab = 0;
	});

    $('#direct').click(function(event) {
    	if(currentTab!=1){
	    	$('.subtabs').fadeOut(2000);
	    	$('#directions').fadeIn(2000);
	    }
    	currentTab = 1;
	});
});