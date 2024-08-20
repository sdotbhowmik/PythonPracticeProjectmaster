# Define the tolerance level
E = 0.001


# Define functions for updating the values of x, y, and z
def X(y, z):
    return (12 - 2 * y - z) / 5


def Y(x, z):
    return (15 - x - 2 * z) / 4


def Z(x, y):
    return (20 - x - 2 * y) / 5


# Main function
def main():
    # Input initial guesses
    x1 = float(input("Enter the initial guess for X: "))
    y1 = float(input("Enter the initial guess for Y: "))
    z1 = float(input("Enter the initial guess for Z: "))

    iteration = 0
    while True:
        # Calculate the next values using the latest updated values

        # *** Gauss-Seidel Update ***
        x2 = X(y1, z1)  # Use previous y1 and z1

        y2 = Y(x2, z1)  # Use the UPDATED x2 and previous z1

        z2 = Z(x2, y2)  # Use the UPDATED x2 and y2

        # Check for convergence
        if (abs(x2 - x1) < E and abs(y2 - y1) < E and abs(z2 - z1) < E):
            print(f"\nConverged after {iteration + 1} iterations:")
            print(f"X is : {x2:.6f}")
            print(f"Y is : {y2:.6f}")
            print(f"Z is : {z2:.6f}")
            break
        else:
            # Update values for the next iteration
            x1, y1, z1 = x2, y2, z2

        iteration += 1


# Run the main function
if __name__ == "__main__":
    main()