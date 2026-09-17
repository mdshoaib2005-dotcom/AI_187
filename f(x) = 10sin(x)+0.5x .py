# f(x) = 10sin(x)+0.5x where 0<=x<=20
# Initial x=2
# Neighbour: x+0.1 and x-0.1
# Find the maximum value of f(x)



import math

def f(x):
    return 10*math.sin(x) + 0.5*x 

x = 2
y = 0.1

print("Initial x=", x)
print("Initial f(x)=", f(x))

while True:
    x_left = x - y
    x_right = x + y

    if x_left < 0:
        x_left = x
    if x_right > 20:
        x_right = x    


    if f(x_left) > f(x):
        x = x_left
    elif f(x_right) > f(x):
        x = x_right
    else:
        break

print("Maximum found:")
print("x=", round(x, 2))
print("f(x)=", round(f(x), 4))



                       