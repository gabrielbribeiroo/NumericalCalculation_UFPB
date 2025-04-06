# 🏃‍♂️ Player Distance Simulation During a Soccer Match

This project simulates a soccer player's speed variation throughout a 90-minute match and calculates the total distance covered using different numerical integration methods: **Trapezoidal Rule**, **Simpson's 1/3 Rule**, and **Simpson's 3/8 Rule**.

## 📊 Objective

Evaluate which numerical integration method provides the best approximation of the total distance based on simulated speed data, by comparing relative error and execution time.

## 🧪 Technologies and Libraries

- Python 3.x
- NumPy
- Matplotlib
- Pandas
- SciPy (optional, for validation)

## 🧠 Methodology

1. **Speed Data Simulation**:
   - Match duration: 90 minutes, with measurements every 10 seconds.
   - Speed values are randomly generated based on activity states (standing, walking, running, sprinting) and realistic probability distributions.

2. **Distance Calculation**:
   - **Exact distance (reference)**: discrete sum \( d = \sum v_i \cdot \Delta t \)
   - **Trapezoidal Rule**
   - **Simpson’s 1/3 Rule**
   - **Simpson’s 3/8 Rule**

3. **Comparison**:
   - Absolute and relative error compared to the discrete sum
   - Execution time
   - Graphical visualization of the area under the speed curve

## 📈 Example Results

| Method         | Distance (m) | Execution Time (s)  | Relative Error (%)  |
|----------------|--------------|---------------------|---------------------|
| Trapezoidal    | 11,581.23    | 0.000173            | 0.1976              |
| Simpson 1/3    | 11,662.63    | 0.000195            | 0.5040              |
| Simpson 3/8    | 11,471.68    | 0.000180            | 1.1416              |

✅ The **trapezoidal rule** yielded the **lowest relative error**, proving to be the most suitable for the highly variable and noisy dataset.

## 📌 Conclusion

The trapezoidal method was the most accurate in this context due to the non-smooth, irregular nature of the speed data. Its linear approximation avoids overfitting, which can occur with higher-order methods like Simpson’s.

## 📬 Contact

If you have any questions, issues, or suggestions, feel free to open an issue or reach out!