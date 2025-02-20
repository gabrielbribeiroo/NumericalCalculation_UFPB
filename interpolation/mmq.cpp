#include <iostream>
#include <math.h>

using namespace std;

// Function to calculate the sum of the product of arrays x and y
double sum_xy(int n, double x[], double y[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += x[i] * y[i];
    }
    return sum;
}

// Function to calculate the sum of array x
double sum_x(int n, double x[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += x[i];
    }
    return sum;
}

// Function to calculate the sum of array y
double sum_y(int n, double y[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += y[i];
    }
    return sum;
}

// Function to calculate the sum of the squares of array x
double sum_square_x(int n, double x[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += pow(x[i], 2);
    }
    return sum;
}

// Function to calculate the value of 'a' in the linear equation
double calculate_a(int n, double xy, double x_y, double square_x, double x) {
    double a = (n * xy - x_y) / (n * square_x - pow(x, 2));
    return a;
}

// Function to calculate the value of 'b' in the linear equation
double calculate_b(int n, double y, double x) {
    double b = (y - x) / n;
    return b;
}

// Function to calculate the exponential value
double exponential(double x, double a, double b) {
    return b * pow(a, x);
}
double quadratic(double x, double a, double b) {
    return a * pow(x, 2) + b;
}

int main() {
    return 0;
}