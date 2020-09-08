const slidePage1 = document.querySelector(".formpage1");
const slidePage2 = document.querySelector('.formpage2'); 
const slidePage3 = document.querySelector('.formpage3');
const slidePage4 = document.querySelector(".formpage4");
const slidePage5 = document.querySelector('.formpage5'); 
const slidePage6 = document.querySelector('.formpage6');
const slidePage7 = document.querySelector('.formpage7');
const slidePage8 = document.querySelector('.formpage8');

const nextBtn1 = document.querySelector(".next-1");
const prevBtn1 = document.querySelector(".prev-1");

const nextBtn2 = document.querySelector(".next-2");
const prevBtn2 = document.querySelector(".prev-2");

const nextBtn3 = document.querySelector(".next-3");
const prevBtn3 = document.querySelector(".prev-3");

const nextBtn4 = document.querySelector(".next-4");
const prevBtn4 = document.querySelector(".prev-4");

const nextBtn5 = document.querySelector(".next-5");
const prevBtn5 = document.querySelector(".prev-5");

const nextBtn6 = document.querySelector(".next-6");
const prevBtn6 = document.querySelector(".prev-6");

const nextBtn7 = document.querySelector(".next-7");
const prevBtn7 = document.querySelector(".prev-7");

const submitBtn = document.querySelector(".submit");
const progressText = document.querySelectorAll('.step p');
const progressCheck = document.querySelectorAll('.step .check');
const bullet = document.querySelectorAll('.step .bullet');
let current = 1

document.addEventListener('DOMContentLoaded', function(){
  slidePage2.style.display ="None";
  slidePage3.style.display = "None";
  slidePage4.style.display ="None";
  slidePage5.style.display = "None";
  slidePage6.style.display ="None";
  slidePage7.style.display = "None";
  slidePage8.style.display = "None";
})

nextBtn1.addEventListener("click", function(){
  slidePage1.style.marginLeft="-25%";
  slidePage1.style.display = "None";
  slidePage2.style.display = "inline";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current-1].classList.add("active");
  current += 1;

});

nextBtn2.addEventListener("click", function(){
  slidePage1.style.marginLeft="-50%";
  slidePage3.style.display = "inline";
  slidePage2.style.display = "None";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current-1].classList.add("active");
  current += 1
})


nextBtn3.addEventListener("click", function(){
  slidePage1.style.marginLeft="-75%";
  slidePage4.style.display = "inline";
  slidePage3.style.display = "None";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current-1].classList.add("active");
  current += 1;

})

nextBtn4.addEventListener("click", function(){
  slidePage1.style.marginLeft="-100%";
  slidePage5.style.display = "inline";
  slidePage4.style.display = "None";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current-1].classList.add("active");
  current += 1;

})

nextBtn5.addEventListener("click", function(){
  slidePage1.style.marginLeft="-125%";
  slidePage6.style.display = "inline";
  slidePage5.style.display = "None";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current-1].classList.add("active");
  current += 1;

})

nextBtn6.addEventListener("click", function(){
  slidePage1.style.marginLeft="-150%";
  slidePage7.style.display = "inline";
  slidePage6.style.display = "None";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current-1].classList.add("active");
  current += 1;

})

nextBtn7.addEventListener("click", function(){
  slidePage1.style.marginLeft="-150%";
  slidePage8.style.display = "inline";
  slidePage7.style.display = "None";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current-1].classList.add("active");
  current += 1;

})

prevBtn1.addEventListener("click", function(){
  slidePage1.style.marginLeft="0%";
  slidePage1.style.display = "inline";
  slidePage2.style.display = "None";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current-2].classList.remove("active");
  current -=1
})

prevBtn2.addEventListener("click", function(){
  slidePage1.style.marginLeft="-25%";
  slidePage2.style.display = "inline";
  slidePage3.style.display = "None";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current-2].classList.remove("active");
  current -=1 
})

prevBtn3.addEventListener("click", function(){
  slidePage1.style.marginLeft="-50%";
  slidePage3.style.display = "inline";
  slidePage4.style.display = "None";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current-2].classList.remove("active");
  current -=1 
})

prevBtn4.addEventListener("click", function(){
  slidePage1.style.marginLeft="-75%";
  slidePage4.style.display = "inline";
  slidePage5.style.display = "None";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current-2].classList.remove("active");
  current -=1 
})

prevBtn5.addEventListener("click", function(){
  slidePage1.style.marginLeft="-100%";
  slidePage5.style.display = "inline";
  slidePage6.style.display = "None";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current-2].classList.remove("active");
  current -=1 
})

prevBtn6.addEventListener("click", function(){
  slidePage1.style.marginLeft="-125%";
  slidePage6.style.display = "inline"
  slidePage7.style.display = "None"
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current-2].classList.remove("active");
  current -=1 
})

prevBtn7.addEventListener("click", function(){
  slidePage1.style.marginLeft="-125%";
  slidePage7.style.display = "inline"
  slidePage8.style.display = "None"
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
