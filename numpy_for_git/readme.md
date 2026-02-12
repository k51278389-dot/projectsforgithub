# NumPy Practice Projects

This repository contains small, focused Python programs built using **NumPy** to demonstrate
core array operations, vectorization, and numerical computation techniques.

The goal of this repo is to showcase **clean NumPy usage without loops**, emphasizing
broadcasting, masking, and statistical operations.

---

## Projects Included

### 1. Pairwise Euclidean Distance Matrix
- Computes the full **N × N pairwise distance matrix** for points in D dimensions
- Uses NumPy broadcasting (`np.newaxis`)
- Avoids explicit Python loops
- Demonstrates vectorized numerical computation

**Key concepts:**
- Broadcasting
- `np.linalg.norm`
- Multidimensional array manipulation

---

### 2. Outlier Detection and Replacement
- Detects outliers using **mean + standard deviation**
- Uses boolean masking to identify and replace outliers
- Performs in-place array modification

**Key concepts:**
- Boolean masks
- Statistical thresholds
- Array indexing and assignment

---

### 3. SYMSOLVER – Numerical Methods Toolkit (Advanced)
A command-line tool implementing numerical differentiation, integration,
and ODE solvers using **NumPy and SymPy**.

Includes:
- Finite difference methods (forward, backward, central, higher-order)
- Numerical integration (Riemann sums, Trapezoidal, Simpson’s rules)
- ODE solvers (Euler, Heun, RK2, RK4, RK45)
- Systems of ODEs (explicit & implicit methods)

**Key concepts:**
- Numerical approximation
- Vectorized computation with NumPy
- Symbolic-to-numeric conversion using SymPy
- Modular CLI design

---


## How to Run

Each file is independent and can be run directly:

```bash
python pairwise_distance.py
python outlier_handling.py
python symsolver.py