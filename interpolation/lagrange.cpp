#include <iostream>

using std::cout;
using std::cin;
using std::endl;

// function to calculate the Lagrange polynomial
double interpolacao_lagrange(int n, const double x[], const double y[], double valor_x) {
    
    double resultado = 0; // initialize the result

    // loop through each point
    for (int i = 0; i < n; i++) {
        double term = y[i]; // start with the y value of the current point
        // loop through each point again to calculate the term
        for (int j = 0; j < n; j++) {
            if (j != i) { // skip the current point
                term *= (valor_x - x[j]) / (x[i] - x[j]); // calculate the term
            }
        }
        resultado += term; // add the term to the result
    }

    return resultado; // return the result
}

int main() {
    int n; // number of points
    cout << "Enter the number of points: "; // prompt the user for the number of points
    cin >> n; // read the number of points

    double x[n], y[n]; // arrays to store the x and y values
    cout << "Insert points in x y format:" << endl; // prompt the user to enter the points
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i]; // read the x and y values
    }

    double valor_x; // value of x for interpolation
    cout << "Enter the value of x for interpolation: "; // prompt the user for the value of x
    cin >> valor_x; // read the value of x

    double resultado = interpolacao_lagrange(n, x, y, valor_x); // calculate the interpolated value
    cout << "The interpolated value for x = " << valor_x << " : " << resultado << endl;

    return 0;
}