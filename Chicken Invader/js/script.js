var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext("2d");
document.onkeydown = checkKey;
//Game Dimensions with craft length and chicken length
var canvasWidth = 600;
var canvasHeight = 600;
var chickenLength = canvasWidth / 12;
var craftLength = canvasWidth / 6; 
//Intial game setting time, y count no of times grid moved at y-axis
//Inital level is set to 1, moveBullet tracks bullet  and score  
var time = 0 ;
var y = 0;
var level = 1;
var grid = [];
var moveBullet;
var LevelTimer;
var timeLeft;
var score = 0;
var GameStatus = "inactive";

var introtheme = new Audio('./audio/introtheme.ogg');                  //Audio
var chickenhit = new Audio('./audio/chickenhit.oga');
var gameover = new Audio('./audio/gameover.oga');
var maintrack = new Audio('./audio/maintrack.oga');
var bulletfire = new Audio('./audio/bullet.ogg');

var intro = function(){                                             //Onload function to create intro screen
    ctx.font = "50px Aerial";
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    ctx.fillText("Chicken Invaders", canvas.width/2, canvas.height/2-200);
    ctx.font = "30px Aerial";
    ctx.fillText("Press Enter to Start!", canvas.width/2, canvas.height/2-100);
    ctx.font = "20px Aerial";
    ctx.fillText("Game Controls: Use Arrow keys to control movement and Space to fire", 
    canvas.width/2, canvas.height/2 + 200);
    introtheme.play();
};

var activeGame = function(){ 
    craft.xPos = canvasWidth / 2 - craftLength/2;                           //setting initial spacecraft position
    craft.yPos = canvasHeight - canvasHeight / 6 - craftLength / 2;
    ctx.clearRect(0, 0, 600, 600);                                          //clearing canvas for game
    makeGrid(); 
    makeCraft();        
    scoreboard();
    time = (level + 2) * 4 + 2;
    clearInterval(LevelTimer);
    LevelTimer = setInterval(function(){                                    //Different level-timer for different levels
        if( y > level + 1){
            overGame();
            clearInterval(LevelTimer);
            }
        y++;
        moveGrid();                                                         //moving grid downward
        },4000);
    timeLeft = setInterval(function(){                                      //time left counter
        ctx.clearRect(canvas.width-300, canvas.height-40, 150, 40);
        ctx.font = "25px Aerial";
        ctx.fillStyle = "white";
        ctx.fillText("Timeleft: " + time,canvas.width-240, canvas.height-5);
        time -=1;
    },1000);
    introtheme.pause();
    maintrack.play();
};

var makeGrid = function(){                                      // function to create each chicken position
    width = canvasWidth / 12;
    for (var i = 0; i < level; i++) {
        grid[i] = [];
        for (var j = 0; j < 10; j++) {
            grid[i][j] = {
                xPos: j * width + width,
                yPos: i * width,
                status: "alive"
            }
            drawChicken(i,j);  
        }
    }
}

var updateGrid = function( ){                                    //updating grid on bullet hit
    var k = 0; 
    for (var i = level - 1; i >= 0; i--) {
        for (var j = 9; j >= 0; j--) {
            if(grid[i][j].status == "alive"){
                k++;
            }
        }
    }
    if(k == 0){
        wonGame();

    }

}

var deleteGrid = function( ){                                   //deleting full grid
    for (var i = 0; i < level; i++) {
        for (var j = 0; j < 10; j++) {
            deleteChicken(i,j);  
        }
    }
}

var moveGrid = function( ){                                     //moving grid after specific interval
    for (var i = 0; i < level; i++) {
        for (var j = 0; j < 10; j++) {
            if(grid[i][j].status == "alive"){
             deleteChicken(i,j);
            }  
        }
    }
    for (var i = 0; i < level; i++) {
        for (var j = 0; j < 10; j++) {
            grid[i][j].yPos  += 50;  
        }
    }
    for (var i = level - 1; i >= 0; i--) {
        for (var j = 9; j >= 0; j--) {
            if(grid[i][j].status == "alive"){
                drawChicken(i, j);
            }
        }
    }
    craftCrash();

}

var chicken = new Image();
chicken.src = './img/chicken.png';
var drawChicken = function(i, j){
    width = canvasWidth / 12;
    ctx.drawImage(chicken,grid[i][j].xPos, grid[i][j].yPos, width, width);
}

var deleteChicken = function(i, j){
    width = canvasWidth / 12;
    ctx.clearRect(grid[i][j].xPos, grid[i][j].yPos, width, width);
}

var craft = {
    xPos: canvasWidth / 2 - craftLength/2,
    yPos: canvasHeight - canvasHeight / 6 - craftLength / 2,
    dim: craftLength
}

var sc = new Image();
    sc.src = './img/sc.png';
var makeCraft = function(){
    ctx.drawImage(sc, craft.xPos, craft.yPos, craftLength, craftLength);
}

var deleteCraft = function(){
    ctx.clearRect(craft.xPos - 2, craft.yPos, craft.dim + 5, craft.dim);
};

var bullet = {
    xPos: 0,
    yPos: 0,
    dim: craftLength / 10,
    status: "active"
}

var makeBullet = function(){
    var b = new Image();
    b.src = './img/bullet.png';
    ctx.drawImage( b , bullet.xPos, bullet.yPos, bullet.dim, bullet.dim);
    bulletfire.play();
}

var deleteBullet = function(){
    ctx.clearRect(bullet.xPos, bullet.yPos, bullet.dim , bullet.dim);
}

var inactiveBullet = function(){                                        //If bullet hit top it will disapper
    if( bullet.yPos < 10){
        ctx.clearRect(bullet.xPos, bullet.yPos, bullet.dim , bullet.dim);
        clearInterval(moveBullet);
        bullet.status = "active";
    }
}

var destroyChicken = function(){                                    //Function for destroying chickensfrom grid
    var k = 0;
    for(i = level - 1; i >= 0; i-- ){
        for(j = 9;j >= 0; j--){
            var c = grid[i][j];
            if(c.status == "alive"){
                if((c.xPos < bullet.xPos + 10 && bullet.xPos < c.xPos + chickenLength) 
                    && ( bullet.yPos < c.yPos + chickenLength - 10)&& bullet.yPos > c.yPos - 10){
                    grid[i][j].status = "dead";
                    deleteBullet();
                    deleteChicken(i,j);
                    clearInterval(moveBullet);
                    bullet.status = "active";
                    k++;
                    score += 10;
                    scoreboard();
                    chickenhit.play();
                    break;
                }
            }
        }
    }

    updateGrid();
};


var craftCrash = function(){                                //Game over if spacecraft crashes into chicken 
    for (var i = level - 1; i >= 0; i--) {
        for (var j = 9; j >= 0; j--) {
            if(grid[i][j].status == "alive"){
                if( craft.yPos < grid[i][j].yPos + chickenLength)
                {
                    if (craft.xPos >= grid[i][j].xPos) {
                        if (craft.xPos - grid[i][j].yPos < chickenLength) {
                            overGame();
                            break;
                        }
                    }
                    else{
                        if(grid[i][j].xPos - craft.xPos < craft.dim){
                            overGame();
                            break;
                        }
                    }
                    
                }
            }
        }
    }
}

var scoreboard = function(){
    ctx.clearRect(canvas.width-120, canvas.height-40, 120, 40);
    ctx.font = "25px Aerial";
    ctx.fillStyle = "white";
    ctx.fillText("Score:"+ score, canvas.width-80, canvas.height-5);
};

/* This works when user wins game */

var wonGame = function(){
    clearInterval(LevelTimer);
    ctx.clearRect(0, 0, 600, 600);
    clearInterval(timeLeft);
    ctx.font = "45px Aerial";
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    ctx.fillText("You Won and your score: " + score, canvas.width/2, canvas.height/2-200);
    ctx.font = "30px Aerial";
    ctx.fillText("Press Enter to play Level: " + (level + 1) , canvas.width/2, canvas.height/2-100);
    ctx.font = "20px Aerial";
    ctx.fillText("Game Controls: Use Arrow keys to control movement and Space to fire", 
    canvas.width/2, canvas.height/2+200);
    y = 0;
    GameStatus = "inactive";
    maintrack.pause();
    introtheme.play();
    if( level > 6){
        finshedGame();
    }
    else{
        level = level + 1;
    }
}

var finshedGame = function(){
    deleteGrid();
    clearInterval(LevelTimer);
    ctx.clearRect(0, 0, 600, 600);
    clearInterval(timeLeft);
    GameStatus = "inactive"; 
    ctx.font = "40px Aerial";
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    ctx.fillText("Game finshed! score: " + score, canvas.width/2, canvas.height/2-200);
    ctx.font = "30px Aerial";
    ctx.fillText("Press Enter to play Again!", canvas.width/2, canvas.height/2-100);
    y = 0;
    level = 1;
    score = 0;
    maintrack.pause();
    introtheme.play();
};

var overGame = function(){
    deleteGrid();
    clearInterval(LevelTimer);
    ctx.clearRect(0, 0, 600, 600);
    clearInterval(timeLeft);
    GameStatus = "inactive"; 
    ctx.font = "40px Aerial";
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    ctx.fillText("Game Over!", canvas.width/2, canvas.height/2-200);
    ctx.font = "30px Aerial";
    ctx.fillText("Press Enter to play Again!", canvas.width/2, canvas.height/2-100);
    ctx.font = "20px Aerial";
    ctx.fillText("Game Controls: Use Arrow keys to control movement and Space to fire", 
    canvas.width/2, canvas.height/2+200);
    y = 0;
    score = score - level * 50;
    maintrack.pause();
    gameover.play();
};


function checkKey(e) {                      //Event handling of keypress
    e = e || window.event;
    if(GameStatus == "active")
    {
    if (e.keyCode == '32' && bullet.status == "active") {
        // up arrow

        bullet.xPos = craft.xPos + craft.dim / 2 - bullet.dim / 2;
        bullet.yPos = craft.yPos - bullet.dim - 2;
        bullet.status = "busy";
        makeBullet(bullet);
        moveBullet = setInterval(function(){
            deleteBullet();
            bullet.yPos = bullet.yPos - 20;
            makeBullet();
            inactiveBullet();
            destroyChicken();
        }, 25);
    }
    else if (e.keyCode == '38'){
        if (craft.yPos > 10){
            deleteCraft();
            craft.yPos = craft.yPos - 10; 
            makeCraft();
            craftCrash();
        }
    }
    else if (e.keyCode == '40') {
        // down arrow
        if (craft.yPos < canvasHeight - 40 - craft.dim ){
            deleteCraft();
            craft.yPos = craft.yPos + 10; 
            makeCraft();
            craftCrash();
        }
    }
    else if (e.keyCode == '37') {
       // left arrow
        if (craft.xPos > 10){
            deleteCraft();
            craft.xPos = craft.xPos - 10; 
            makeCraft();
            craftCrash();
        }
    
    }
    else if (e.keyCode == '39') {
       // right arrow
        if (craft.xPos < canvasWidth - 10 - craft.dim ){
            deleteCraft();
            craft.xPos = craft.xPos + 10; 
            makeCraft();
            craftCrash();
        }
     }
  }
    else if (e.keyCode == 13) {
        activeGame();
        GameStatus = "active";
    }
}

