import turtle as t

screen = t.Screen()
screen.tracer(0)
pen = t.Turtle()
pen.hideturtle()

def draw_circle(pen, x, y, radius):
    pen.penup()
    pen.goto(x, y-radius)
    pen.pendown()
    pen.pensize(3)
    pen.pencolor("orange")
    pen.circle(radius)

def draw_rectangle(pen, x, y, w, h):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pensize(3)
    pen.pencolor("orange")
    for i in range(2):
        pen.forward(w)
        pen.right(90)
        pen.forward(h)
        pen.right(90)

def draw_text(pen, x, y, text):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pencolor("red")
    pen.write(text, font=("Comic Sans MS", 30, "normal"), align="center")

def is_collision(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, r2 = rect2
    x_left = x1
    x_right = x1 + w1
    y_top = y1
    y_bottom = y1 - h1

    if x2 < x_left:
        xA = x_left
    elif x2 > x_right:
        xA = x_right
    else:
        xA = x2

    if y2 > y_top:
        yA = y_top
    elif y2 < y_bottom:
        yA = y_bottom
    else:
        yA = y2

    return (x2 - xA)**2 + (y2 - yA)**2 <= r2**2

def notify_impact(rect1, rect2):
    if is_collision(rect1, rect2):
        draw_text(pen, 0, 300, "2 hình đã va chạm")
    else:
        draw_text(pen, 0, 300, "2 hình đang di chuyển")

def update_shape():
    draw_rectangle(pen, x1, y1, w1, h1)
    draw_circle(pen, x2, y2, r2)

    rect1 = (x1, y1, w1, h1)
    rect2 = (x2, y2, r2)
    notify_impact(rect1, rect2)

    screen.update()


def move_up():
    global x1, y1, w1, h1, x2, y2, r2
    pen.clear()
    y2 += 5
    update_shape()

def move_down():
    global x1, y1, w1, h1, x2, y2, r2
    pen.clear()
    y2 -= 5
    update_shape()

def move_left():
    global x1, y1, w1, h1, x2, y2, r2
    pen.clear()
    x2 -= 5
    update_shape()

def move_right():
    global x1, y1, w1, h1, x2, y2, r2
    pen.clear()
    x2 += 5
    update_shape()

x1 = -10
y1 = -10
w1 = 200
h1 = 100

x2 = -100
y2 = -100
r2 = 75

draw_rectangle(pen, x1, y1, w1, h1)
draw_circle(pen, x2, y2, r2)

update_shape()
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.listen()
t.done()