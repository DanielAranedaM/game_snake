import turtle
import time
import random

delay = 0.1
body_segments = []
score = 0
record = 0

wn = turtle.Screen()
#titulo (wn=windows)
wn.title("Juego SNAKE")
#tamaño ventana(wn)
wn.setup(width=600,height=600)
#color fondo
wn.bgcolor('light green')

#head Snake
#objeto turtle
head = turtle.Turtle()
#para que se quede fijo
head.speed(0)
#forma
head.shape('square')
#head color
#para no dejar rastro de la animacion
head.penup()
head.color('red')
#centrar
head.goto(0,0)
#para hacer que el programa espere la orden de mover
head.direction = "stop"

#comida de snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)
food.direction = "stop"

#puntaje
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write(f'Score: 0        Record: 0', align="center", font=("Impact", 24))

#movimiento
def mov():
    if head.direction == "up":
        #almacena el valor actual de la coordenada (Y)
        y = head.ycor()     
        head.sety(y +10)

    if head.direction == "down":
        #almacena el valor actual de la coordenada (Y)
        y = head.ycor() 
        head.sety(y -10)

    if head.direction == "right":
        #almacena el valor actual de la coordenada (X)
        y = head.xcor()        
        head.setx(y +10)

    if head.direction == "left":
        #almacena el valor actual de la coordenada (X)
        y = head.xcor()        
        head.setx(y -10)
#funcion para direcciones
def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"

#conectar teclado con el programa
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")


while True:
    wn.update()
    #colision con la ventana
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #esconder segmentos
        for segment in body_segments:
            segment.goto(1000,1000)
        #limpiar los segmentos    
        body_segments.clear()
        score = 0
        text.clear()
        text.write(f'Score: {score}        Record: {record}', align="center", font=("Impact", 24))

    #colision contra la comida
    if head.distance(food) < 20:
        x = random.randint(-280 ,280)
        y = random.randint(-280 ,280)
        food.goto(x,y)
        #nuevo segmento de snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.penup()
        new_segment.color('red')
        body_segments.append(new_segment)

        #actualizar puntajes
        score += 10
        if score > record:
            record = score
        text.clear()
        text.write(f'Score: {score}        Record: {record}', align="center", font=("Impact", 24))

    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)

    mov()

    #colicion con el cuerpo
    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #esconder segmentos
            for segment in body_segments:
                segment.goto(1000,1000)
            
            body_segments.clear()
            
            score = 0
            text.clear()
            text.write(f'Score: {score}        Record: {record}', align="center", font=("Impact", 24))


    time.sleep(delay)



turtle.done()

