//same issuse as the blood fall burrows dont know the import for thos :(
// large medum or small crust
var R_SMALL_CRUST = 75;
var R_SMALL_SAUSE_CHEZE = R_SMALL_CRUST / (1.1);
var R_MED_CRUST = R_SMALL_CRUST * 1.5;
var R_MED_SAUSE_CHEZE = R_MED_CRUST / (1.1);
var R_LARGE_CRUST = R_SMALL_CRUST * 2;
var R_LARGE_SAUSE_CHEZE = R_LARGE_CRUST / (1.1);
var R_TOP = R_SMALL_SAUSE_CHEZE / 8;
//grid stuff
var TOP_SIZE_X = 3
var TOP_SIZE_Y = 2
var SIZE_OF_OBJECTS_X = getWidth() / TOP_SIZE_X;
var SIZE_OF_OBJECTS_Y = getHeight() / TOP_SIZE_Y;
//the topings
var size = "";
var sau = false;
var che = false;
var pep = false;
var olv = false;
var mush = false;
//the grid
var topings = new Grid(TOP_SIZE_Y, TOP_SIZE_X);
topings.initFromArray([
    ["Sauce","Cheese","Pepperoni ",],
    ["Olives","Mushrooms","    Make"]
]);
function start(){
    setSizeBut();
}
//adds the L M or S buttions and has user tap input
function setSizeBut(){
    var smallB;
    var medB;
    var largeB;
    smallB = new Rectangle(getWidth() * (1 / 3), getHeight());
    smallB.setPosition(0, 0);
    smallB.setColor("green");
    add(smallB);
    var smallBText = new Text("Small", "30pt Arial");
    smallBText.setPosition(0, getHeight() / 2);
    medB = new Rectangle(getWidth() * (1 / 3), getHeight());
    medB.setPosition(getWidth() / 3, 0);
    medB.setColor("white");
    add(medB);
    var medBText = new Text("Medium", "25pt Arial");
    medBText.setPosition(getWidth() * (1 / 3), getHeight() / 2);
    largeB = new Rectangle(getWidth() / (1 / 3), getHeight());
    largeB.setPosition(getWidth() / 1.5, 0);
    largeB.setColor("red");
    add(largeB);
    var largeBText = new Text("Large", "30pt Arial");
    largeBText.setPosition(getWidth() / 1.5, getHeight() / 2);
    add(medBText);
    add(smallBText);
    add(largeBText);
    var name = new Text("Pizza shop choose what pizza size you want!", "15pt Arial");
    name.setPosition(0, getHeight() / 6);
    add(name);
    mouseClickMethod(buttionPressSize);
    function buttionPressSize(e){
        var elem = getElementAt(e.getX(), e.getY());
        if (elem == smallB) {
            size = "small";
            removeAll();
            setTopBut();
        }else if (elem == medB) {
            size = "medium";
            removeAll();
            setTopBut();
        }else if (elem == largeB) {
            size = "large";
            removeAll();
            setTopBut();
        }else{}
    }
}
// makes grid buttions and tap function to change the color then slect it
function setTopBut(){
    var b = 1;
    var colorChoose = ["red",Color.RED,"#FC2E2E","#E42424","#C61717","gray"];
    // THIS IS A TEST var colorChoose = ["gray",Color.RED,"blue","pink","green","gray"];
    for(var y = 0; y < TOP_SIZE_Y; y++){
        b -= 1;
        for(var x = 0; x < TOP_SIZE_X; x++){
            var topingName =  topings.get(y, x);
            var butte = new Rectangle(getWidth() / 3 , getHeight() /2);
            butte.setPosition((x * SIZE_OF_OBJECTS_X), (y * SIZE_OF_OBJECTS_Y));
            butte.setColor(colorChoose[(y + b)]);
            b++;
            add(butte);
            var nameOfThing = new Text(topingName, "19pt Arial");
            nameOfThing.setPosition(butte.getX(), butte.getY() + butte.getHeight() / 2);
            add(nameOfThing);
        }
    }
    mouseClickMethod(buttionPressTop);
    function buttionPressTop(e){
        var elem = getElementAt(e.getX(), e.getY());
        if(elem != null){
            if(elem.getColor() == colorChoose[0]){
                elem.setColor("green");
                sau = true;
            }else if(elem.getColor() == colorChoose[1]){
                elem.setColor("green");
                che = true;
            }else if(elem.getColor() == colorChoose[2]){
                elem.setColor("green");
                pep = true;
            }else if(elem.getColor() == colorChoose[3]){
                elem.setColor("green");
                olv = true;
            }else if(elem.getColor() == colorChoose[4]){
                elem.setColor("green");
                mush = true;
            }else if(elem.getColor() == colorChoose[5]){
                removeAll();
                pizzaMake();
            }else{
            }
        }
    }
}
// maes the pizza and has an click to "eat" function
function pizzaMake(){
    var ranch = new WebImage("https://i5.walmartimages.com/asr/c53362a2-fbcb-408c-88bf-36db3bcd72a4_2.6ca568e9e8a7510a0fd7a345d03f62c9.jpeg");
    ranch.setSize(150, 150);
    ranch.setPosition( - 40, getHeight() / 2 - 150);
    add(ranch);
    var sizee;
    var topCount;
    var pizzaCrust;
    var pizzaSorC;
    var xRad;
    var yRad;
    if(size == "small"){
        pizzaCrust = new Circle(R_SMALL_CRUST);
        pizzaSorC = new Circle(R_SMALL_SAUSE_CHEZE);
        xRad = R_SMALL_SAUSE_CHEZE;
        yRad = R_SMALL_SAUSE_CHEZE;
        topCount = 10;
        sizee = R_SMALL_CRUST;
    }else if(size == "medium"){
        pizzaCrust = new Circle(R_MED_CRUST);
        pizzaSorC = new Circle(R_MED_SAUSE_CHEZE);
        xRad = R_MED_SAUSE_CHEZE;
        yRad = R_MED_SAUSE_CHEZE;
        topCount = 15;
        sizee = R_MED_CRUST;
    }else if(size == "large"){
        pizzaCrust = new Circle(R_LARGE_CRUST);
        pizzaSorC = new Circle(R_LARGE_SAUSE_CHEZE);
        xRad = R_LARGE_SAUSE_CHEZE;
        yRad = R_LARGE_SAUSE_CHEZE;
        topCount = 20;
        sizee = R_LARGE_CRUST;
    }
    pizzaCrust.setPosition(getWidth() / 2, getHeight() / 2);
    pizzaCrust.setColor("#dba24a");
    add(pizzaCrust);
    if(che == true){
        pizzaSorC.setColor("#e1d800");
        pizzaSorC.setPosition(getWidth() / 2, getHeight() / 2);
        add(pizzaSorC);
    }else if(sau == true){
        pizzaSorC.setColor("#e12301");
        pizzaSorC.setPosition(getWidth() / 2, getHeight() / 2);
        add(pizzaSorC);
    }else{}
    if(pep == true){
        for(var q = 0; q < topCount; q++){
            //randmised this baces off a distance and an angle
            var distance = Randomizer.nextInt(0, (pizzaSorC.getRadius() * 2) - sizee - R_TOP );
            var angle = Randomizer.nextInt(0, 360);
            //convert angle to radians
            angle *= Math.PI / 180;
            var distX = Math.sin(angle) * distance;
            var distY = Math.cos(angle) * distance;
            var insertPep = new WebImage("https://upload.wikimedia.org/wikipedia/commons/f/f1/Heart_coraz%C3%B3n.svg");
            insertPep.setSize(R_TOP * 3, R_TOP * 3);
            insertPep.setPosition(getWidth() / 2 + distX, getHeight() / 2 + distY);
            insertPep.setColor("#981515");
            add(insertPep);
        }
        
        pizzaSorC
    }
    if(olv == true){
        for(var w = 0; w < topCount; w++){
            //randmised this baces off a distance and an angle
            var distance = Randomizer.nextInt(0, (pizzaSorC.getRadius() * 2) - sizee - R_TOP );
            var angle = Randomizer.nextInt(0, 360);
            //convert angle to radians
            angle *= Math.PI / 180;
            var distX = Math.sin(angle) * distance;
            var distY = Math.cos(angle) * distance;
            var insertOlv = new Circle(R_TOP);
            insertOlv.setPosition(getWidth() / 2 + distX, getHeight() / 2 + distY);
            insertOlv.setColor("black");
            add(insertOlv);
        }
    }
    if(mush == true){
        for(var e = 0; e < topCount; e++){
            //randmised this baces off a distance and an angle
            var distance = Randomizer.nextInt(0, (pizzaSorC.getRadius() * 2) - sizee - R_TOP );
            var angle = Randomizer.nextInt(0, 360);
            //convert angle to radians
            angle *= Math.PI / 180;
            var distX = Math.sin(angle) * distance;
            var distY = Math.cos(angle) * distance;
            var insertMush = new Circle(R_TOP);
            insertMush.setPosition(getWidth() / 2 + distX, getHeight() / 2 + distY);
            insertMush.setColor("gray");
            add(insertMush);
        }
    }
    mouseClickMethod(eat);
    function eat(kli){
        var eating = new Circle(26);
        eating.setPosition(kli.getX(), kli.getY())
        eating.setColor("white");
        add(eating);
    }
    mouseDragMethod(eatDrag);
    function eatDrag(klik){
        var eating = new Circle(26);
        eating.setPosition(klik.getX(), klik.getY())
        eating.setColor("white");
        add(eating);
    }
}
