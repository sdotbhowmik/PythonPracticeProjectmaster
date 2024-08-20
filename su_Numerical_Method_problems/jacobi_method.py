# Define constants
E = 0.001
def X(y, z):
    return (12 - 2 * y - z) / 5

def Y(x, z):
    return (15 - x - 2 * z) / 4

def Z(x, y):
    return (20 - x - 2 * y) / 5

# Main function
def main():
    # Input values
    x1 = float(input("Enter the value of X1: "))
    y1 = float(input("Enter the value of Y1: "))
    z1 = float(input("Enter the value of Z1: "))

    while True:
        # Calculate the next values
        x2 = X(y1, z1)
        y2 = Y(x1, z1)
        z2 = Z(x1, y1)

        # Check for convergence
        if (abs(x2 - x1) < E and abs (y2 - y1) < E and abs (z2 - z1) < E):
            print(f"X is : {x2:.6f}")
            print(f"Y is : {y2:.6f}")
            print(f"Z is : {z2:.6f}")
            break
        else:
            # Update values for the next iteration
            x1 = x2
            y1 = y2
            z1 = z2

# Run the main function
if __name__ == "__main__":
    main()