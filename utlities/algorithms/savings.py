def calc_savings():

    r = 0.0005
    p = int(input("How many initial savings do you have? "))
    d = int(input("How much do you want to contribute to your savings daily? "))
    t = int(input("For how many days? "))

    total = p
    for i in range(1, t+1):
        total = total * (1 + r) + d

    return total
