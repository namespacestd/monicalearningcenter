var currentSlide = 1;
var slideNumber = 0;
function startSlideshow(numSlides){
	var begin = "<div class = \"slide\" id = \"slide";

	try{
		var allSlides = "";
		for (var i=1; i<=numSlides; i++){
			var slide = begin + i + "\"><img src = \"/static/img/0" + i +".jpg\" /> </div>";
			allSlides += slide;
		}
		document.getElementById('slideshow_background').innerHTML = allSlides;
		hideAll(numSlides);
		slideNumber = numSlides;
		var myVar = setInterval(function(){slideShow()}, 6000);
	}
	catch(err){
	}
}

function hideAll(numSlides){
	for(var i=2; i<=numSlides;i++){
		$("#slide"+i).css("display", "none");
	}
}

function slideShow(){
	$('#slide'+currentSlide).fadeOut(2000);
	currentSlide = currentSlide + 1;
	if(currentSlide > slideNumber)
		currentSlide = 1;
	$('#slide'+currentSlide).delay(2000).fadeIn(2000);
}