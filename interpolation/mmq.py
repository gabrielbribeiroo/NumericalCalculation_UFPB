import numpy as np
import matplotlib.pyplot as plt

def plot_mmq(x, y, a, b):
    # Generate a range of x values for plotting the interpolation
    x_plot = np.linspace(min(x), max(x), 500)
    y_plot = a + b * x_plot

    # Plot the original data points
    plt.scatter(x, y, color='red', label='Data Points')

    # Plot the least squares line
    plt.plot(x_plot, y_plot, label='Least Squares Line')

    # Add title and labels
    plt.title('Least Squares Line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def mmq(x, y):
    # Number of data points
    n = len(x)
    
    # Calculate the sums needed for the coefficients
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x * x)
    sum_xy = np.sum(x * y)
    
    # Calculate the coefficients a and b for the line y = a + bx
    denominator = n * sum_xx - sum_x ** 2
    a = (sum_y * sum_xx - sum_x * sum_xy) / denominator
    b = (n * sum_xy - sum_x * sum_y) / denominator
    
    return a, b

def main():
    n = int(input("Enter the number of points: "))

    x = []
    y = []
    print("Enter the points in the format x y:")
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)

    a, b = mmq(np.array(x), np.array(y))
    print(f"The coefficients are: a = {a}, b = {b}")

    plot_mmq(x, y, a, b)

if __name__ == "__main__":
    main()
