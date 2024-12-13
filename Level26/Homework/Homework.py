import turtle


def draw_triangle(side_length, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

side_length = 50  
num_triangles = 120 


turtle.speed(0)
turtle.penup()
turtle.setposition(-200, 200)  
turtle.pendown()


for i in range(num_triangles):
    if i % 2 == 0: 
        draw_triangle(side_length, "green")
    else:  
        draw_triangle(side_length, "blue")

  
    turtle.penup()
    turtle.forward(side_length + 10)  
    turtle.pendown()


turtle.done()
