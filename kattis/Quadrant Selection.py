def quadrant(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3
            
            
x_in = int(input())
y_in = int(input())

print(quadrant(x_in, y_in))