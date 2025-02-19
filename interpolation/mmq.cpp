#include <iostream>
#include <math.h>

using namespace std;

// function to calculate the sum of the product of x and y arrays
double sum_xy(int n, double x[], double y[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += x[i] * y[i];
    }
    return sum;
}

// function to calculate the sum of the x array
double sum_x(int n, double x[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += x[i];
    }
    return sum;
}

// function to calculate the sum of the y array
double sum_y(int n, double y[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += y[i];
    }
    return sum;
}

// function to calculate the sum of the squares of the x array
double sum_square_x(int n, double x[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += pow(x[i], 2);
    }
    return sum;
}

// function to calculate the value of 'a' in the linear equation
double calculate_a(int n, double xy, double x_y, double square_x, double x) {
    double a = (n * xy - x_y) / (n * square_x - pow(x, 2));
    return a;
}

// function to calculate the value of 'b' in the linear equation
double calculate_b(int n, double y, double x) {
    double b = (y - x) / n;
    return b;
}

// function to calculate the exponential value
double exponential(double x, double a, double b) {
    return b * pow(a, x);
}

// Function to calculate the quadratic value
double quadratic(double x, double a, double b) {
    return a * pow(x, 2) + b;
}

int main() {
    return 0;
}