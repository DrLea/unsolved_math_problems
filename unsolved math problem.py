import turtle
tur= turtle.Turtle()

counter = 1
wasUp = True

def fto(a):
    global wasUp
    b = 0
    if(a%2==0):
        a/=2
        if(wasUp==True):
            tur.right(150)
            wasUp=False
            b = tur.position()[1]/2
        tur.fd(b)
    else:
        a=a*3+1
        if(wasUp==False):
            tur.left(150)
            wasUp=True
            b = tur.position()[1]*3+1
        tur.fd(b)
    if(a!=1):
        global counter
        counter += 1
        if (tur.position()>(300,-300)):
            tur.penup()
            tur.goto(-300,0)
            tur.pendown()
        return(fto(a))




tur.left(75)
tur.penup()
tur.goto(-300,0)       
tur.pendown()



fto(1125)
print(counter)



input()