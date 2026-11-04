# CTI-110
# P4LAB1 - House Drawing
# Aidan Pelletant
# November 4, 2026
#
# Pseudocode:
# 1. Import  turtle.
# 2. Create the screen/window and the turtle pen object.
# 3. Set custom background color, pen size, color, and shape.
# 4. Use a FOR loop to draw the 4 sides of the square base.
# 5. Lift the pen, move the turtle to the top of the square, and put the pen down.
# 6. Use a WHILE loop to draw the 3 sides of the triangle roof.
# 7. Keep the drawing window open using win.mainloop().

import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
win.bgcolor("lightblue")

pen = turtle.Turtle()
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

# 1. Draw the Square Base using a FOR loop
for side in range(4):
    pen.forward(100)
    pen.left(90)

# Move the turtle into position for the roof (top of the square)
pen.penup()
pen.goto(0, 100)
pen.setheading(0)
pen.pendown()

# 2. Draw the Triangle Roof using a WHILE loop
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

# Hide the turtle when done drawing
pen.hideturtle()

# Wait for user to close window
win.mainloop()