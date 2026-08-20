def fill_A(x,y):
    return(4,0)
def fill_B(x,y):
    return(0,3)

def Empty_A(x,y):
    return(0,y)
def Empty_B(x,y):
    return(x,0)

def Transfer_A_to_B(a,b):
    if a<=3-b:
        return(0,a+b)
    else:
        return(a-(3-b),3)
def Transfer_B_to_A(a,b):
    if b<=4-a:
        return(a+b,0)
    else:
        return(4,b-(4-a))

def bfs():

    queue = [(0, 0)]

    visited = [(0, 0)]

    while queue:

        current = queue.pop(0)

        a, b = current

        print(current)

        # Goal

        if a == 2:

            print("Goal reached!")

            return

        states = [

            fill_A(a, b),

            fill_B(a, b),

            Empty_A(a, b),

            Empty_B(a, b),

            Transfer_A_to_B(a, b),

            Transfer_B_to_A(a, b)

        ]

        for state in states:

            if state not in visited:

                visited.append(state)

                queue.append(state)

bfs()    

