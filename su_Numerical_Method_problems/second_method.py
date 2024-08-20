def F(x):
    return x**2 - 4*x - 10

def main():
    x1 = float(input("Enter the value of x1: "))
    x2 = float(input("Enter the value of x2: "))
    tolerance = 0.001  # Convergence criteria


    while True:
        f1 = F(x1)
        f2 = F(x2)

        x3 = x2 - (f2 * (x2 - x1)) / (f2 - f1)
        if abs(x3 - x2) < tolerance:
            break

        x1, x2 = x2, x3

    print(f"Root is {x3:.6f}")

if __name__ == "__main__":
    main()