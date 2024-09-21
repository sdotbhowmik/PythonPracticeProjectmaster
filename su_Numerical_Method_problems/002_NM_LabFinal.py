def F(x):
    return x**2 - 3*x + 2

def F1(x):
    return 2*x - 3

def main():
    x0 = float(input("Enter the value of x0: "))
    max_iterations = 100  # Maximum number of iterations
    E = 0.001

    iteration = 0
    while iteration < max_iterations:
        if F1(x0) == 0:
            print("Derivative near zero")
            break

        x1 = x0 - F(x0) / F1(x0)
        if abs(F(x1)) < E:
            print(f"Root is {x1}")
            break
        else:
            x0 = x1
            iteration += 1
    else:
        print("Maximum iterations reached.")

if __name__ == "__main__":
    main()