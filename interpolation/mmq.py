import numpy as np
import matplotlib.pyplot as plt

# Function to plot the data points and the least squares line or curve
def plot_mmq(x, y, y_plot, title):
    # Plot the original data points
    plt.scatter(x, y, color='red', label='Data Points')

    # Plot the least squares line or curve
    plt.plot(x, y_plot, label=title)

    # Add title and labels
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to perform linear least squares fitting
def mmq_linear(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x * x)
    sum_xy = np.sum(x * y)
    
    denominator = n * sum_xx - sum_x ** 2
    a = (sum_y * sum_xx - sum_x * sum_xy) / denominator
    b = (n * sum_xy - sum_x * sum_y) / denominator
    
    return a, b

# Function to perform quadratic least squares fitting
def mmq_quadratic(x, y):
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return a, b, c

# Function to perform exponential least squares fitting
def mmq_exponential(x, y):
    y_log = np.log(y)
    b, log_a = mmq_linear(x, y_log)
    a = np.exp(log_a)
    return a, b

# Main function to execute the program
def main():
    # Get the number of points from the user
    n = int(input("Enter the number of points: "))

    x = []
    y = []
    print("Enter the points in the format x y:")
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)

    # Get the type of function to fit from the user
    print("Choose the function type:")
    print("1. Linear (y = a + bx)")
    print("2. Quadratic (y = ax^2 + bx + c)")
    print("3. Exponential (y = a * e^(bx))")
    choice = int(input("Enter your choice (1/2/3): "))

    x = np.array(x)
    y = np.array(y)

    # Perform the fitting based on the user's choice
    if choice == 1:
        a, b = mmq_linear(x, y)
        y_plot = a + b * np.linspace(min(x), max(x), 500)
        plot_mmq(x, y, y_plot, 'Least Squares Line (Linear)')
        print(f"The coefficients are: a = {a}, b = {b}")
    elif choice == 2:
        a, b, c = mmq_quadratic(x, y)
        x_plot = np.linspace(min(x), max(x), 500)
        y_plot = a * x_plot**2 + b * x_plot + c
        plot_mmq(x, y, y_plot, 'Least Squares Curve (Quadratic)')
        print(f"The coefficients are: a = {a}, b = {b}, c = {c}")
    elif choice == 3:
        a, b = mmq_exponential(x, y)
        x_plot = np.linspace(min(x), max(x), 500)
        y_plot = a * np.exp(b * x_plot)
        plot_mmq(x, y, y_plot, 'Least Squares Curve (Exponential)')
        print(f"The coefficients are: a = {a}, b = {b}")
    else:
        print("Invalid choice")

# Entry point of the program
if __name__ == "__main__":
    main()
