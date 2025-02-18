# Função para calcular o polinômio de Lagrange
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

if __name__ == '__main__':
    main()  # Call the main function