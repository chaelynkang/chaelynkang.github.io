i, k = 0, 0

i = 0
while i < 9 :
    if i < 5 :
        k = 0
        while k < 4 - i :
            print(' ', end = ' ')
            k += 1
        k = 0
        while k < i * 2 + 1 :
            print('\u2665', end = ' ')
            k += 1
    else :
        for k in range(0,i-4):
            print (' ', end=' ')
        for k in range((9-i)*2-1) :
            print('\u2665', end=' ')
    print()
    i += 1