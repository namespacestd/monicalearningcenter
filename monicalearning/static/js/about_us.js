var currentTab = 0;

$(window).bind("load", function() {
	$('#about_us').click(function(event) {
    	if(currentTab!=0){
	    	$('.subtabs').fadeOut(2000);
	    	$('#init_tab').fadeIn(2000);
	    }
    	currentTab = 0;
	});

    $('#testimony').click(function(event) {
    	if(currentTab!=1){
	    	$('.subtabs').fadeOut(2000);
	    	$('#testimony_info').fadeIn(2000);
	    }
    	currentTab = 1;
	});

	$('#history').click(function(event) {
    	if(currentTab!=2){
	    	$('.subtabs').fadeOut(2000);
	    	$('#history_info').fadeIn(2000);
	    }
    	currentTab = 2;
	});
});