def f(x):
    return x**3 - x - 1

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
E = 0.001
program = input("Enter which program you want to run e.g 1=Bisection, 2=False_Possition: ")

def bisection(x1, x2, E):
    condition = True
    while (condition):

        # step2
        f1 = f(x1)
        f2 = f(x2)
        print(f"f1={f1}, f2={f2}")

        # step3
        if (f1 * f2 > 0):
            print("Not correct")
            condition = False

        # step4
        else:
            x0 = (x1 + x2) / 2
            f0 = f(x0)

        # step5
        if (f1 * f0 < 0):
            x2 = x0

        else:
            x1 = x0

        if (abs(f0) < E):
            print(f"Root is {x0}")
            condition = False

def falsePosssition(x1, x2, E):
    condition = True
    while condition:
        # Step 2: Calculate f1 and f2
        f1 = f(x1)
        f2 = f(x2)
        print(f"f1={f1}, f2={f2}")

        # Step 3: Check if initial guesses are correct
        if f1 * f2 > 0:
            print("Initial guesses are not correct.")
            condition = False
        else:
            # Step 4: Calculate x0 using false position method
            x0 = (x1 * f2 - x2 * f1) / (f2 - f1)
            f0 = f(x0)

            # Step 5: Update x1 or x2 based on the sign of f1*f0
            if f1 * f0 < 0:
                x2 = x0
            else:
                x1 = x0

            # Check if the absolute value of f0 is less than the tolerance level E
            if abs(f0) < E:
                print(f"Root is {x0}")
                condition = False

if (program==1):
    bisection(x1,x2,E)

else:
    falsePosssition(x1,x2,E)