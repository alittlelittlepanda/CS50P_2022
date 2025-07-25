for i in range(1,10):
    for j in range(1,10):
        if i<j :
            continue
        else :
            print(i,'*',j,'=',i*j,sep='',end=' ')
    print('\n')