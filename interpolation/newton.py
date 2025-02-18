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

if __name__ == "__main__":
    main()
