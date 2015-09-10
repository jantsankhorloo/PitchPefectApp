import turtle
import random


#def draw_square():
    #window = turtle.Screen()
#    window.bgcolor("black")
#
#    jimi = turtle.Turtle()
#    jimi.speed(20)
##
 #   distance = 120
 #   colors = ["white", "yellow", "green", "blue", "red", "purple"]

 #   for laps in range(0,15):
 #       for in_laps in range(0,3):
 #           jimi.color(colors[int(random.randrange(0,len(colors)))])
 #           jimi.forward(distance + laps*2)
 #           jimi.right(90 + in_laps*3)
 #   window.exitonclick()
#draw_square()



def draw_square(turtle1):
    for i in range(1, 5):
        turtle1.forward(100)
        turtle1.right(90)

#def draw_triangle(turtle):
    #for i in range(3):
 #       turtle.right(120)
 #       turtle.forward(100)

#def draw_circle(turtle):
    #turtle.circle(100)

def main():
    window = turtle.Screen()
    window.bgcolor("lightgray")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
    #draw_circle(brad)
    #draw_triangle(brad)

    window.exitonclick()

main()
