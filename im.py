from turtle import *

def fun():
    hideturtle()
    colors = ['orange', 'darkMagenta', 'red', 'DeepPink', 'DarkGoldenrod1']
    pencolor(colors[3])
    pensize(10)
    circle(50)
# Move the turtle to a new position for the next drawing
    up()
    goto(-50, -25)
    down()
    for i in range(4):
        pencolor(colors[i])
        forward(100)
        circle(25, 90)   
# Move the turtle to a new position for the small circle
    up()
    goto(55, 95)
    down()
# Draw the small circle with red color
    pencolor(colors[2])
    circle(5, 360)
    
def write_text(message, pos, color):
    up()
    goto(pos)
    down()
    pencolor(color)
    write(message, align="center", font=("Comic Sana MS", 18, "bold"))

fun()
# Add text without animation
write_text("Instagram Management System", (0, -150), "black")
write_text("Managed By: Eman Razi",(0,-180),'DeepPink')

# Keep the window open
done()