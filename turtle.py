import turtle 

snel = turtle.Turtle()
skk = turtle.Turtle() 
skk.color("red") 
snel.speed(5)
snel.fillcolor("green")

for i in range(360):
    snel.begin_fill() 
    snel.forward(100)
    snel.right(30)
    snel.forward(20)
    snel.left(60)
    snel.forward(50)
    snel.right(30)
    
    snel.penup()
    snel.setposition(0, 0)
    snel.pendown()
    
    snel.right(2)
    snel.end_fill() 
    
turtle.done()
