column = 0
for i in range(9):
    if i<=4 :
        column = 5+i
    else :
        column -= 1
    for j in range(column):
        if 4-i >= 0 :
            temp = 4-i
        else :
            temp = i-4
        if j < temp :
            print(" ", end = '')
        else :
            print('*', end = '')
    print()