// canvas
let c = document.getElementById("slate");

// context object
let ctx = c.getContext("2d");

// init global var
let mode = "rect";

let toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circle";
    }
    else {
        mode = "rect";
    }
}

let drawRect = function(e) {
    ctx.fillStyle = "red";
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillRect(mouseX, mouseY, 100, 200);
    ctx.fill()
}

let drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(e.offsetX, e.offsetY, 50, 0, 2 * Math.PI);
    ctx.fillStyle = "red";
    ctx.stroke();
    ctx.fill(); 
}

let draw = (e) => {
    if (mode == "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

let wipeCanvas = function() {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
let bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", function() {
    toggleMode();
    bToggler.innerHTML = mode;
    }
);
let clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);


