//there is a import I don't remember what tho...
//board with and hight of grid
var GRID_WIDTH = 10;
var GRID_HIGHT = 10;
//Grid with and hight
var GRID_WID_HIGH = GRID_WIDTH + GRID_HIGHT;
//Entire with and hight of the map
var ENTIRE_W_AND_H_OF_BOARD = GRID_WID_HIGH * GRID_WIDTH;
//the entire first map
var board = new Grid(GRID_HIGHT, GRID_WIDTH);
//CHANGE ALL BOARDS TO 10 DOWN AN THE COUNTERS 
//each incment will alow to change maps
var dificulty = 1;
var mapCount = 1;
//to make eazy for boos fights
var bossFight = false;
//players buttions
var upButon;
var downButon;
var leftButon;
var rightButon;
/*TEMPLATE
    board.initFromArray([
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""]
        ]);
*/
//-----------------------------------Makes the RANDMLEY GENERATED map
// w = wall, e = empty, c = player, g = win, d = danger/ enemy, n = next room, b = boss, l = loot
function randomGenMap(){
    removeAll();
    var luck = Randomizer.nextInt(1,12);
    var topRight = Randomizer.nextInt(1,2);
    var topLeft = Randomizer.nextInt(1,2);
    var bottemRight = Randomizer.nextInt(1,2);
    var bottemLeft = Randomizer.nextInt(1,2);
    if(luck == 12){
        board.initFromArray([
        ["w","w","w","w","n","w","w","w","w","w"],
        ["w","w","w","w","e","e","w","w","w","w"],
        ["w","w","w","e","e","e","e","w","w","w"],
        ["w","w","e","e","l","e","e","l","w","w"],
        ["w","e","l","e","e","e","e","e","e","w"],
        ["w","e","e","e","e","e","e","e","l","w"],
        ["w","l","e","l","e","e","e","e","e","w"],
        ["w","w","e","e","e","e","l","e","w","w"],
        ["w","w","w","e","c","e","e","w","w","w"],
        ["w","w","w","w","w","w","w","w","w","w"]
        ]);
    }else if(mapCount % 5 == 0){
        board.initFromArray([
        ["w","w","w","w","n","w","w","w","w","w"],
        ["w","w","w","w","e","e","w","w","w","w"],
        ["w","w","w","e","e","e","e","w","w","w"],
        ["w","w","e","e","e","e","e","e","w","w"],
        ["w","e","e","e","e","e","e","e","e","w"],
        ["w","d","e","e","e","e","e","e","d","w"],
        ["w","e","e","e","e","e","e","e","e","w"],
        ["w","w","e","e","e","e","e","e","w","w"],
        ["w","w","w","e","c","e","e","w","w","w"],
        ["w","w","w","w","w","w","w","w","w","w"]
        ]);
        if(mapCount % 10 == 0){
        board.initFromArray([
        ["w","w","w","w","n","w","w","w","w","w"],
        ["w","w","w","w","b","e","w","w","w","w"],
        ["w","w","w","e","e","e","e","w","w","w"],
        ["w","w","e","e","e","e","e","e","w","w"],
        ["w","e","e","e","e","e","e","e","e","w"],
        ["w","d","e","e","e","e","e","e","d","w"],
        ["w","e","e","e","e","e","e","e","e","w"],
        ["w","w","e","e","e","e","e","e","w","w"],
        ["w","w","w","e","c","e","e","w","w","w"],
        ["w","w","w","w","w","w","w","w","w","w"]
    ]);
        }
    }else{
        randGen();
    }
function randGen(){
    if(bottemRight == 1){
        board.initFromArray([
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","w","w","w","w","w"],
            ["","","","","","w","e","d","e","w"],
            ["","","","","","w","e","w","e","w"],
            ["","","","","","e","e","w","n","w"],
            ["","","","","","w","w","w","w","w"]
        ]);
    }else if(bottemRight == 2){
       board.initFromArray([
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","","","","",""],
            ["","","","","","w","w","w","w","w"],
            ["","","","","","e","e","e","d","w"],
            ["","","","","","e","w","w","e","w"],
            ["","","","","","e","d","d","n","w"],
            ["","","","","","w","w","w","w","w"]
        ]); 
    }
    if(bottemLeft == 1){
        board.initFromArray([
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["w","e","w","w","w"],
            ["w","d","e","w","w"],
            ["w","w","e","w","w"],
            ["w","w","e","e","e"],
            ["w","w","w","w","w"]
        ]);
    }else if(bottemLeft == 2){
       board.initFromArray([
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["w","e","w","w","w"],
            ["w","e","e","e","w"],
            ["w","e","d","e","w"],
            ["w","e","e","e","d"],
            ["w","w","w","w","w"]
        ]); 
    }
    if(topRight == 1){
        board.initFromArray([
            ["","","","","","w","w","w","w","w"],
            ["","","","","","e","w","e","c","w"],
            ["","","","","","e","w","e","w","w"],
            ["","","","","","e","d","e","w","w"],
            ["","","","","","e","e","e","w","w"]
        ]);
    }else if(topRight == 2){
       board.initFromArray([
            ["","","","","","w","w","w","w","w"],
            ["","","","","","e","e","d","c","w"],
            ["","","","","","w","e","w","e","w"],
            ["","","","","","w","e","w","e","w"],
            ["","","","","","w","e","e","e","w"]
        ]); 
    }
    if(topLeft == 1){
        board.initFromArray([
            ["w","w","w","w","w"],
            ["w","w","w","e","e"],
            ["w","e","e","e","w"],
            ["w","e","w","e","w"],
            ["w","e","e","d","w"]
        ]);
    }else if(topLeft == 2){
       board.initFromArray([
            ["w","w","w","w","w"],
            ["w","e","e","e","e"],
            ["w","e","d","w","w"],
            ["w","d","e","e","w"],
            ["w","e","e","d","w"]
        ]); 
    }
}
    setBoard();
}
//detects fromm the "ADD(below)" and adds what it is on the board
//Graficjs vars
var ply;
var next;
var win;
var bosse;
var loot;
function setBoard(){
    /*
    //makes a grid
    grid();
    function grid(){
        var numCou = 10;
        var x = 0;
        var y = 0;
        for(var count = 0; count < numCou; count++){
            var line = new Line(0, y, getWidth() , y);
            line.setLineWidth(1);
            add(line);
            y += GRID_WID_HIGH;
        }
        for(var countT = 0; countT < numCou; countT++){
            var line = new Line(x, 0, x, getHeight());
            line.setLineWidth(1);
            add(line);
            x += GRID_WID_HIGH;
        }
    }
    */
    playUI();
    for(var j = 0; j < GRID_HIGHT; j++){
          for(var i = 0; i < GRID_WIDTH; i++){
        var position =  board.get(j, i);
        if(position == "w"){
            boxSet(i, j);
        }else if(position == "c"){
            playerSet(i, j);
        }else if(position == "g"){
            winer(i, j);
        }else if(position == "d"){
            dangerBlockSet(i, j);
        }else if(position == "d"){
            dangerBlockSet(i, j);
        }else if(position == "n"){
            nextRoom(i, j);
        }else if(position == "b"){
            bossBlock(i, j);
        }else if(position == "l"){
            lootBox(i, j);
        }
        }
    }
    //adds "walls"
    function boxSet(x, y){
        var backRoundRandom = Randomizer.nextInt(1,2);
        if(backRoundRandom == 1){
            var rect = new WebImage("https://tse2.mm.bing.net/th/id/OIP.-vHfBFCyjr1DVg82qhX5aAHaFj?pid=ImgDet&rs=1");
        }else if(backRoundRandom == 2){
        var rect = new WebImage("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6176f303-518c-4b9f-a201-b6fe1b4239b2/d6wdlx3-688e0e84-ce76-4ffb-96bd-42939941a91d.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzYxNzZmMzAzLTUxOGMtNGI5Zi1hMjAxLWI2ZmUxYjQyMzliMlwvZDZ3ZGx4My02ODhlMGU4NC1jZTc2LTRmZmItOTZiZC00MjkzOTk0MWE5MWQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.gVwkqXdBCzI-tRBrm-ntgF6vFCZt2CnpyNsVT1oUdK0");
        }
        rect.setSize(GRID_WID_HIGH, GRID_WID_HIGH);
        //var rect = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
        rect.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
        add(rect);
    }
    //Player box
    function playerSet(x, y){
        //var ply = new WebImage("");
        //ply.setSize(GRID_WID_HIGH, GRID_WID_HIGH);
        ply = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
        ply.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
        ply.setColor("blue");
        add(ply);
    }
    //danger
    function dangerBlockSet(x, y){
        //var danger = new WebImage("");
        //danger.setSize(GRID_WID_HIGH, GRID_WID_HIGH);
        var danger = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
        danger.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
        danger.setColor("green");
        add(danger);
    }
    // next room
    function nextRoom(x, y){
        //var rect = new WebImage("");
        //rect.setSize(GRID_WID_HIGH, GRID_WID_HIGH);
        next = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
        next.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
        next.setColor("gray");
        add(next);
    }
    //Win box
    function winer(x, y){
        //var rect = new WebImage("");
        //rect.setSize(GRID_WID_HIGH, GRID_WID_HIGH);
        win = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
        win.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
        win.setColor("purple");
        add(win);
    }
    // boss
    function bossBlock(x, y){
        //var rect = new WebImage("");
        //.setSize(GRID_WID_HIGH, GRID_WID_HIGH);
        bosse = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
        bosse.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
        bosse.setColor("red");
        add(bosse);
    }
    //anytype of common loot
    function lootBox(x, y){
        //var rect = new WebImage("");
        //rect.setSize(GRID_WID_HIGH, GRID_WID_HIGH);
        loot = new Rectangle(GRID_WID_HIGH, GRID_WID_HIGH);
        loot.setPosition(x * GRID_WID_HIGH, y * GRID_WID_HIGH);
        loot.setColor("yellow");
        add(loot);
    }
}
//-------------------------moverment for the player && detition of block && leval up
//for movement durning stuff
var canMove = true;
keyDownMethod(keyDown);
function keyDown(kea){
    //println("(" + e.getX() + " , " + e.getY() + ")")
    //movemnetnt and detection
    //set up for it
    /*if(board.get(y, x) == "STRING"){
        ply.move(0, - GRID_WID_HIGH );
        OR
        board.set(y, x, "e");
        elem = getElementAt((y - + 1) * GRID_WID_HIGH, (y - + 1) * GRID_WID_HIGH);
        remove(elem);
        IF Eni
        eniEncounter();
    */
    if(canMove == true){
        var x = ply.getX() / GRID_WID_HIGH;
        var y = ply.getY() / GRID_WID_HIGH;
        var elem;
        if(kea.key == "w" || kea.key == "ArrowUp"){
            if(board.get(y -1, x) == "e"){
                ply.move(0, - GRID_WID_HIGH );
            }else if(board.get(y -1, x) == "g"){
                ply.move(0, - GRID_WID_HIGH);
                actionwin();
            }else if(board.get(y -1, x) == ""){
            }else if(board.get(y -1, x) == "b"){
                bossFight = true;
                board.set(y -1, x, "e");
                elem = getElementAt(x * GRID_WID_HIGH, (y - 1) * GRID_WID_HIGH);
                remove(elem); 
                eniEncounter();
            }else if(board.get(y -1, x) == "n" || board.get(y -1, x) == null){
                dificulty += 0.25;
                mapCount += 1;
                randomGenMap();
            }else if(board.get(y -1, x) == "d"){
                board.set(y -1, x, "e");
                elem = getElementAt(x * GRID_WID_HIGH, (y -1) * GRID_WID_HIGH);
                remove(elem); 
                eniEncounter();
            }else if(board.get(y -1, x) == "l"){
                board.set(y -1, x, "e");
                elem = getElementAt(x * GRID_WID_HIGH, (y -1) * GRID_WID_HIGH);
                remove(elem);
                randLoot();
            }
        }
        if(kea.key == "a" || kea.key == "ArrowLeft"){
            if(board.get(y, x - 1) == "e"){
                ply.move(- GRID_WID_HIGH, 0);
            }else if(board.get(y, x - 1) == "g"){
                ply.move(- GRID_WID_HIGH, 0);
                actionwin();
            }else if(board.get(y, x - 1) == ""){
            }else if(board.get(y, x - 1) == "b"){
                bossFight = true;
                board.set(y, x + 1.1, "e");
                elem = getElementAt((x + 1) * GRID_WID_HIGH, y * GRID_WID_HIGH);
                remove(elem); 
                    eniEncounter();
            }else if(board.get(y, x - 1) == "n" || board.get(y, x - 1) == null){
                dificulty += 0.25;
                mapCount += 1;
                randomGenMap();
            }else if(board.get(y, x - 1) == "d"){
                board.set(y, x - 1, "e");
                elem = getElementAt((x - 1) * GRID_WID_HIGH, y * GRID_WID_HIGH);
                remove(elem); 
                eniEncounter();
            }else if(board.get(y, x - 1) == "l"){
                board.set(y, x - 1, "e");
                elem = getElementAt((x - 1) * GRID_WID_HIGH, y * GRID_WID_HIGH);
                remove(elem);
                randLoot();
            }
        }
        if(kea.key == "s" || kea.key == "ArrowDown"){
            if(board.get(y + 1, x) == "e"){
                ply.move(0, + GRID_WID_HIGH);
            }else if(board.get(y + 1, x) == "g"){
                ply.move(0, + GRID_WID_HIGH);
                actionwin();
            }else if(board.get(y + 1, x) == ""){
            }else if(board.get(y + 1, x) == "b"){
                bossFight = true;
                board.set(y + 1, x, "e");
                elem = getElementAt(x * GRID_WID_HIGH, (y + 1) * GRID_WID_HIGH);
                remove(elem); 
                eniEncounter();
            }else if(board.get(y + 1, x) == "n" || board.get(y + 1, x) == null){
                dificulty += 0.25;
                mapCount += 1;
                randomGenMap();
            }else if(board.get(y + 1, x) == "d"){
                board.set(y + 1, x, "e");
                elem = getElementAt(x * GRID_WID_HIGH, (y + 1) * GRID_WID_HIGH);
                remove(elem); 
                eniEncounter();
            }else if(board.get(y + 1, x) == "l"){
                board.set(y + 1, x, "e");
                elem = getElementAt(x * GRID_WID_HIGH, (y + 1) * GRID_WID_HIGH + 10);
                remove(elem);
                randLoot();
            }
        }
        if(kea.key == "d" || kea.key == "ArrowRight"){
            if(board.get(y, x + 1) == "e"){
                ply.move(+ GRID_WID_HIGH, 0);
            }else if(board.get(y, x + 1) == "g"){
                ply.move(+ GRID_WID_HIGH, 0);
                actionwin();
            }else if(board.get(y, x + 1) == ""){
            }else if(board.get(y, x + 1) == "b"){
                bossFight = true;
                board.set(y, x + 1, "e");
                elem = getElementAt((x + 1.1) * GRID_WID_HIGH, y * GRID_WID_HIGH);
                remove(elem); 
                eniEncounter();
            }else if(board.get(y, x + 1) == "n" || board.get(y, x + 1) == null){
                dificulty += 0.25;
                mapCount += 1;
                randomGenMap();
            }else if(board.get(y, x + 1) == "d"){
                board.set(y, x + 1, "e");
                elem = getElementAt((x + 1.1) * GRID_WID_HIGH, y * GRID_WID_HIGH);
                remove(elem); 
                eniEncounter();
            }else if(board.get(y, x + 1) == "l"){
                board.set(y, x + 1, "e");
                elem = getElementAt((x + 1.1) * GRID_WID_HIGH, y * GRID_WID_HIGH);
                remove(elem); 
                randLoot();
            }
        }
        if(kea.key == "i"){
            itemChoose();
        }
    }
}

//-----------------------------------players's stats and spells and item
// Diffrent classes
var playerPerson = [/*name*/"",/*Max hp*/30,/*now hp*/30,/*attack*/4,/*defence*/3,/*xp LV*/0,/*gold*/0];

//classes for player
var fighter = false;
var mage = false;
var tank = false;
//spells IT GOES var spellName = [/*name*/"",/*what it does*/"",/*element*/"",/*numb of change*/#];
var spellName = [/*name*/"",/*what it does*/"",/*element*/"",/*numb of change*/0];
//Items
var items = new Grid(2, 5);
items.initFromArray([
    //set up [/*name*/"",/*what it does*/"",/*numb of have*/0,/*numb of change*/0],
    [/*name*/"Hp Potion",/*what it does*/"Heals you 25%",/*numb of have*/0,/*numb of change*/0.25],
    [/*name*/"Xp Potion",/*what it does*/"Gives you 5 xp",/*numb of have*/0,/*numb of change*/5]
]);
//-----------------------------------------------Player spell use

//----------------------------------------Random Loot randmiser
function randLoot(){
    let randomItomChose = Randomizer.nextInt(0,3);
    if(randomItomChose == 3){
        let randomExtraGold = Randomizer.nextInt(1, 12);
        playerPerson[6] += randomExtraGold;
        println("You gained " + randomExtraGold + " gold! ");
    }
    if(randomItomChose < 2){
        items.set(randomItomChose, 2, (items.get(randomItomChose, 2) + 1));
        println("You gained " + items.get(randomItomChose, 0));
    }
}
//-----------------------------------------------Player invtory slect
async function itemChoose(){
    var temptemp = false;
    print("test");
    if(canMove == true){
        canMove = false;
        println("your hp: " + playerPerson[2] + " your xp: " + playerPerson[5]);
        temptemp = true;
    }
    println("Items you have");
    for(var i = 0; i < items.numRows(); i++){
        if(items.get(i, 2) != 0){
            println(i + ": " + items.get(i, 0) + " Have: " + items.get(i, 2));
        }
    }
    while(true){
        let itemToUse = await readIntAsync("What do you want to use? (-1 to stop) ");
        if(itemToUse < items.numRows() && itemToUse >= 0){
            if(itemToUse == 0 && items.get(itemToUse, 2) != 0){
                playerPerson[2] = playerPerson[2] + (playerPerson[2] * items.get(0, 3))
                if(playerPerson[2] > playerPerson[1]){
                    playerPerson[2] = playerPerson[1];
                }
                items.set(itemToUse, 2, (items.get(itemToUse, 2) -1));
                break;
            }else if(itemToUse == 1 && items.get(itemToUse, 2) != 0){
                playerPerson[5] =  playerPerson[5] + items.get(itemToUse, 3);
                await levUp();
                items.set(itemToUse, 2, (items.get(itemToUse, 2) -1));
                break;
            }
        }else if(itemToUse == -1){
            break;
        }else{
            println("(Plese put the number befor the name) (-1 to stop)");
        }
    }
    if(temptemp == true){
        canMove = true;
        temptemp = false;
    }
}
//-----------------------------------Levle up function
var lVsNeededToLV = 15;
async function levUp(){
    if(playerPerson[5] >= lVsNeededToLV){
        println("You can leval up!!!");
        var magicUp = 1;
        var defenceUP = 1;
        var attackUp = 2;
        if(fighter == true){
            attackUp = 3;
        }else if(mage == true){
            magicUp = 2;
        }else if(tank == true){
            defenceUP = 2;
        }
        while(true){
            var whatToLV = await readLineAsync("What do you want to levle up? by 2 point Attack(a), by 1 point Defence(d), or Hp(h) by 5 points!?");
            if(whatToLV == "a"){
                playerPerson[3] += attackUp;
                println("Your attack is now " + playerPerson[3]);
                playerPerson[2] = playerPerson[1];
                lVsNeededToLV += 17;
                break;
            }else if(whatToLV == "d"){
                playerPerson[4] += defenceUP;
                println("Your defence is now " + playerPerson[4]);
                playerPerson[2] = playerPerson[1];
                lVsNeededToLV += 17;
                break;
            }else if(whatToLV ==  "h"){
                playerPerson[1] += 5;
                println("Your HP is now " + playerPerson[1]);
                playerPerson[2] = playerPerson[1];
                lVsNeededToLV+= 17;
                break;
            }else {
                println("a, d, or h");
            }
        }
    }
}
//-----------------------------------attack sene 
var battle = false;
async function eniEncounter(){
    //----------------------------------enimes function
    //enimes [/*name*/"",/*Max hp*/0,/*now hp*/0,/*attack*/0,/*defence*/0,/*xp gain*/0,/*gold gain*/0];
    var goblen = [/*name*/"Goblen",/*Max hp*/15 * dificulty,/*now hp*/15 * dificulty,/*attack*/4 * dificulty,/*defence*/2 * dificulty,/*xp gain*/6,/*gold gain*/2];
    var goblenStrong = [/*name*/"Strong goblen Nathan",/*Max hp*/10 * dificulty,/*now hp*/10 * dificulty,/*attack*/6 * dificulty,/*defence*/1 * dificulty,/*xp gain*/10,/*gold gain*/4];
    var goblenWizard = [/*name*/"Goblen Wizard",/*Max hp*/5 * dificulty,/*now hp*/5 * dificulty,/*attack*/8 * dificulty,/*defence*/0 * dificulty,/*xp gain*/8,/*gold gain*/3];
    var goblenMaster = [/*name*/"Goblen Master Logan that sits by me",/*Max hp*/30 * dificulty,/*now hp*/30 * dificulty,/*attack*/8 * dificulty,/*defence*/4 * dificulty,/*xp gain*/16,/*gold gain*/10];
    //-----------------------------------End text
    canMove = false;
    battle = true;
    var encounter;
    var whatEncounter = Randomizer.nextInt(0,2);
    if(bossFight == false){
        if(whatEncounter == 0){
            encounter = goblen;
        }else if(whatEncounter == 1){
            encounter = goblenStrong;
        }else if(whatEncounter == 2){
            encounter = goblenWizard;
        }
        println("Watch out a " + encounter[0] + " has appeared.");
    }else if(bossFight == true){
        encounter = goblenMaster;
        println("Boss fighttttttttttt!!! " + encounter[0] + " is your opponent.");
    }
    var turns = 0;
    var block = false;
    while(true){
        while(turns == 0){
        playUI();
        println("your hp: " + playerPerson[2] + "    enemy hp: " + encounter[2] + " Enemy attack " + encounter[3] + " and defence " + encounter[4]);
        let action = await readLineAsync("attack or defend or use an item? ");
            if(action == "d" || action == "defend"){
                block = true;
                turns++;
                break;
            }else if(action == "a" || action == "attack"){
                let attack = playerPerson[3];
                let eDefence = encounter[4];
                if(attack - eDefence < 0){
                    println(encounter[4] + " takes 0 hit points");
                    turns++;
                    break;
                }else{
                    println(encounter[0] + " takes " + (attack - eDefence) + " hit points!");
                    encounter[2] -= (attack - eDefence);
                    turns++;
                    break;
                }
            }else if(action == "m" || action == "magic"){
                
            }else if(action == "i" || action == "item"){
                await itemChoose();
                turns++;
                break;
            }else{
                println("a or d or i");
            }
        }
        while(turns == 1){
        playUI();
        let eniaOt = Randomizer.nextInt(0,6);
        if(eniaOt >= 2){
            let attack = encounter[3];
            let eDefence = playerPerson[4];
            if(block == true){
                if(eniaOt == 4){
                    let dubDef = playerPerson[4] * 2;
                    let dubAttE = encounter[3] * 2;
                    if(dubAttE - dubDef <= 0){
                        println("You take 0 hit points");
                        block = false;
                        turns--;
                        break
                    }else{
                        println("You take " + (dubAttE - dubDef) + " hit points!!!");
                        playerPerson[2] -= (dubAttE - dubDef);
                        block = false;
                        turns--;
                        break;
                    }
                }else{
                    let dubDef = encounter[4] * 2;
                    if(attack - dubDef <= 0){
                        println("You take 0 hit points");
                        block = false;
                        turns--;
                        break
                    }else{
                        println("You take " + (attack - dubDef) + " hit points");
                        playerPerson[2] -= (attack - dubDef);
                        block = false;
                        turns--;
                        break;
                    }
                }
            }else{
                if(eniaOt == 4){
                    let dubAttE = encounter[3] * 2;
                    if(dubAttE - playerPerson[4] <= 0){
                        println("You take 0 hit points");
                        turns--;
                        break
                    }else{
                        println("You take " + (dubAttE - playerPerson[4]) + " hit points!!!");
                        playerPerson[2] -= (dubAttE - playerPerson[4]);
                        turns--;
                        break;
                    }
                }else if(attack - eDefence <= 0){
                    println("You take 0 hit points");
                }else{
                    println("You take " + (attack - eDefence) + " hit points");
                    playerPerson[2] -= (attack - eDefence);
                    turns--;
                    break;
                }
            }
            turns--;
            break;
        }else if(eniaOt == 1){
            println("He tripted!");
            turns--;
            break;
        }
    }
        //lose or win based on hp and add an item if you get it
        //win
        if(encounter[2] <= 0){
            clear();
            println("You win!");
            await levUp();
            randLoot();
            println("you gained " + encounter[6] + " gold! ");
            encounter[2] = encounter[1];
            playerPerson[5] += encounter[5];
            playerPerson[6] += encounter[6];
            canMove = true;
            battle = false;
            playUI();
            
            break;
        //lose
        }else if(playerPerson[2] <= 0){
            println("You LOSE!");
            removeAll();
            actionLose();
            break;
        }
    }
}
//-----------------------------------Begining and ending cutseens
//so it doesent remove the screen afer the start
var firstTap = 0;
//start screan
function start(){
    setBackgroundColor("pink");
    setSize(ENTIRE_W_AND_H_OF_BOARD * 2, ENTIRE_W_AND_H_OF_BOARD);
    //setFullscreen();
    canMove = false;
    var title = new Text("Simple dungeon", "20pt Arial");
    title.setPosition(getWidth() / 1/4.25 , getHeight() / 1/3);
    var startMdir = new Text("w,a,s,d or arrows to move", "15pt Arial"); 
    startMdir.setPosition(getWidth() / 1/4 , getHeight() / 1/3 + 50);
    var startCon = new Text("Tap to start!", "15pt Arial"); 
    startCon.setPosition(getWidth() / 1/3 , getHeight() / 1/3 + 100);
    add(title);
    add(startMdir);
    add(startCon);
    var mouse = mouseClickMethod(tap);
    function tap(mouse){
            if(firstTap == 0){
            firstTap++;
            removeAll();
            setSizeBut();
        }
    }
}
// Cartor choose
function setSizeBut(){
    var butOne;
    var butTwo;
    var butThree;
    butOne = new Rectangle(getWidth() * (1 / 3), getHeight());
    butOne.setPosition(0, 0);
    butOne.setColor("gray");
    add(butOne);
    var fighterText = new Text("Fighter", "30pt Arial");
    fighterText.setPosition(0, getHeight() / 2);
    butTwo = new Rectangle(getWidth() * (1 / 3), getHeight());
    butTwo.setPosition(getWidth() / 3, 0);
    butTwo.setColor("blue");
    add(butTwo);
    var mageText = new Text("Mage", "30pt Arial");
    mageText.setPosition(getWidth() * (1 / 3), getHeight() / 2);
    butThree = new Rectangle(getWidth() / (1 / 3), getHeight());
    butThree.setPosition(getWidth() / 1.5, 0);
    butThree.setColor("red");
    add(butThree);
    var tankText = new Text("Tank", "30pt Arial");
    tankText.setPosition(getWidth() / 1.5, getHeight() / 2);
    add(mageText);
    add(fighterText);
    add(tankText);
    var name = new Text("The classes", "20pt Arial");
    name.setPosition(getWidth() / 2 - (name.getWidth() / 2), getHeight() / 6);
    add(name);
    mouseClickMethod(buttionPressSize);
    function buttionPressSize(e){
        var elem = getElementAt(e.getX(), e.getY());
        if (elem == butOne) {
            fighter = true;
            removeAll();
            randomGenMap();
            canMove = true;
        }else if (elem == butTwo) {
            mage = true;
            removeAll();
            randomGenMap();
            canMove = true;
        }else if (elem == butThree) {
            tank = true;
            removeAll();
            randomGenMap();
            canMove = true;
        }else{}
    }
}
//Outside UI ENTIRE_W_AND_H_OF_BOARD
var firstTapTwo = 0;
function playUI(){
    /*
    setSize(ENTIRE_W_AND_H_OF_BOARD * 2, ENTIRE_W_AND_H_OF_BOARD);
    var upButon;
    var downButon;
    var leftButon;
    var rightButon;
    if(mapCount == 0){
        var bigWidth = GRID_WID_HIGH * GRID_WIDTH
        var playerHp = new Text("Your HP: " + playerPerson[2], "10pt Arial");
        playerHp.setPosition(bigWidth, 100);
        var playerXp = new Text("Your Xp: " + playerPerson[5], "9pt Arial");
        playerXp.setPosition();
        
        var playergold = new Text("Your Gold: " + playerPerson[6], "10pt Arial");
        playergold.setPosition();
        
        var playerXpNeed = new Text("Xp Needed: " + lVsNeededToLV, "10pt Arial");
        playerXpNeed.setPosition();
        
        var playerAtt = new Text("Your Attack: " + playerPerson[3], "10pt Arial");
        playerAtt.setPosition();
        
        var playerDeff = new Text("Your Defence: " + playerPerson[4], "10pt Arial");
        playerDeff.setPosition();
        add(playerHp); //add(playerXp); add(playergold); add(playerXpNeed); add(playerAtt); add(playerDeff);
        firstTapTwo++;
        
    }
    playerHp.setText("Your HP: " + playerPerson[2]); //playerXp.setText("Your Xp: " + playerPerson[5]); playergold.setText("Your Gold: " + playerPerson[6]); playerXpNeed.setText("Xp Needed: " + lVsNeededToLV); playerAtt.setText("Your Attack: " + playerPerson[3]); playerDeff.setText("Your Defence: " + playerPerson[4]);
    */    
    
    
    }
function enimeUI(){
    if(battle == true){
    var eniHp = new Text("Your HP: " + playerPerson[2], "10pt Arial");
    eniHp.setPosition(ENTIRE_W_AND_H_OF_BOARD, eniHp.getHeight());
    var enirAtt = new Text("Your Attack: " + playerPerson[3], "10pt Arial");
    enirAtt.setPosition(ENTIRE_W_AND_H_OF_BOARD, eniHp.getY() * 2);
    var eniDeff = new Text("  Your Defence: " + playerPerson[4], "10pt Arial");
    eniDeff.setPosition(ENTIRE_W_AND_H_OF_BOARD + enirAtt.getWidth(), eniHp.getY() * 2);
    remove(playerHp); add(playerHp);
    remove(enirAtt); add(enirAtt);
    remove(eniDeff); add(eniDeff)
    }
}
//win screen
function actionwin(){
        removeAll();
        canMove = false;
        let end = new Text("YOU WIN!!!", "20pt Arial");
        end.setPosition(getWidth() / 1/3.5 , getHeight() / 1/3);
        let goodJ = new Text("Good job!", "15pt Arial"); 
        goodJ.setPosition(getWidth() / 1/3 , getHeight() / 1/3 + 50);
        add(end);
        add(goodJ);
    }
// lose screen
function actionLose(){
        removeAll();
        canMove = false;
        let end = new Text("You...", "20pt Arial");
        end.setPosition(getWidth() / 1/3.5 , getHeight() / 1/3);
        let goodJ = new Text("lose.", "15pt Arial"); 
        goodJ.setPosition(getWidth() / 1/3 , getHeight() / 1/3 + 50);
        add(end);
        add(goodJ);
}
