n = eval(input("请输入菱形的总长度"))
if n%2 == 0:
    print('总长度必须是奇数')
    exit()

column = int ((n+1)/2)
col = int ((n+1)/2)
for i in range(1,n+1) :
    for j in range(1, column+1) :
        if col - i >= 0 :
            start  = col - i + 1
        else :
            start = i - col + 1
        if j == column or j == start :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()
    if i < (n + 1) / 2:
        column += 1
    else :
        column -= 1
