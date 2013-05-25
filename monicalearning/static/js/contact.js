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
        $("#map").slideToggle(); 
        $("#map").html('<iframe width="500" height="650" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=Monica+Learning+Center,3999+Mission+Street,+San+Francisco,+CA+94112&amp;aq=&amp;sll=37.732482,-122.421834&amp;sspn=0.003519,0.005845&amp;t=m&amp;g=3999+Mission+Street,+San+Francisco,+CA+94112&amp;ie=UTF8&amp;hq=Monica+Learning+Center&amp;hnear=3999+Mission+St,+San+Francisco,+California+94112&amp;cid=2860980745052319627&amp;ll=37.733458,-122.425032&amp;spn=0.023826,0.036478&amp;z=14&amp;output=embed"></iframe>').css('display','block');
		$("#map2").slideToggle();
		$("#map2").html('<iframe width="500" height="650" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=Monica+Learning+Center,+noriega&amp;aq=&amp;sll=37.733996,-122.42589&amp;sspn=0.003519,0.005845&amp;t=m&amp;ie=UTF8&amp;hq=Monica+Learning+Center,+noriega&amp;cid=13705557173211135984&amp;hnear=&amp;ll=37.754023,-122.478161&amp;spn=0.023819,0.036478&amp;z=14&amp;iwloc=A&amp;output=embed"></iframe>').css('display', 'block');
	});
});