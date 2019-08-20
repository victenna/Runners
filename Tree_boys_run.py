import turtle
import time
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t1.speed(10)
t2.speed(10)
t3.speed(10)


wn = turtle.Screen()
wn.bgcolor('green')
wn.setup(800,800)
wn.bgpic('field.gif')
turtle.tracer(2)

image1=['boy11.gif','boy12.gif','boy13.gif','boy14.gif']
image2=['boy21.gif','boy22.gif','boy23.gif','boy24.gif']
image3=['boy31.gif','boy32.gif','boy33.gif','boy34.gif']

t1.up()
t1.hideturtle()
X1=-600
t1.goto(X1,-50)
t1.speed(1)
t1.setheading(90)
t1.showturtle()

t2.up()
t2.hideturtle()
X2=-450
t2.goto(X2,110)
t2.speed(1)
t2.setheading(90)
t2.showturtle()

t3.up()
t3.hideturtle()
X3=-300
t3.goto(X3,200)
t3.speed(1)
t3.setheading(90)
t3.showturtle()

delta=7
i=0
import winsound
winsound.PlaySound('music3.wav', winsound.SND_ASYNC)

while True:
  if X1>400:
    X1=-600
    t1.hideturtle()
    t1.goto(-600,-50)
    t1.showturtle()

 
    X2=-450
    t2.hideturtle()
    t2.goto(-500,110)
    t2.showturtle()

 
    X3=-300
    t3.hideturtle()
    t3.goto(-300,200)
    t3.showturtle()
    
  i1=i%4
  wn.addshape(image1[i1])
  t1.shape(image1[i1])
  t1.goto(X1,-50)
  X1=t1.xcor()
  X1=X1+delta

  wn.addshape(image2[i1])
  t2.shape(image2[i1])
  t2.goto(X2,110)
  X2=t2.xcor()
  X2=X2+delta

  wn.addshape(image3[i1])
  t3.shape(image3[i1])
  t3.goto(X3,200)
  X3=t3.xcor()
  X3=X3+delta
  i=i+1
#time.sleep(0.4)
