for no in range(1, 1001):
    sum = 0
    save = no
    count = 0

    temp = no

    # Count digits
    while temp > 0:
        temp = temp // 10
        count = count + 1

    temp = no

    # Armstrong check
    while temp > 0:
        rem = temp % 10
        sum = sum + (rem ** count)
        temp = temp // 10

    if sum == save:
        print("no is armstrong ",i)