import numpy as np
import matplotlib.pyplot as plt

# Plot the given points and the interpolation polynomial
def plot_interpolation(x, y, value_x, result):
    plt.scatter(x, y, color='red', label='Given Points')  # Plot the given points
    plt.plot(value_x, result, 'bo', label=f'Interpolated Point ({value_x}, {result:.6f})')  # Plot the interpolated point

    # Generate a range of x values for plotting the interpolation polynomial with a margin
    margin = 0.1 * (max(x) - min(x))  # Define a margin as 10% of the range of x
    x_range = np.linspace(min(x) - margin, max(x) + margin, 500)
    y_range = [interpolation_lagrange(len(x), x, y, xi) for xi in x_range]

    plt.plot(x_range, y_range, label='Lagrange Polynomial')  # Plot the interpolation polynomial
    plt.xlabel('x')  # Label for x-axis
    plt.ylabel('y')  # Label for y-axis
    plt.legend()  # Show legend
    plt.title('Lagrange Interpolation')  # Title of the plot
    plt.grid(True)  # Show grid
    plt.show()  # Display the plot

# Function to calculate the Lagrange polynomial
def interpolation_lagrange(n, x, y, value_x):
    result = 0.0  # Initialize the result as 0.0

    for i in range(n):
        term = y[i]  # Initialize the term as the value y[i]
        for j in range(n):
            if j != i:
                # Calculate the term by multiplying by the Lagrange factor
                term *= (value_x - x[j]) / (x[i] - x[j])
        result += term  # Add the term to the result
        
    return result  # Return the final result

def main():
    n = int(input('Enter the number of points: '))  # Read the number of points

    print('Insert points in x y format: ')
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(float, input().split())  # Read the x and y points
        x.append(x_i)  # Add x_i to the x list
        y.append(y_i)  # Add y_i to the y list

    value_x = float(input('Enter the value of x for interpolation: '))  # Read the value of x for interpolation

    result  = interpolation_lagrange(n, x, y, value_x)  # Calculate the interpolated value
    # Print the interpolated value for the given x
    print(f'The interpolated value for x = {value_x} is: {result:.6f}')
    
    # Call the plot function after calculating the result
    plot_interpolation(x, y, value_x, result)

if __name__ == '__main__':
    main()  # Call the main function