var currentTab = 1;

$(window).bind("load", function() {
	$('#resources').click(function(event) {
    	if(currentTab!=1){
	    	$('.subtabs').fadeOut(2000);
	    	$('#practice_info').fadeIn(2000);
	    }
    	currentTab = 1;
	});

    $('#practice').click(function(event) {
    	if(currentTab!=1){
	    	$('.subtabs').fadeOut(2000);
	    	$('#practice_info').fadeIn(2000);
	    }
    	currentTab = 1;
	});
	$('#intern').click(function(event) {
    	if(currentTab!=2){
	    	$('.subtabs').fadeOut(2000);
	    	$('#intern_info').fadeIn(2000);
	    }
    	currentTab = 2;
	});
	$('#aid').click(function(event) {
    	if(currentTab!=3){
	    	$('.subtabs').fadeOut(2000);
	    	$('#aid_info').fadeIn(2000);
	    }
    	currentTab = 3;
	});
});