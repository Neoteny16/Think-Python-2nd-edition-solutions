import turtle, math
bob = turtle.Turtle()
# print(bob)

# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
def invsquare(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(-90)
# square(bob, 200)

# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)


# def circle(t, r):
#     circ = 2 * math.pi * r
#     n = int(circ/3) + 1
#     length = circ / n
#     polygon(t, length, n)
    
# polygon(bob, 50, 5)
# circle(bob, 50)
# square(bob, -100)
# square(bob, 100)
# circle(bob, -50)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    # print(arc_length,'yg')
    n = int(arc_length/2) + 1
    # print(n)
    step_length = arc_length / n
    step_angle = angle / n
    # print(step_length,step_angle)
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        # raise Exception

def circle(t, r):
    arc(t, r, 360)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
arc(bob, 50, 180)
invsquare(bob, 100)
arc(bob, 50, -180)
# bob.fd(2)      # fixed probblem of approxiamtion for this task before author mentioned it
bob.rt(90)
bob.fd(100)
square(bob, 100)
bob.rt(45)

# circle(bob, 60)











print('Fuck off mate')

turtle.mainloop()




