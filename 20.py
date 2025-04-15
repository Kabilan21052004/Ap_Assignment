def oddCollatz(n):
    while n != 1:
        if n % 2 != 0:
            print(n)
            n = 3*n + 1
        else:
            n = n // 2
    if n == 1:
        print(1)
oddCollatz(7)