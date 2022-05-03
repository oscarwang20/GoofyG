/* 
  Aryaman Goenka
  Softdev pd0
  k32 -- canvas based JS animation
  2022-02-17 

  JS file for JS cavas work    
*/

var c = document.getElementById('playground');
var dotButton = document.getElementById('animation');
var stopButton = document.getElementById('stop');
var logoButton = document.getElementById('logo')

var ctx = c.getContext("2d");
ctx.fillStyle = 'red';

var clear = () => {
  ctx.clearRect(0, 0, c.width, c.height);
}

var requestID_Dot = 0;
var requestID_Logo = 0;


var startLogo = (e) => {
  //if statement in place to stop animation from speeding up
  requestID_Dot = 0;
  if (requestID_Logo === 0){
    requestID_Logo = window.requestAnimationFrame(drawLogo)
  }
  else{
    return;
  }
}

var startDot = (e) => {
    requestID_Logo = 0;
    //if statement in place to stop animation from speeding up
    if (requestID_Dot === 0){
        requestID_Dot = window.requestAnimationFrame(drawDot)
    }
    else{
      return;
    }
  }

var radius = 0;
var growing = true;

var drawDot = () => {
  if (requestID_Dot > 0){
    console.log("draw circ");

    clear();

    ctx.beginPath();
    ctx.arc(c.width / 2, c.width / 2, radius, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();

    if (radius >= 250){
      growing = false;
    }
    else if (radius <= 1){
      growing = true;
    }

    if(growing){
      radius++;
    } 
    else {
      radius--;
    }

    requestID_Dot = window.requestAnimationFrame(drawDot);
  }
}

//ctx.drawImage()

let dvdImage = new Image();
dvdImage.src = 'dvdimage.png';

var x = Math.floor(Math.random() * 300) + 100;
var y = Math.floor(Math.random() * 300) + 100;
var direction = 'br';

var drawLogo = (e) => {
    console.log('Logo')

    clear()

    ctx.beginPath();
    ctx.drawImage(dvdImage, x, y, 200, 100);
    ctx.stroke();
    ctx.fill();

    if(x === 500 - 200){

       direction = 'ul';

    }else if(y === 500 - 100){

        direction = "ur";

    }else if(y === 0 + 50){

        direction = 'bl';

    }else if (x === 0 + 50){

        direction = 'br';

    }
       
    if (direction === "ur"){y--; x++;}
    else if(direction === "ul"){y--; x--;}
    else if(direction === "bl"){y++; x--;}
    else if (direction === "br"){y++; x++;}
    

    requestID_Logo = window.requestAnimationFrame(drawLogo);

}

var stopIt = (e) => {

    console.log("stopIt invoked ...");


    window.cancelAnimationFrame(requestID_Dot);
    window.cancelAnimationFrame(requestID_Logo);
    requestID_Dot = 0;
    requestID_Logo = 0;
}

//start() vs start ??
dotButton.addEventListener('click', startDot); 
logoButton.addEventListener('click', startLogo);
stopButton.addEventListener('click', stopIt);