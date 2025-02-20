import numpy as np
import matplotlib.pyplot as plt

def plot_newton_interpolation(x, y, matrix, x_value, interpolated_y):
    # Generate a range of x values for plotting the interpolation
    x_plot = np.linspace(min(x) - 1, max(x) + 1, 1000)  # Increased resolution and added padding
    y_plot = [newton_interpolation(len(x), x, xi, matrix) for xi in x_plot]

    # Plot the original data points
    plt.scatter(x, y, color='red', label='Data Points')

    # Plot the Newton interpolation polynomial
    plt.plot(x_plot, y_plot, label='Newton Interpolation Polynomial')

    # Plot the interpolated point
    plt.scatter(x_value, interpolated_y, color='blue', label='Interpolated Point')

    # Add title and labels
    plt.title('Newton Interpolation Polynomial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Adjust the axis limits for better visualization
    x_margin = (max(x) - min(x)) * 0.1  # 10% margin
    y_margin = (max(y) - min(y)) * 0.1  # 10% margin
    plt.xlim(min(x) - x_margin, max(x) + x_margin)
    plt.ylim(min(y) - y_margin, max(y) + y_margin)

    plt.show()
    
def divided_differences(n, x, y):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # initialize the first column with y values
    for i in range(n):
        matrix[i][0] = y[i]

    # calculate orders from 1 to n
    for j in range(1, n):
        for i in range(n - j):
            # calculate the divided difference using the formula
            matrix[i][j] = (matrix[i + 1][j - 1] - matrix[i][j - 1]) / (x[i + j] - x[i])

    return matrix

def newton_interpolation(n, x, interpolate_value, matrix):
    result = matrix[0][0]
    term = 1

    for i in range(1, n):
        term *= (interpolate_value - x[i - 1])
        result += (term * matrix[0][i])

    return result

def main():
    n = int(input("Enter the number of points: "))

    x = []
    y = []
    print("Enter the points in the format x y:")
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)

    x_value = float(input("Enter the value of x for interpolation: "))

    matrix = divided_differences(n, x, y)
    result = newton_interpolation(n, x, x_value, matrix)
    print(f"The interpolated value for x = {x_value} : {result}")

    plot_newton_interpolation(x, y, matrix, x_value, result)

if __name__ == "__main__":
    main()
