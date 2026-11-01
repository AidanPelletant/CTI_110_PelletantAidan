# -----------------------------------------------------------------------------
# Name: P4LAB1_PelletantAidan
# Description: This program uses Python's turtle graphics library, incorporating 
#              both a for loop and a while loop to draw a house (square base and 
#              triangle roof) filled with green.
#
# Pseudocode:
# 1. Import the turtle module.
# 2. Set up the screen and turtle properties.
# 3. Use a FOR loop to draw and fill the square base.
# 4. Lift the pen, move precisely to the top-left corner, and put the pen down.
# 5. Use a WHILE loop to draw and fill the triangle roof so it aligns with the square.
# 6. Hide the turtle and keep the graphics window open until clicked.
# -----------------------------------------------------------------------------

import turtle

def draw_house():
    # Set up screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black", "green")  # Outline in black, fill with green
    t.pensize(2)
    t.speed(3)
    
    # 1. Draw and fill the square base using a FOR loop
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
        
    # 2. Position the turtle for the roof without drawing lines
    t.penup()
    t.goto(0, -100)          # Go back to the starting bottom-left corner
    t.setheading(90)      # Face North (up)
    t.forward(100)        # Move straight up the left wall to the top-left corner
    t.setheading(0)       # Face East (right) to align with the top edge
    t.pendown()

    # 3. Draw and fill the triangle roof using a WHILE loop
    t.begin_fill()
    sides_drawn = 0
    while sides_drawn < 3:
        t.forward(100)
        t.left(120)       # 120-degree turn for equilateral triangle vertices
        sides_drawn += 1
    t.end_fill()

    # Hide the turtle when finished
    t.hideturtle()
    
    # Keep the window open until clicked
    turtle.done()

if __name__ == "__main__":
    draw_house()