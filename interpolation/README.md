# Interpolation Methods for Optimus Route AI

## Overview

This repository contains various interpolation methods essential for the Optimus Route AI project. The goal of this project is to determine the best route for your routine, optimizing travel time and efficiency.

## Purpose of Interpolation Methods

Interpolation is a method of constructing new data points within the range of a discrete set of known data points. In the context of Optimus Route AI, interpolation methods are used to estimate unknown values that fall between known data points, which is crucial for accurate route planning and optimization.

## Methods Included

1. **Polynomial Interpolation**: This method uses polynomials to estimate values between known data points. It is more flexible than linear interpolation but can be more complex.
2. **Lagrange Interpolation**: This method uses the Lagrange polynomial to estimate values. It is useful for small datasets and provides an exact fit through the known data points.
3. **Newton Interpolation**: This method uses Newton's divided differences to estimate values. It is useful for both small and large datasets and provides a polynomial that fits through the known data points.
4. **Least Squares Method**: This method minimizes the sum of the squares of the differences between the observed and estimated values. It is useful for fitting a model to data with noise or errors.

## How to Use

Each interpolation method is implemented in a separate file within this directory. You can use these methods by importing the corresponding file into your project and calling the appropriate functions with your data.

## Google Colab and Slides

You can find the Google Colab notebook and the project slides at the following links:
- [Google Colab Notebook](https://colab.research.google.com/drive/1I65Qa26y-hYd8j3Ws_AOvMtXXrduCtD1?usp=sharing)
- [Project Slides](https://www.canva.com/design/DAGfaZmZv6Y/KKu9mUMibHx_4HicDF9Y7w/edit)

## Contribution

You should know that contributions to improve the interpolation methods or add new ones are welcome. Please follow the standard guidelines for contributing to this repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or issues, don't hesitate to get in touch with the project maintainer.
