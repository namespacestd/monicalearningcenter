var currentTab = 0;

$(window).bind("load", function() {
	

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

    	event.preventDefault();
        $("#map1").slideToggle(); 
        $("#map1").html('<iframe width="500" height="500" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=monica+learning+center+3999+mission+st+san+francisco&amp;aq=&amp;sll=37.7577,-122.4376&amp;sspn=0.235332,0.528374&amp;ie=UTF8&amp;hq=monica+learning+center&amp;hnear=3999+Mission+St,+San+Francisco,+California+94112&amp;t=m&amp;cid=2860980745052319627&amp;ll=37.740449,-122.425203&amp;spn=0.033937,0.04283&amp;z=14&amp;iwloc=A&amp;output=embed"></iframe>').css('display','block');
		$("#map2").slideToggle();
		$("#map2").html('<iframe width="500" height="500" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=monica+learning+center+1333+noriega+street+san+francisco&amp;aq=&amp;sll=37.7577,-122.4376&amp;sspn=0.235332,0.528374&amp;ie=UTF8&amp;hq=monica+learning+center&amp;hnear=1333+Noriega+St,+San+Francisco,+California+94122&amp;t=m&amp;ll=37.755668,-122.477925&amp;spn=0.008483,0.010707&amp;z=16&amp;iwloc=A&amp;output=embed"></iframe>').css('display', 'block');
	});
});