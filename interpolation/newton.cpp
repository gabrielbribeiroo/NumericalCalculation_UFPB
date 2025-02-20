#include <iostream>
#include <vector>

using namespace std;

// Function to calculate divided differences
vector<vector<double>> divided_differences(int n, double x[], double y[]) {
    // Create a matrix to store divided differences
    vector<vector<double>> matrix(n, vector<double>(n)); 

    // Initialize the first column with y values
    for (int i = 0; i < n; i++) {
        matrix[i][0] = y[i];
    }

    /*  
    Matrix logic
        index       0       1        2
                    order 1 order 2 order 3
        0              4        -3     2/3
        1              1        -1     
        2             -1
    */

    // Calculate orders from 1 to n
    for (int j = 1; j < n; j++) {
        for (int i = 0; i < n - j; i++) {
            // Calculate the divided difference using the formula
            matrix[i][j] = (matrix[i+1][j-1] - matrix[i][j-1]) / (x[i+j] - x[i]);
        }
    }
    return matrix;
}

// Function to perform Newton interpolation
double newton_interpolation(int n, double x[], double interpolate_value, vector<vector<double>> matrix) {
    double result = matrix[0][0]; // Initialize result with the first y value
    double term = 1; // Initialize term for multiplication
    
    // Calculate the interpolation result
    for (int i = 1; i < n; i++) {
        term *= (interpolate_value - x[i-1]); // Update term with the difference
        result += (term * matrix[0][i]); // Add the term multiplied by the divided difference
    }
    return result;
}

int main() {
    int n;
    cout << "Enter the number of points: ";
    cin >> n; // Input the number of points

    double x[n], y[n];
    cout << "Enter the points in the format x y:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i]; // Input the x and y values
    }

    double x_value;
    cout << "Enter the value of x for interpolation: ";
    cin >> x_value; // Input the x value for interpolation

    // Calculate the divided differences matrix
    vector<vector<double>> matrix = divided_differences(n, x, y);
    // Perform Newton interpolation
    double result = newton_interpolation(n, x, x_value, matrix);
    // Output the interpolated value
    cout << "The interpolated value for x = " << x_value << " : " << result << endl;

    return 0;
}