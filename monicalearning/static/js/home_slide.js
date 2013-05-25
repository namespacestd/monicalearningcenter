var currentSlide = 1;
var slideNumber = 0;

var currentNews = 1;

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
		setInterval(function(){slideShow()}, 6000);
		setInterval(function(){newsTicker()}, 7000);
	}
	catch(err){
	}
}

function hideAll(numSlides){
	for(var i=2; i<=numSlides;i++){
		$("#slide"+i).css("display", "none");
	}
}

function newsTicker(){
	$('.slogan'+currentNews).slideUp(2000);
	currentNews++;
	if(currentNews > 4)
		currentNews = 1;
	$('.slogan'+currentNews).slideToggle(2000);
}

function slideShow(){
	$('#slide'+currentSlide).fadeOut(2000);
	currentSlide = currentSlide + 1;
	if(currentSlide > slideNumber)
		currentSlide = 1;
	$('#slide'+currentSlide).fadeIn(2000);
}