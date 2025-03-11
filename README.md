# quadratic-equation-solver 

## Description  
**Quadratic Equation Solver** is a command-line application that solves quadratic equations of the form:  


### **ax^2 + bx + c = 0**


where a, b, and c are real numbers, and a != 0.  
The program supports two modes:  
- **interactive mode** – users input coefficients manually.  
- **non-interactive (file) mode** – coefficients are read from a file.  

---

## Installation and Usage  

To run this application, you need [Python](https://www.python.org) installed on your system.

### Clone the repository 
```
git clone https://github.com/your_username/quadratic-equation-solver.git
```
```
cd quadratic-equation-solver
```

### Run in interactive mode
Simply execute the script without arguments:
```
python3 equation.py
```

### Run in non-interactive (file) mode
Create a file containing three space-separated numbers and pass it as an argument:
```
python3 equation.py path/to/input_file.txt
```

### File format for non-interactive (file) mode
The input file must contain three numbers (coefficients a, b, and c) separated by a space, followed by a newline (\n):
```
5 3 -26
```

## Revert commit
[revert commit](https://github.com/ErmishinS/quadratic-equation-solver/commit/a4b8c605d72e175bb370b0f65b34752df51bc8f1)

