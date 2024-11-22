#need to import tracy and change all tracy comands to have the tracy.wdiaudiuawhhdiuah to it
print("Welcome to make your own spider web!")
"""imports math for sin and cos to make web"""
import math
speed(0)
"""askes user for background color and web color"""
bgcolor(input("What color background? "))
collor = input("What color web? ")
color(collor)
howmany = int(input("How many webs circles? "))
for i in range(0, 360, 45):
    left(i)
    forward(900)
    goto(0,0)
    setheading(0)
for radius in range(20, 200, (200 / (howmany))):
    up() 
    goto(radius, 0) 
    down()
    for angle in range(-135, (360 + 45 - 135), 45): 
        """draw the web using sin and cos to get positions"""
        right(-angle)
        circle(radius, 45)
        setheading(0)
        up(); goto(0, 0)
        down()
        goto(-radius * math.cos(math.radians(angle)), -radius * math.sin(math.radians(angle)))
print("Now make your own design!")
print("Click around to draw.")
up()
goto(0,0)
down()
# Save screen to canvas variable
canvas = getscreen()
def move_to_cursor(x, y): 
  goto(x, y)
# Call move_to_click function when canvas is clicked
canvas.onclick(move_to_cursor)
upp = True
poss_color = ["black", "blue","brown","cyan","gold","gray","green","indigo","orange","pink","purple","red","violet","white","yellow", "silver"]
while True:
    print("Type an int to change size.")
    print("Type a color to change color. " + collor)
    jeff = input("Type a Type anything to put pen up / down. Your pen is down? " + str(upp) + " ")
    try:
        int(jeff)
        pensize(jeff)
    except ValueError:
        for color_check in poss_color:
            if jeff == color_check:
                color(jeff)
                collor = jeff
        if jeff != collor:
            if upp:
                up()
                upp = False
            else:
                down()
                upp = True
