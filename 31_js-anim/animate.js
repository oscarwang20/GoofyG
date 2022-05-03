/* 
  Aryaman Goenka
  Softdev pd0
  k31 -- canvas based JS animation
  2022-02-15 

  JS file for JS cavas work    
*/

var c = document.getElementById('playground');
var dotButton = document.getElementById('animation');
var stopButton = document.getElementById('stop');

var ctx = c.getContext("2d");
ctx.fillStyle = 'red';

var requestID = 0;

var clear = (e) => {
  ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;

var start = (e) => {
  //if statement in place to stop animation from speeding up
  if (requestID === 0){
    requestID = window.requestAnimationFrame(drawDot)
  }
  else{
    return;
  }
}

var drawDot = (e) => {
  if (requestID > 0){
    console.log("draw circ");

    clear()

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

    requestID = window.requestAnimationFrame(drawDot);
  }
}

var stopIt = (e) => {

    console.log("stopIt invoked ...");
    console.log(requestID);

    window.cancelAnimationFrame(requestID);
    requestID = 0;
}


dotButton.addEventListener('click', start);
stopButton.addEventListener('click', stopIt);