import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('red')
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t2.hideturtle()
t3.hideturtle()
FORCE_FACTOR = 30

#intro screen
t.penup()
t.goto(0, 100)
t.pendown()
t.write('', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 0)
t.pendown()
screen.addshape('turtle.gif')
t.shape('turtle.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(0, -100)
t.pendown()


t.write('Miss', font=("ariel", 30, "italic"), align="center")
round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('tan')

hit = 0
attempt = 1
while attempt <= 5:
    t2.penup()
    t2.goto(0, 200)
    t2.pendown()

    t.setheading(0)
    #variables
    target_x = random.randint(50,170)
    sign_x = random.randint(1,2)
    if sign_x == 2:
        target_x = random.randint(-250,-130)
    TARGET_L_LEFT_X = target_x
    TARGET_L_LEFT_Y = random.randint(-250, 170)
    SIDES = random.randint(20,80)
    FORCE_FACTOR= 30
    hit = 0
    attempt = 2


    t.penup()
    t.goto(TARGET_L_LEFT_X, TARGET_L_LEFT_Y)
    t.pendown()

    t.forward(SIDES)
    t.left(90)
    t.forward(SIDES)
    t.left(90)
    t.forward(SIDES)
    t.left(90)
    t.forward(SIDES)
    t.left(90)

    t.penup()
    t.goto(0,0)
    t.pendown()

    t.setheading(0)

    angle = float(input("Enter the angle: "))
    force = float(input("Enter a force (1-10): "))

    distance = force*FORCE_FACTOR

    t.setheading(angle)
    t.penup()
    t.speed(1)
    t.forward(distance)
    t.speed(0)

    if (t.xcor() >= TARGET_L_LEFT_X and t.ycor() <= TARGET_L_LEFT_Y + SIDES) and (t.ycor() >= TARGET_L_LEFT_Y and t.ycor() <= TARGET_L_LEFT_Y + SIDES):
        t2.write("Hit", font =("ariel", 30, "italic"),align = "center")
        hit += 1

    else:
        t2.write("Miss", font =("ariel", 30, "italic"),align = "center")
    t3.penup()
    t3.goto(0,150)
    t3.pendown()
    t3.clear()
    t3.write(str(hit)+"/"+str(attempt), font =("ariel", 30, "italic"),align = "center")

    round = input("Press Enter to Continue: ")
    t.clear()
    t2.clear()
    t3.penup()
    t3.goto(0, -100)
    t3.pendown()
    hit = 1
    if attempt == 5:
        if hit >=4:
            t.write('Sniper', font=("ariel", 30, "italic"), align="center")
        elif hit >= 2:
            t.write('Pretty Good, Keep Practicing', font=("ariel", 30, "italic"), align="center")
        else:
            t.write('Practice, Practice, Practice', font=("ariel", 30, "italic"), align="center")

    round = input("Press Enter to Continue: ")
    attempt = attempt + 1
#End Screen
t.clear()
t2.clear()
t3.clear()
screen.bgcolor('dodgerblue')
t.penup()
t.goto(0, 100)
t.pendown()
t.write('Game', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 0)
t.pendown()
screen.addshape('turtlefiveleg.gif')
t.shape('turtlefiveleg.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(0, -100)
t.pendown()
t.write('Over', font=("ariel", 30, "italic"), align="center")
round = input("Press Enter to Continue: ")
turtle.done()