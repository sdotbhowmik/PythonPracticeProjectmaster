def f(x):
    return x**3 - x - 1

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

#error tollerance
E = float(input("Enter error tolerance: "))

condition = True
counter =0

while (condition):

    #step2
    f1 = f(x1)
    f2 = f(x2)

    #step3
    if(f1*f2 > 0):
        print("Not correct")
        condition = False

    #step4
    else:
        x0 = x1 - (f1 * (x2 - x1)) / (f2 - f1)
        f0 = f(x0)

    #step5
    if(f1*f0 < 0):
        x2 = x0

    else:
        x1 = x0

    if (abs(f0) < E):
        print(f"Root is {x0}")
        condition = False
    counter = counter+1

    print(f"itteration = {counter}, Root= {x0}, f(x1)={f1}, f(x2)={f2}, f(x0)={f0}")