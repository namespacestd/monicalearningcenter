var currentTab = 0;

$(window).bind("load", function() {
	$('#program').click(function(event) {
    	if(currentTab!=0){
	    	$('.subtabs').fadeOut(2000);
	    	$('#init_tab').fadeIn(2000);
	    }
    	currentTab = 0;
	});

    $('#mathsci').click(function(event) {
    	if(currentTab!=1){
	    	$('.subtabs').fadeOut(2000);
	    	$('#mathsci_info').fadeIn(2000);
	    }
    	currentTab = 1;
	});

	$('#english').click(function(event){
		if(currentTab!=2){
			$('.subtabs').fadeOut(2000);
			$('#english_info').fadeIn(2000);
		}
		currentTab = 2;
	});
	
	$('#sat').click(function(event){
		if(currentTab!=3){
			$('.subtabs').fadeOut(2000);
			$('#sat_info').fadeIn(2000);
		}
		currentTab = 3;
	});
	
	$('#ssat').click(function(event){
		if(currentTab!=4){
			$('.subtabs').fadeOut(2000);
			$('#ssat_info').fadeIn(2000);
		}
		currentTab = 4;
	});
	
	$('#star').click(function(event){
		if(currentTab!=5){
			$('.subtabs').fadeOut(2000);
			$('#star_info').fadeIn(2000);
		}
		currentTab = 5;
	});

	$('#chinese').click(function(event){
		if(currentTab!=6){
			$('.subtabs').fadeOut(2000);
			$('#chinese_info').fadeIn(2000);
		}
		currentTab = 6;
	});
});