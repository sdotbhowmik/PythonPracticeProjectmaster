# Function definitions
def f(x):
    return x**3 - x - 1

def F(x):
    return x**2 - 4*x - 10

# Main function
def main():
    x1 = float(input("Enter the value of x1: "))
    x2 = float(input("Enter the value of x2: "))
    E = float(input("Enter error tolerance: "))

    f1 = f(x1)
    f2 = f(x2)

    # Check if False Position condition is satisfied
    if f1 * f2 < 0:
        print("\nUsing False Position Method:")
        # False Position method
        while True:
            # Calculate new approximation
            x0 = x1 - (f1 * (x2 - x1)) / (f2 - f1)
            f0 = f(x0)

            # Check convergence
            if abs(f0) < E:
                print(f"Root is {x0:.6f}")
                break

            # Update interval for next iteration
            if f1 * f0 < 0:
                x2 = x0
                f2 = f0
            else:
                x1 = x0
                f1 = f0

    else:
        print("\nUsing Secant Method:")
        # Secant method
        while True:
            f1 = F(x1)
            f2 = F(x2)

            # Calculate new approximation
            x3 = x2 - (f2 * (x2 - x1)) / (f2 - f1)

            # Check convergence
            if abs(x3 - x2) < E:
                print(f"Root is {x3:.6f}")
                break

            # Update values for next iteration
            x1, x2 = x2, x3

if __name__ == "__main__":
    main()