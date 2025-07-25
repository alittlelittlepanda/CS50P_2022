for i in range(100, 1000):
    sum = 0
    temp = i
    for j in range(3):
        digit = temp%10
        temp = int(temp/10)
        sum += digit ** 3
    if sum == i:
        print(i)