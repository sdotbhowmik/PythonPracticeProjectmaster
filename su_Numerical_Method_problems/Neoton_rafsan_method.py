def F(x):
    return x**2 - 3*x + 2

def F1(x):
    return 2*x - 3

def main():
    x0 = float(input("Enter the value of x0: "))
    max_iterations = 100  # Maximum number of iterations
    tolerance = 1e-5  # Convergence criteria

    iteration = 0
    while iteration < max_iterations:
        if F1(x0) == 0:
            print("Derivative near zero; stopping...")
            break

        x1 = x0 - F(x0) / F1(x0)
        if abs(F(x1)) < tolerance:
            print(f"Root is {x1}")
            break
        else:
            x0 = x1
            iteration += 1
    else:
        print("Maximum iterations reached; result may not be accurate.")

if __name__ == "__main__":
    main()