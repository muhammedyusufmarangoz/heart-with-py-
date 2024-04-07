import turtle

def draw_heart():
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def draw_c_in_heart():
    turtle.penup()
    turtle.goto(0, 82)  # Adjust the coordinates to position the "C" inside the heart
    turtle.pendown()

    turtle.color("white")  # Set the text color to white
    turtle.write("#", align="center", font=("Arial", 30, "normal"))

turtle.speed(2)

draw_heart()
draw_c_in_heart()

# Move the turtle to a new position
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

turtle.done()
