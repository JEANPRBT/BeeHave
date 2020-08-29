const slidePage1 = document.querySelector(".formpage1");
const slidePage2 = document.querySelector('.formpage2'); 
const slidePage3 = document.querySelector('.formpage3');
const firstNextBtn = document.querySelector(".next-1");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-2");
const prevBtnThird = document.querySelector(".prev-2");
const submitBtn = document.querySelector(".submit");
const progressText = document.querySelectorAll('.step p');
const progressCheck = document.querySelectorAll('.step .check');
const bullet = document.querySelectorAll('.step .bullet');
let max = 4;
let current = 1

document.addEventListener('DOMContentLoaded', function(){
	slidePage2.style.display ="None"
	slidePage3.style.display = "None"

})

firstNextBtn.addEventListener("click", function(){
	slidePage1.style.marginLeft="-25%";
	slidePage1.style.display = "None";
	slidePage2.style.display = "inline";
	bullet[current - 1].classList.add("active");
	progressCheck[current - 1].classList.add("active");
	progressText[current-1].classList.add("active");
	current += 1;

});

prevBtnSec.addEventListener("click", function(){
	slidePage1.style.marginLeft="0%";
	slidePage1.style.display = "inline";
	slidePage2.style.display = "None";
	bullet[current - 2].classList.remove("active");
	progressCheck[current - 2].classList.remove("active");
	progressText[current-2].classList.remove("active");
	current -=1
})

nextBtnSec.addEventListener("click", function(){
	slidePage1.style.marginLeft="-50%";
	slidePage3.style.display = "inline";
	slidePage2.style.display = "None";
	bullet[current - 1].classList.add("active");
	progressCheck[current - 1].classList.add("active");
	progressText[current-1].classList.add("active");
	current += 1
})

prevBtnThird.addEventListener("click", function(){
	slidePage1.style.marginLeft="-25%";
	slidePage2.style.display = "inline"
	slidePage3.style.display = "None"
	bullet[current - 2].classList.remove("active");
	progressCheck[current - 2].classList.remove("active");
	progressText[current-2].classList.remove("active");
	current -=1	
})

submitBtn.addEventListener("click", function(){
	bullet[current - 1].classList.add("active");
	progressCheck[current - 1].classList.add("active");
	progressText[current-1].classList.add("active");
	current += 1
})