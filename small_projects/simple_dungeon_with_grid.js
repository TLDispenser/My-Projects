//same issue as bloodfall dont remeber import for this.. :(((((
var GRID_WID_HIGH = 20;
var arrayCount = 0;
//-----------------------------------Makes the board
//the entire first map
var board = new Grid(11, 10);
// w = wall, e = empty, c = player, g = win, d = danger/ enime
board.initFromArray([
    ["w","w","w","w","w","w","w","w","w","e"],
    ["w","g","e","e","e","e","e","e","w","w"],
    ["w","w","e","w","e","w","w","e","e","w"],
    ["w","e","e","e","e","w","w","w","e","w"],
    ["w","e","w","w","e","w","e","e","e","w"],
    ["w","e","w","w","e","e","e","w","e","w"],
    ["w","e","w","w","e","w","e","w","e","w"],
    ["w","e","w","e","e","e","e","e","e","w"],
    ["w","e","e","e","e","w","w","w","w","w"],
    ["w","w","w","c","w","w","w","w","w","w"],
    ["w","w","w","w","w","w","w","w","w","w"]
]);

//makes the grid
var numCou = 11;
function grid(x, y){
    for(var count = 0; count < numCou; count++){
        var line = new Line(0, y, getWidth() /2, y);
        line.setLineWidth(1);
        add(line);
        y += GRID_WID_HIGH;
    }
    for(var countT = 0; countT < numCou; countT++){
        var line = new Line(x, 0, x, getHeight() /2.39);
        line.setLineWidth(1);
        add(line);
        x += GRID_WID_HIGH;
    }
    
    setBoard();
}

//detects fromm the "ADD(below)" and adds what it is on the board
function setBoard(){
    for (var j = 0; j < 10; j++){
          for(var i = 0; i < 10; i++){
        var position =  board.get(j, i);
        if(position == "w"){
            boxSet(i, j);
        }else if(position == "c"){
            playerSet(i, j);
        }else if(position == "g"){
            winer(i, j);
        }else if(position == "d"){
            dangerBlockSet(i, j);
        }
        }
    }
}

//adds "walls"
function boxSet(x, y){
    var rect = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
    rect.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
    add(rect);
}

//Player box
var ply = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
function playerSet(x, y){
    ply.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
    ply.setColor("pink");
    add(ply);
}

//danger
function dangerBlockSet(x, y){
    var danger = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
    danger.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
    danger.setColor("green");
    add(danger);
}
//Win box
var win = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
function winer(x, y){
    win.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
    win.setColor("yellow");
    add(win);
}

//-------------------------moverment for the player && detition of block
var keys = keyDownMethod(keyDown);
function keyDown(kea) {
    var x = ply.getX() / GRID_WID_HIGH;
    var y = ply.getY() / GRID_WID_HIGH;
    if(kea.key == "w"){
        if(board.get(y -1, x) == "e"){
            ply.move(0, - GRID_WID_HIGH );
        }else if(board.get(y -1, x) == "g"){
            ply.move(0, - GRID_WID_HIGH);
            actionwin();
        }else if(board.get(y -1, x) == 0){
        }
    }else if (kea.key == "a") {
        if(board.get(y, x - 1) == "e"){
            ply.move(- GRID_WID_HIGH, 0);
        }else if(board.get(y, x - 1) == "g"){
            ply.move(- GRID_WID_HIGH, 0);
            actionwin();
        }else if(board.get(y, x - 1) == 0){
        }
    }else if (kea.key == "s") {
        if(board.get(y + 1, x) == "e"){
                ply.move(0, + GRID_WID_HIGH);
            }else if(board.get(y + 1, x) == "g"){
            ply.move(0, + GRID_WID_HIGH);
            actionwin();
        }else if(board.get(y + 1, x) == 0){
        }
    }else if (kea.key == "d") {
        if(board.get(y, x + 1) == "e"){
                ply.move(+ GRID_WID_HIGH, 0);
            }else if(board.get(y, x + 1) == "g"){
            ply.move(+ GRID_WID_HIGH, 0);
            actionwin();
        }else if(board.get(y, x + 1) == 0){
    }
}
}

//-----------------------------------Player's stats and pritntng them
var player = {
    name: "player",
    hp: "12",
    attack: "100",
    defence: 2
}

//-----------------------------------Danger blocks 
function dangerCutscene(){
    
}

//-----------------------------------Begining and ending cutseens
//so it doesent remove the screen afer the start
var firstTap = 0;
//start screan
function start(){
    var title = new Text("Simple dungeon", "20pt Arial");
    title.setPosition(getWidth() / 1/4.25 , getHeight() / 1/3);
    var startCon = new Text("Tap to start!", "15pt Arial"); 
    startCon.setPosition(getWidth() / 1/3 , getHeight() / 1/3 + 50);
    add(title);
    add(startCon);
    var mouse = mouseClickMethod(tap);
    function tap(mouse){
            if(firstTap == 0){
            firstTap++;
            removeAll();
            arrayCount = 0;
            grid(0, 0);
            }
    }
    var hp = player["12"];
    println(hp);
}
//win screen
function actionwin(){
        removeAll();
        var end = new Text("YOU WIN!!!", "20pt Arial");
        end.setPosition(getWidth() / 1/3.5 , getHeight() / 1/3);
        var goodJ = new Text("Good job!", "15pt Arial"); 
        goodJ.setPosition(getWidth() / 1/3 , getHeight() / 1/3 + 50);
        add(end);
        add(goodJ);
    }
