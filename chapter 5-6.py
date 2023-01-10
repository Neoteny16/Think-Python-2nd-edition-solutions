import turtle, random
turtle.speed("fastest")
turtle.tracer(0, 0)
turtle.colormode(255)
turtle.bgcolor('black')
def koch(t, length, curve):
    """ Make koch curve with
    length - int
    curve - length of the curve
    """
    if length <= curve:
        t.fd(length)
        return
    koch(t, length/3, curve)
    t.lt(60)
    koch(t, length/3, curve)
    t.rt(120)
    koch(t, length/3, curve)
    t.lt(60)
    koch(t, length/3, curve)
def snowflake(t, length, angle, curve=18):
    """ Snowflake using for loop
        t = Turtle object
        length = length of Koch curve(int)
        angle = angle of snowflake(must be divisor of 360)
        curve - length of the koch curve
        """
    if 360 % angle != 0:
        print("angle must be divisor of 360")
    for i in range(360//angle):
        koch(t, length, curve)
        t.rt(angle)
bob = turtle.Turtle()
bob.color("red")    
angle = 45
for i in range(360//angle):
    dom = random.randint(90, 180)
    dom1 = random.randint(90, 180)
    dom2= random.randint(90, 180)
    bob.color(dom, dom1, dom2)
    snowflake(bob, 500, 60, 3)
    bob.rt(angle)
turtle.update()
turtle.mainloop()






# koch(bob, 120)

# def snowflake(t, length, angle, sum=0):
#     """ Draws snowflake using koch curve and recursion
#         t = Turtle object
#         length = length of Koch curve(int)
#         angle = angle of snowflake(must be divisor of 360)
#         sum = sum of angle to make full circle snowflake
#     """
#     print(angle)
#     print('sum', sum)
#     if 360 % angle != 0:
#         print("angle must be divisor of 360")
#         return 
#     elif sum >= 360:
#         # t.
#         return
    
#     t.rt(angle)
#     koch(t, length)
#     snowflake(t, length, angle, sum+angle)