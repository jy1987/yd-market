const body = document.querySelector("body");
const backImg = body.querySelector(".js-clock");
const inputImg = backImg.querySelector("img");

const IMG_NUMBER = 11;
let initNum = 1;
let factor = Date.now();

function genRandom() {
  const number = Math.floor(Math.random(factor) * IMG_NUMBER) + 1;
  return number;
}

function paintImage() {
  genRandom();

  const k = genRandom();
  /*const image = new Image();
  image.src = `images/${k}.jpg`;
  image.classList.add("bgImage");*/
  inputImg.src = `images/${k}.jpg`;
  inputImg.classList.add("bgImage");
  /*inputImg.innerHTML = ` <img src="images/${k}.jpg" class="bgImage" />`; 얘도 사용 가능하나 차이는 텀이 생긴다는거?*/
}

/*function makeAllImg() {
  for (var i = 1; i < IMG_NUMBER; i += 1) {
    paintImage(i);
  }
}*/
function init() {
  setInterval(paintImage, 5000);
  paintImage();
}

init();
