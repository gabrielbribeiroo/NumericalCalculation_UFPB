import numpy as np
import matplotlib.pyplot as plt

def plot_newton_interpolation(x, y, matrix, x_value, interpolated_y):
    # Generate a range of x values for plotting the interpolation
    x_plot = np.linspace(min(min(x), x_value) - 1, max(max(x), x_value) + 1, 5000)  # Increase resolution to 5000 points
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
    x_margin = (max(x + [x_value]) - min(x + [x_value])) * 0.05  # 5% margin
    y_margin = (max(y + [interpolated_y]) - min(y + [interpolated_y])) * 0.05  # 5% margin
    plt.xlim(min(x + [x_value]) - x_margin, max(x + [x_value]) + x_margin)
    plt.ylim(min(y + [interpolated_y]) - y_margin, max(y + [interpolated_y]) + y_margin)

    plt.show()
