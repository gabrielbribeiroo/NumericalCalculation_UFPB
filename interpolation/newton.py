import numpy as np
import matplotlib.pyplot as plt

# Function to plot the Newton interpolation polynomial
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
    x_margin = (max(x + [x_value]) - min(x + [x_value])) * 0.1  
    y_margin = (max(y + [interpolated_y]) - min(y + [interpolated_y])) * 0.1 
    plt.xlim(min(x + [x_value]) - x_margin, max(x + [x_value]) + x_margin)
    plt.ylim(min(y + [interpolated_y]) - y_margin, max(y + [interpolated_y]) + y_margin)

    # Show the plot
    plt.show()
    
# Function to calculate the divided differences table
def divided_differences(n, x, y):
    # Initialize a matrix with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize the first column with y values
    for i in range(n):
        matrix[i][0] = y[i]

    # Calculate orders from 1 to n
    for j in range(1, n):
        for i in range(n - j):
            # Calculate the divided difference using the formula
            matrix[i][j] = (matrix[i + 1][j - 1] - matrix[i][j - 1]) / (x[i + j] - x[i])

    return matrix

# Function to perform Newton interpolation
def newton_interpolation(n, x, interpolate_value, matrix):
    result = matrix[0][0]
    term = 1

    # Calculate the interpolation result using the Newton polynomial
    for i in range(1, n):
        term *= (interpolate_value - x[i - 1])
        result += (term * matrix[0][i])

    return result

# Main function to execute the program
def main():
    # Input the number of points
    n = int(input("Enter the number of points: "))

    x = []
    y = []
    print("Enter the points in the format x y:")
    # Input the points
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)

    # Input the value of x for interpolation
    x_value = float(input("Enter the value of x for interpolation: "))

    # Calculate the divided differences table
    matrix = divided_differences(n, x, y)
    # Perform Newton interpolation
    result = newton_interpolation(n, x, x_value, matrix)
    print(f"The interpolated value for x = {x_value} : {result}")

    # Plot the Newton interpolation polynomial
    plot_newton_interpolation(x, y, matrix, x_value, result)

# Execute the main function
if __name__ == "__main__":
    main()
