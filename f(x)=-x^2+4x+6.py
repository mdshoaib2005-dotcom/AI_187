#--------------HILL-CLIMBING-PROBLEM----------------



def f(x):
    return -x**2+4*x+6

x=0
print("Initial x=", x)
print("f(x)=", f(x))
while True:

 left = x-1
 right = x+1

 if f(left) > f(x):
    x = left
 elif f(right) > f(x):
    x = right
 else:
     break

print("Move to x=", x," f(x)= ", f(x))
print("Max Value of f(x)=", f(x))
print("At x=", x)
