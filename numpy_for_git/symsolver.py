import numpy as np
import sympy as sp
   
def menu_1():
    handlers = {
        "1": fd_cli,
        "2": gd_cli,
        "3": cd_cli,
        "4": high_ord_cli,
        "5": five_pointer_cli,
        "6": left_reimann_cli,
        "7": right_reimann_cli,
        "8": trapezoidal_cli,
        "9": midpoint_cli,
        "10": simpson_cli,
        "11": simpson_38_cli,
        "Q": None
    }

    while True:
        print("="*60)
        print('WELCOME TO NUMERICAL DIFFERENTIATION & INTEGRATION'.center(60))
        print("="*60)
        print("1. Solve Forward Difference Derivative")
        print("2. Solve Backward Difference Derivative")
        print("3. Solve Central Difference Derivative")
        print("4. Solve Higher-Order Derivative using Finite Difference")
        print("5. Solve Five-Point Stencil Derivative")
        print("6. Solve Left Riemann Sum Integration")
        print("7. Solve Right Riemann Sum Integration")
        print("8. Solve Trapezoidal Rule Integration")
        print("9. Solve Midpoint Rule Integration")
        print("10. Solve Simpson's Rule Integration")
        print("11. Solve Simpson's 3/8 Rule Integration")
        print("Q. Return to Main Menu")
        print("-"*60)

        choice = input("Choose an option: ").strip()

        # Quit
        if choice.upper() == "Q":
            print("\nReturning to Main Menu...\n")
            break

        handler = handlers.get(choice)

        if handler is None:
            print("❌ Invalid choice — try again.")
            continue

        try:
            handler()   
            
        except Exception as e:
            print("❌ Error occurred:", str(e))
            
def menu_2():
    handlers = {
        "1": euler_cli,
        "2": Heun_cli,
        "3": Midpoint_cli,
        "4": RK2_cli,
        "5": RK4_cli,
        "6": rk45_cli,               
        "Q": None
    }

    while True:
        print("="*60)
        print('WELCOME TO ODE SOLVERS'.center(60))
        print("="*60)
        print("1. Solve Euler's Method for ODEs")
        print("2. Solve Heun's Method for ODEs")
        print("3. Solve Midpoint Method for ODEs")
        print("4. Solve RK2 Method for ODEs")
        print("5. Solve RK4 Method for ODEs")
        print("6. Solve RK45 Method for ODEs")
        print("Q. Return to Main Menu")
    
        print("-"*60)

        choice = input("Choose an option: ").strip()

        # Quit
        if choice.upper() == "Q":
            print("\nReturning to Main Menu...\n")
            break

        handler = handlers.get(choice)

        if handler is None:
            print("❌ Invalid choice — try again.")
            continue

        try:
            handler()   
            
        except Exception as e:
            print("❌ Error occurred:", str(e))
            
            
def menu_3():
    handlers = {
        "1": backward_euler_system_cli,
        "2": explicit_euler_system_cli,
        "3": trapezoidal_system_cli,
        "4": rk4_system_cli,               
        "Q": None
    }

    while True:
        print("="*60)
        print('WELCOME TO ODE SYSTEMS'.center(60))
        print("="*60)
        print("1. Solve Backward Euler Method for ODE Systems")
        print("2. Solve Explicit Euler Method for ODE Systems")
        print("3. Solve Trapezoidal Method for ODE Systems")
        print("4. Solve RK4 Method for ODE Systems")
        print("Q. Return to Main Menu")
    
        print("-"*60)

        choice = input("Choose an option: ").strip()

        # Quit
        if choice.upper() == "Q":
            print("\nReturning to Main Menu...\n")
            break

        handler = handlers.get(choice)

        if handler is None:
            print("❌ Invalid choice — try again.")
            continue

        try:
            handler()   
            
        except Exception as e:
            print("❌ Error occurred:", str(e))
            
            
            
            
            
def menu():
    handlers = {
        "1": menu_1,
        "2": menu_2,
        "3": menu_3,               
        "Q": None
    }

    while True:
        print("="*60)
        print('WELCOME TO SYMSOLVER'.center(60))
        print("="*60)
        print("1. Numerical Differentiation & Integration")
        print("2. ODE Solver")
        print("3. ODE Systems")
        print("Q. Exit")

        print("-"*60)

        choice = input("Choose an option: ").strip()

        # Quit
        if choice.upper() == "Q":
            print("\nThank you for using SYMSOLVER!\n")
            break

        handler = handlers.get(choice)

        if handler is None:
            print("❌ Invalid choice — try again.")
            continue

        try:
            handler()   
            
        except Exception as e:
            print("❌ Error occurred:", str(e)),                              
                                             
   


def user_input_const(user_input):
    try:
        f_expr = sp.sympify(user_input)

        symbols = sorted(list(f_expr.free_symbols), key=lambda s: s.name)

        f = sp.lambdify(symbols, f_expr, "numpy")

        return f_expr, symbols, f

    except Exception as e:
        # ANY error that happens above will land here
        print("Error:", e)
        
        print("Invalid expression. Please try again.")
        return None, None, None
    
    
def user_input_ode():
    while True:
        user_input = input("Enter dy/dx = f(x, y): ").strip()

        if not user_input:
            print("You must enter an expression.")
            continue

        try:
            f_expr = sp.sympify(user_input)
            symbols = sorted(list(f_expr.free_symbols), key=lambda s: s.name)

            if len(symbols) != 2:
                print(
                    f"ODE must contain EXACTLY 2 variables.\n"
                    f"Detected: {symbols}\n"
                    "Example: sin(x) + y**2"
                )
                continue

            indep_sym = symbols[0]
            dep_sym   = symbols[1]

            print(f"Detected variables: {symbols}")
            print(f"Interpreting as d({dep_sym})/d({indep_sym})")

            x, y = sp.symbols("x y")
            f_expr_internal = f_expr.subs({indep_sym: x, dep_sym: y})
            f = sp.lambdify((x, y), f_expr_internal, "numpy")

            return f_expr_internal, f, (indep_sym, dep_sym)

        except Exception as e:
            print("Invalid expression:", e)
            print("Try again.\n")



def user_input_ode_system():
    while True:
        try:
            m = int(input("Enter number of equations: "))
            if m <= 0:
                print("Must be positive.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    x = sp.Symbol("x")
    y_syms = sp.symbols(f"y1:{m+1}")
    allowed = {x, *y_syms}

    print("\nAllowed variables:")
    print("x,", ", ".join(str(y) for y in y_syms))

    exprs = []

    for i in range(m):
        while True:
            raw = input(
                f"Enter dy{i+1}/dx = f{i+1}(x, y1..y{m}): "
            ).strip()

            try:
                expr = sp.sympify(raw)
            except Exception:
                print("Invalid expression syntax. Try again.")
                continue

            used = expr.free_symbols
            illegal = used - allowed

            if illegal:
                print(
                    f"ERROR: Illegal variable(s): {sorted(illegal)}\n"
                    f"Allowed: x, {', '.join(str(y) for y in y_syms)}"
                )
                continue   

            exprs.append(expr)
            break   # next equation

    f = sp.lambdify((x, y_syms), exprs, "numpy")
    return f, y_syms, x


    
    

def fd_core(f, x, h):
    
    try:
        return (f(x+h) - f(x)) / h
    except Exception as e:
        print("Error computing forward difference:", e)
        return None

def fd_cli():
    print("\n=== Forward Difference Derivative Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  # remove leading/trailing spaces
        if not raw:  # empty input
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        x_input = input(f"Enter the value of {var} at which to compute f'({var}): ").strip()
        if not x_input:
            print("You must enter a numeric value.")
            continue
        try:
            x0 = float(x_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
            
            
    while True:
        h_input = input("Enter step size h (default 1e-5): ").strip()
        if not h_input:
            print('you must enter a numeric number')
            continue
        try:
            h0=float(h_input)
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    df=fd_core(f,x0,h0) 
    if df is None:
        print("Derivative could not be computed.")
        return
    
    print("\n--- Results ---")
    print(f"Function:      {f_expr}")
    print(f"Variable:      {var}")
    print(f"Point x =      {x0}")
    print(f"Step size h =  {h0}")
    print(f"Forward diff:  f'({x0}) ≈ {df}\n")    
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")    



def gd_core(f, x, h):
    
    try:
        return (f(x) - f(x - h)) / h
    except Exception as e:
        print("Error computing forward difference:", e)
        return None

def gd_cli():
    print("\n=== Backward Difference Derivative Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  # remove leading/trailing spaces
        if not raw:  # empty input
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        x_input = input(f"Enter the value of {var} at which to compute f'({var}): ").strip()
        if not x_input:
            print("You must enter a numeric value.")
            continue
        try:
            x0 = float(x_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
            
            
    while True:
        h_input = input("Enter step size h (default 1e-5): ").strip()
        if not h_input:
            print('you must enter a numeric number')
            continue
        try:
            h0=float(h_input)
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    dg=gd_core(f,x0,h0) 
    if dg is None:
        print("Derivative could not be computed.")
        return
    
    print("\n--- Results ---")
    print(f"Function:      {f_expr}")
    print(f"Variable:      {var}")
    print(f"Point x =      {x0}")
    print(f"Step size h =  {h0}")
    print(f"Forward diff:  f'({x0}) ≈ {dg}\n")
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")                    
            
            
            
def cd_core(f, x, h):
    
    try:
        return (f(x+h) - f(x - h)) / (2*h)
    except Exception as e:
        print("Error computing forward difference:", e)
        return None

def cd_cli():
    print("\n=== Central Difference Derivative Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  
        if not raw:  
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        x_input = input(f"Enter the value of {var} at which to compute f'({var}): ").strip()
        if not x_input:
            print("You must enter a numeric value.")
            continue
        try:
            x0 = float(x_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
            
            
    while True:
        h_input = input("Enter step size h (default 1e-5): ").strip()
        if not h_input:
            print('you must enter a numeric number')
            continue
        try:
            h0=float(h_input)
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    dc= cd_core(f,x0,h0) 
    if dc is None:
        print("Derivative could not be computed.")
        return
    
    print("\n--- Results ---")
    print(f"Function:      {f_expr}")
    print(f"Variable:      {var}")
    print(f"Point x =      {x0}")
    print(f"Step size h =  {h0}")
    print(f"Forward diff:  f'({x0}) ≈ {dc}\n") 
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")                   
            
 
 
def high_ord_core(f, x, h):
    
    try:
        return (f(x+h) - 2*f(x) + f(x - h)) / (h**2)
    except Exception as e:
        print("Error computing forward difference:", e)
        return None

def high_ord_cli():
    print("\n=== Central Difference Derivative Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  
        if not raw:  
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        x_input = input(f"Enter the value of {var} at which to compute f'({var}): ").strip()
        if not x_input:
            print("You must enter a numeric value.")
            continue
        try:
            x0 = float(x_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
            
            
    while True:
        h_input = input("Enter step size h (default 1e-5): ").strip()
        if not h_input:
            print('you must enter a numeric number')
            continue
        try:
            h0=float(h_input)
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    ho= high_ord_core(f,x0,h0) 
    if ho is None:
        print("Derivative could not be computed.")
        return
    
    print("\n--- Results ---")
    print(f"Function:      {f_expr}")
    print(f"Variable:      {var}")
    print(f"Point x =      {x0}")
    print(f"Step size h =  {h0}")
    print(f"Forward diff:  f'({x0}) ≈ {ho}\n") 
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")                
            
            
            
def five_pointer_core(f, x, h):
    
    try:
        return ( - f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)
    except Exception as e:
        print("Error computing forward difference:", e)
        return None

def five_pointer_cli():
    print("\n=== Central Difference Derivative Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  
        if not raw:  
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        x_input = input(f"Enter the value of {var} at which to compute f'({var}): ").strip()
        if not x_input:
            print("You must enter a numeric value.")
            continue
        try:
            x0 = float(x_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
            
            
    while True:
        h_input = input("Enter step size h (default 1e-5): ").strip()
        if not h_input:
            print('you must enter a numeric number')
            continue
        try:
            h0=float(h_input)
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    fp= five_pointer_core(f,x0,h0) 
    if fp is None:
        print("Derivative could not be computed.")
        return
    
    print("\n--- Results ---")
    print(f"Function:                 {f_expr}")
    print(f"Variable:                 {var}")
    print(f"Point x =                 {x0}")
    print(f"Step size h =             {h0}")
    print(f"Forward diff:  f'({x0}) ≈ {fp}\n")    
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")    
                            
            
    
def left_riemann_core(f, a, b, n):
    try:
        h = (b - a) / n
        x = a + np.arange(0, n) * h
        return h * np.sum(f(x))
    except Exception as e:
        print("Error computing Left Riemann sum:", e)
        return None


def left_reimann_cli():
    print("\n=== Left Reimann Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  
        if not raw:  
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        a_input = input(f"Enter the value of lower limit for f{var}): ").strip()
        if not a_input:
            print("You must enter a numeric value.")
            continue
        try:
            a0 = float(a_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
    while True:
        b_input = input(f"Enter the value of upper limit for f{var}): ").strip()
        if not b_input:
            print("You must enter a numeric value.")
            continue
        try:
            b0 = float(b_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")        
            
    while True:
        n_input = input("Enter the number of intervals (n) : ").strip()
        if not n_input:
            print('you must enter a numeric number')
            continue
        try:
            n0=int(n_input)
            if n0 <= 0:
                print("Number of intervals must be positive.")
                continue
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    try:
        if a0 > b0:
            a0, b0 = b0, a0

            
        lr = left_riemann_core(f, a0, b0, n0)

        if lr is None:
            print("Integration could not be computed.")
            return

    except Exception as e:
        print("Error during integration:", e)
        return        
    
    print("\n--- Results ---")
    print(f"Function:              {f_expr}")
    print(f"Variable:              {var}")
    print(f"Upper Limit =          {a0}")
    print(f"Lower Limit =          {b0}")
    print(f"No. of Intervals:      {n0}")
    print(f"Left Riemann Integral: {lr}")    
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")               
            
            
    
    
def right_riemann_core(f, a, b, n):
    try:
        h = (b - a) / n
        x = a + np.arange(1, n+1)*h  
        return h * np.sum(f(x))
    except Exception as e:
        print("Error computing Left Riemann sum:", e)
        return None


def right_reimann_cli():
    print("\n=== Right Reimann Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  
        if not raw:  
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        a_input = input(f"Enter the value of lower limit for f{var}): ").strip()
        if not a_input:
            print("You must enter a numeric value.")
            continue
        try:
            a0 = float(a_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
    while True:
        b_input = input(f"Enter the value of upper limit for f{var}): ").strip()
        if not b_input:
            print("You must enter a numeric value.")
            continue
        try:
            b0 = float(b_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")        
            
    while True:
        n_input = input("Enter the number of intervals (n) : ").strip()
        if not n_input:
            print('you must enter a numeric number')
            continue
        try:
            n0=int(n_input)
            if n0 <= 0:
                print("Number of intervals must be positive.")
                continue
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    try:
        if a0 > b0:
            a0, b0 = b0, a0

            
        rr = right_riemann_core(f, a0, b0, n0)

        if rr is None:
            print("Integration could not be computed.")
            return

    except Exception as e:
        print("Error during integration:", e)
        return        
            

    print("\n--- Results ---")
    print(f"Function:               {f_expr}")
    print(f"Variable:               {var}")
    print(f"Upper Limit =           {a0}")
    print(f"Lower Limit =           {b0}")
    print(f"No. of Intervals:       {n0}")
    print(f"Right Riemann Integral: {rr}")  
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")     
    
    
 
def trapezoidal_core(f, a, b, n):
    try:
        h = (b - a) / n
        x = a + np.arange(1, n) * h  # interior points
        return h * (0.5*f(a) + np.sum(f(x)) + 0.5*f(b))
    except Exception as e:
        print("Error computing trapezoidal integral:", e)
        return None


def trapezoidal_cli():
    print("\n=== Trapezoidal Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  
        if not raw:  
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        a_input = input(f"Enter the value of lower limit for f{var}): ").strip()
        if not a_input:
            print("You must enter a numeric value.")
            continue
        try:
            a0 = float(a_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
    while True:
        b_input = input(f"Enter the value of upper limit for f{var}): ").strip()
        if not b_input:
            print("You must enter a numeric value.")
            continue
        try:
            b0 = float(b_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")        
            
    while True:
        n_input = input("Enter the number of intervals (n) : ").strip()
        if not n_input:
            print('you must enter a numeric number')
            continue
        try:
            n0=int(n_input)
            if n0 <= 0:
                print("Number of intervals must be positive.")
                continue
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    try:
        if a0 > b0:
            a0, b0 = b0, a0

            
        tp = trapezoidal_core(f, a0, b0, n0)

        if tp is None:
            print("Integration could not be computed.")
            return

    except Exception as e:
        print("Error during integration:", e)
        return        
            

    print("\n--- Results ---")
    print(f"Function:               {f_expr}")
    print(f"Variable:               {var}")
    print(f"Upper Limit =           {a0}")
    print(f"Lower Limit =           {b0}")
    print(f"No. of Intervals:       {n0}")
    print(f"Trapezoidal Integral:   {tp}")   
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")    
                
                
 
def midpoint_core(f, a, b, n):
    try:
        h = (b - a) / n
        midpoints = a + (np.arange(0, n) + 0.5) * h
        return h * np.sum(f(midpoints))
    except Exception as e:
        print("Error computing midpoint rule:", e)
        return None


def midpoint_cli():
    print("\n=== Midpoint Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()  
        if not raw:  
            print("You must enter a function. Try again.")
            continue
        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            print("Invalid function. Try again.")
            continue
        if len(symbols) != 1:
            print("Function must have exactly one variable. Detected variables:", symbols)
            continue
        
        var=symbols[0]
        
        if len(var.name) != 1:
            print(f"Variable name must be a single letter (x, y, z). Detected: {var}")
            continue
        break
    
    while True:
        a_input = input(f"Enter the value of lower limit for f{var}): ").strip()
        if not a_input:
            print("You must enter a numeric value.")
            continue
        try:
            a0 = float(a_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")
    while True:
        b_input = input(f"Enter the value of upper limit for f{var}): ").strip()
        if not b_input:
            print("You must enter a numeric value.")
            continue
        try:
            b0 = float(b_input)
            break
        except ValueError:
            print("Invalid number. Please try again.")        
            
    while True:
        n_input = input("Enter the number of intervals (n) : ").strip()
        if not n_input:
            print('you must enter a numeric number')
            continue
        try:
            n0=int(n_input)
            if n0 <= 0:
                print("Number of intervals must be positive.")
                continue
            break
        except ValueError:
            print("Invalid step size. Please enter a numeric value.")
            
    try:
        if a0 > b0:
            a0, b0 = b0, a0

            
        mp = midpoint_core(f, a0, b0, n0)

        if mp is None:
            print("Integration could not be computed.")
            return

    except Exception as e:
        print("Error during integration:", e)
        return        
            

    print("\n--- Results ---")
    print(f"Function:               {f_expr}")
    print(f"Variable:               {var}")
    print(f"Upper Limit =           {a0}")
    print(f"Lower Limit =           {b0}")
    print(f"No. of Intervals:       {n0}")
    print(f"Midpoint Integral:      {mp}")        
    
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")   
    
    
def simpson_core(f, a, b, n):
    try:
        if n % 2 != 0:
            print("Simpson's rule requires n to be even.")
            return None

        h = (b - a) / n
        x = a + h * np.arange(0, n + 1)

        fx = f(x)

        # Simpson weighting
        result = (h / 3) * (fx[0]+ fx[-1]+ 4 * np.sum(fx[1:n:2])+ 2 * np.sum(fx[2:n-1:2]))
        return result

    except Exception as e:
        print("Error computing Simpson integral:", e)
        return None
                
                
def simpson_cli():
    print("\n=== Simpson's 1/3 Rule Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()
        if not raw:
            print("You must enter a function.")
            continue

        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            continue
        if len(symbols) != 1:
            print("Function must have one variable.")
            continue

        var = symbols[0]
        if len(var.name) != 1:
            print("Variable name must be single letter.")
            continue
        break

    # lower limit
    while True:
        a_input = input(f"Enter the lower limit for {var}: ").strip()
        try:
            a0 = float(a_input)
            break
        except:
            print("Invalid number.")

    # upper limit
    while True:
        b_input = input(f"Enter the upper limit for {var}: ").strip()
        try:
            b0 = float(b_input)
            break
        except:
            print("Invalid number.")

    # n
    while True:
        n_input = input("Enter number of intervals n (even): ").strip()
        try:
            n0 = int(n_input)
            if n0 <= 0:
                print("n must be positive.")
                continue
            if n0 % 2 != 0:
                print("n must be EVEN for Simpson.")
                continue
            break
        except:
            print("Invalid number.")

    # swap limits if needed
    if a0 > b0:
        a0, b0 = b0, a0

    result = simpson_core(f, a0, b0, n0)
    if result is None:
        return

    print("\n--- Results ---")
    print(f"Function:            {f_expr}")
    print(f"Variable:            {var}")
    print(f"Lower Limit:         {a0}")
    print(f"Upper Limit:         {b0}")
    print(f"Intervals (n):       {n0}")
    print(f"Simpson 1/3 Result:  {result}")    
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")   
            
    
    
    
def simpson_38_core(f, a, b, n):
    try:
        if n % 3 != 0:
            print("Simpson 3/8 rule requires n to be divisible by 3.")
            return None

        h = (b - a) / n
        x = a + h * np.arange(0, n + 1)
        fx = f(x)

        # indices 1..n-1
        mid = np.arange(1, n)

        # weights
        w3 = fx[mid[(mid % 3) != 0]]   # not multiple of 3
        w2 = fx[mid[(mid % 3) == 0]]   # multiples of 3

        result = (3 * h / 8) * (fx[0] + fx[-1] + 3*np.sum(w3) + 2*np.sum(w2))
        return result

    except Exception as e:
        print("Error computing Simpson 3/8 integral:", e)
        return None

                
                
def simpson_38_cli():
    print("\n=== Simpson's 3/8 Rule Calculator ===")
    while True:
        raw = input("Enter a function f(x): ").strip()
        if not raw:
            print("You must enter a function.")
            continue

        f_expr, symbols, f = user_input_const(raw)
        if f is None:
            continue
        if len(symbols) != 1:
            print("Function must have one variable.")
            continue

        var = symbols[0]
        if len(var.name) != 1:
            print("Variable name must be single letter.")
            continue
        break

    # lower limit
    while True:
        a_input = input(f"Enter the lower limit for {var}: ").strip()
        try:
            a0 = float(a_input)
            break
        except:
            print("Invalid number.")

    # upper limit
    while True:
        b_input = input(f"Enter the upper limit for {var}: ").strip()
        try:
            b0 = float(b_input)
            break
        except:
            print("Invalid number.")

    # n
    while True:
        n_input = input("Enter number of intervals n (even): ").strip()
        try:
            n0 = int(n_input)
            if n0 <= 0:
                print("n must be positive.")
                continue
            if n0 % 3 != 0:
                print("n must be divisible by 3 for Simpson 3/8.")
                continue
            break
        except:
            print("Invalid number.")

    # swap limits if needed
    if a0 > b0:
        a0, b0 = b0, a0

    result = simpson_38_core(f, a0, b0, n0)
    if result is None:
        return

    print("\n--- Results ---")
    print(f"Function:            {f_expr}")
    print(f"Variable:            {var}")
    print(f"Lower Limit:         {a0}")
    print(f"Upper Limit:         {b0}")
    print(f"Intervals (n):       {n0}")
    print(f"Simpson 3/8 Result:  {result}") 
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")      
    
    
    
    
    
    
def euler_core(f, x0, y0, xf, n):
    try:
        h = (xf - x0) / n
        xs = np.linspace(x0, xf, n+1)
        ys = np.zeros(n+1)
        ys[0] = y0

        for i in range(n):
            ys[i+1] = ys[i] + h * f(xs[i], ys[i])

        return xs, ys
    except Exception as e:
        print("Error during Euler computation:", e)
        return None, None
                
                
def euler_cli():
    print("\n=== Euler Calculator ===")
   

    f_expr_internal, f, (indep_sym, dep_sym) = user_input_ode()
        

    print(f"Internal ODE interpreted as dy/dx = {f_expr_internal}")
    print(f"Independent variable = {indep_sym}, Dependent variable = {dep_sym}")
     


    
    while True:
        try:
            x0 = float(input(f"Enter initial value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            y0 = float(input(f"Enter {dep_sym} ({indep_sym} = {x0}): "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            xf = float(input(f"Enter final value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

            
    while True:
        n_input = input("Enter number of intervals n : ").strip()
        try:
            n0 = int(n_input)
            if n0 <= 0:
                print("n must be positive.")
                continue
            break
        except:
            print("Invalid number.")

    try:
        xs, ys = euler_core(f, x0, y0, xf, n0)
    except Exception as e:
        print("Error computing solution:", e)
        return

    print("\n--- Results ---")
    print(f"Function: dy/dx = {f_expr_internal}")
    print(f"Variable x: {indep_sym}, Variable y: {dep_sym}")
    print(f"Initial condition: {dep_sym}({indep_sym}={x0}) = {y0}")
    print(f"Final x = {xf}, Steps = {n0}")
    print("Solution (x, y):")
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.5f}, y = {yi:.5f}")   
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")            
    
    

def Heun_core(f, x0, y0, xf, n):
    try:
        h = (xf - x0) / n
        xs = np.linspace(x0, xf, n+1)
        ys = np.zeros(n+1)
        ys[0] = y0

        for i in range(n):
            k1 = f(xs[i], ys[i])
            y_predict = ys[i] + h * k1
            k2 = f(xs[i] + h, y_predict)
            ys[i+1] = ys[i] + (h/2) * (k1 + k2)

        return xs, ys
    except Exception as e:
        print("Error during Heun computation:", e)
        return None, None
                
                
def Heun_cli():
    print("\n=== Heun Calculator ===")
    
    f_expr_internal, f, (indep_sym, dep_sym) = user_input_ode()
        

    print(f"Internal ODE interpreted as dy/dx = {f_expr_internal}")
    print(f"Independent variable = {indep_sym}, Dependent variable = {dep_sym}")
        

    
    while True:
        try:
            x0 = float(input(f"Enter initial value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            y0 = float(input(f"Enter {dep_sym} ({indep_sym} = {x0}): "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            xf = float(input(f"Enter final value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

            
    while True:
        n_input = input("Enter number of intervals n : ").strip()
        try:
            n0 = int(n_input)
            if n0 <= 0:
                print("n must be positive.")
                continue
            break
        except:
            print("Invalid number.")

    try:
        xs, ys = Heun_core(f, x0, y0, xf, n0)
    except Exception as e:
        print("Error computing solution:", e)
        return

    print("\n--- Results ---")
    print(f"Function: dy/dx = {f_expr_internal}")
    print(f"Variable x: {indep_sym}, Variable y: {dep_sym}")
    print(f"Initial condition: {dep_sym}({indep_sym}={x0}) = {y0}")
    print(f"Final x = {xf}, Steps = {n0}")
    print("Solution (x, y):")
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.5f}, y = {yi:.5f}")       
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")        
    
    
    
def Midpoint_core(f, x0, y0, xf, n):
    try:
        h = (xf - x0) / n
        xs = np.linspace(x0, xf, n+1)
        ys = np.zeros(n+1)
        ys[0] = y0

        for i in range(n):
            k1 = f(xs[i], ys[i])
            k2 = f(xs[i] + h/2, ys[i] + (h/2) * k1)
            ys[i+1] = ys[i] + h * k2

        return xs, ys
    except Exception as e:
        print("Error during Midpoint computation:", e)
        return None, None
                
                
def Midpoint_cli():
    print("\n=== Midpoint Calculator ===")
    

    f_expr_internal, f, (indep_sym, dep_sym) = user_input_ode()
        
    print(f"Internal ODE interpreted as dy/dx = {f_expr_internal}")
    print(f"Independent variable = {indep_sym}, Dependent variable = {dep_sym}")
       


    
    while True:
        try:
            x0 = float(input(f"Enter initial value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            y0 = float(input(f"Enter {dep_sym} ({indep_sym} = {x0}): "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            xf = float(input(f"Enter final value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

            
    while True:
        n_input = input("Enter number of intervals n : ").strip()
        try:
            n0 = int(n_input)
            if n0 <= 0:
                print("n must be positive.")
                continue
            break
        except:
            print("Invalid number.")

    try:
        xs, ys = Midpoint_core(f, x0, y0, xf, n0)
    except Exception as e:
        print("Error computing solution:", e)
        return

    print("\n--- Results ---")
    print(f"Function: dy/dx = {f_expr_internal}")
    print(f"Variable x: {indep_sym}, Variable y: {dep_sym}")
    print(f"Initial condition: {dep_sym}({indep_sym}={x0}) = {y0}")
    print(f"Final x = {xf}, \nSteps = {n0}")
    print("Solution (x, y):")
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.5f}, y = {yi:.5f}")      
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")       
        
    
    
    
def RK2_core(f, x0, y0, xf, n):
    try:
        h = (xf - x0) / n
        xs = np.linspace(x0, xf, n+1)
        ys = np.zeros(n+1)
        ys[0] = y0

        for i in range(n):
            k1 = f(xs[i], ys[i])
            k2 = f(xs[i] + (2/3)*h, ys[i] + (2/3)*h*k1)
            try:
                ys[i+1] = ys[i] + h * (0.25*k1 + 0.75*k2)
            except Exception as e:
                print(f"Error at step {i}: {e}")
                return xs[:i+1], ys[:i+1]
        return xs, ys
    except Exception as e:
        print("Error during RK2 computation:", e)
        return None, None
                
                
def RK2_cli():
    print("\n=== RK2 Calculator ===")
  
    f_expr_internal, f, (indep_sym, dep_sym)= user_input_ode()
        
    print(f"Internal ODE interpreted as dy/dx = {f_expr_internal}")
    print(f"Independent variable = {indep_sym}, Dependent variable = {dep_sym}")



    
    while True:
        try:
            x0 = float(input(f"Enter initial value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            y0 = float(input(f"Enter {dep_sym} ({indep_sym} = {x0}): "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            xf = float(input(f"Enter final value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

            
    while True:
        n_input = input("Enter number of intervals n : ").strip()
        try:
            n0 = int(n_input)
            if n0 < 4:
                print("n must be positive.")
                continue
            break
        except:
            print("Invalid number.")

    try:
        xs, ys = RK2_core(f, x0, y0, xf, n0)
    except Exception as e:
        print("Error computing solution:", e)
        return

    print("\n--- Results ---")
    print(f"Function: dy/dx = {f_expr_internal}")
    print(f"Variable x: {indep_sym}, Variable y: {dep_sym}")
    print(f"Initial condition: {dep_sym}({indep_sym}={x0}) = {y0}")
    print(f"Final x = {xf}, \nSteps = {n0}")
    print("Solution (x, y):")
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.5e}, y = {yi:.5e}")  
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")          
    
    
    
def RK4_core(f, x0, y0, xf, n):
    try:
        h = (xf - x0) / n
        xs = np.linspace(x0, xf, n+1)
        ys = np.zeros(n+1)
        ys[0] = y0

        for i in range(n):
            k1 = f(xs[i], ys[i])
            k2 = f(xs[i] + h/2, ys[i] + h/2 * k1)
            k3 = f(xs[i] + h/2, ys[i] + h/2 * k2)
            k4 = f(xs[i] + h, ys[i] + h * k3)
            try:
                ys[i+1] = ys[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
            except Exception as e:
                print(f"Error at step {i}: {e}")
                return xs[:i+1], ys[:i+1]     
        return xs, ys
    except Exception as e:
        print("Error during RK4 computation:", e)
        return None, None
                
                
def RK4_cli():
    print("\n=== RK4 Calculator ===")
    

    f_expr_internal, f, (indep_sym, dep_sym) = user_input_ode()

    print(f"Internal ODE interpreted as dy/dx = {f_expr_internal}")
    print(f"Independent variable = {indep_sym}, Dependent variable = {dep_sym}")
        


    
    while True:
        try:
            x0 = float(input(f"Enter initial value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            y0 = float(input(f"Enter {dep_sym} ({indep_sym} = {x0}): "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            xf = float(input(f"Enter final value for {indep_sym}: "))
            break
        except:
            print("Invalid number.")

            
    while True:
        n_input = input("Enter number of intervals n : ").strip()
        try:
            n0 = int(n_input)
            if n0 < 4:
                print("n must be positive.")
                continue
            break
        except:
            print("Invalid number.")

    try:
        xs, ys = RK4_core(f, x0, y0, xf, n0)
    except Exception as e:
        print("Error computing solution:", e)
        return

    print("\n--- Results ---")
    print(f"Function: dy/dx = {f_expr_internal}")
    print(f"Variable x: {indep_sym}, Variable y: {dep_sym}")
    print(f"Initial condition: {dep_sym}({indep_sym}={x0}) = {y0}")
    print(f"Final x = {xf}, \nSteps = {n0}")
    print("Solution (x, y):")
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.5e}, y = {yi:.5e}")   
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")        
      
    
    
    
def rk45_core(f, x0, y0, xf, h0=0.1, tol=1e-6):
    

    try:
        x = float(x0)
        y = float(y0)
        xf = float(xf)
        h = float(h0)
        tol = float(tol)

        xs = [x]
        ys = [y]

        if h <= 0:
            raise ValueError("Initial step size h must be positive.")
        if tol <= 0:
            raise ValueError("Tolerance must be positive.")

        while x < xf:
            if x + h > xf:
                h = xf - x  # prevent overshoot

            # --- Dormand–Prince stages ---
            k1 = f(x, y)
            k2 = f(x + h/5, y + h*(k1/5))
            k3 = f(x + 3*h/10, y + h*(3*k1/40 + 9*k2/40))
            k4 = f(x + 4*h/5, y + h*(44*k1/45 - 56*k2/15 + 32*k3/9))
            k5 = f(
                x + 8*h/9,
                y + h*(19372*k1/6561 - 25360*k2/2187
                       + 64448*k3/6561 - 212*k4/729)
            )
            k6 = f(
                x + h,
                y + h*(9017*k1/3168 - 355*k2/33
                       + 46732*k3/5247 + 49*k4/176
                       - 5103*k5/18656)
            )

            # 4th-order solution
            y4 = y + h * (
                5179*k1/57600
                + 7571*k3/16695
                + 393*k4/640
                - 92097*k5/339200
                + 187*k6/2100
            )

            # 5th-order solution
            y5 = y + h * (
                35*k1/384
                + 500*k3/1113
                + 125*k4/192
                - 2187*k5/6784
                + 11*k6/84
            )

            # Error estimate
            err = abs(y5 - y4)

            # --- Step acceptance ---
            if err <= tol:
                x += h
                y = y5
                xs.append(x)
                ys.append(y)

            # --- Step size control ---
            if err == 0:
                s = 2.0
            else:
                s = 0.9 * (tol / err) ** 0.2

            # Clamp scaling factor
            s = min(5.0, max(0.2, s))
            h *= s

            if h <= 1e-14:
                raise RuntimeError("Step size underflow. ODE may be stiff.")

        return np.array(xs), np.array(ys)

    except Exception as e:
        print("RK45 solver failed:")
        print(e)
        return None, None                
                
def rk45_cli():
    print("\n=== RK45 (Adaptive Runge–Kutta) Calculator ===")

    
        

    f_expr_internal, f, (indep_sym, dep_sym) = user_input_ode()
    

    print(f"Internal ODE interpreted as dy/dx = {f_expr_internal}")
    print(f"Independent variable = {indep_sym}, Dependent variable = {dep_sym}")
        

    # --- Initial x ---
    while True:
        try:
            x0 = float(input(f"Enter initial value for {indep_sym}: "))
            break
        except ValueError:
            print("Invalid number.")

    # --- Initial y ---
    while True:
        try:
            y0 = float(input(f"Enter {dep_sym} ({indep_sym} = {x0}): "))
            break
        except ValueError:
            print("Invalid number.")

    # --- Final x ---
    while True:
        try:
            xf = float(input(f"Enter final value for {indep_sym}: "))
            if xf <= x0:
                print("Final value must be greater than initial value.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    # --- Initial step size ---
    while True:
        try:
            h0 = float(input("Enter initial step size h (e.g. 0.1): "))
            if h0 <= 0:
                print("Step size must be positive.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    # --- Tolerance ---
    while True:
        try:
            tol = float(input("Enter error tolerance (e.g. 1e-6): "))
            if tol <= 0:
                print("Tolerance must be positive.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    # --- Solve ---
    xs, ys = rk45_core(f, x0, y0, xf, h0, tol)
    if xs is None:
        print("Solution failed.")
        return

    # --- Output ---
    print("\nSolution (x, y):")
    for xi, yi in zip(xs, ys):
        print(f"{indep_sym} = {xi:.6f}, {dep_sym} = {yi:.6f}")
        
        
    print("\n--- Results ---")
    print(f"Function: dy/dx = {f_expr_internal}")
    print(f"Independent variable: {indep_sym}")
    print(f"Dependent variable:   {dep_sym}")
    print(f"Initial condition: {dep_sym}({indep_sym}={x0}) = {y0}")
    print(f"Final {indep_sym} = {xf}")
    print(f"Tolerance = {tol}")
    print(f"Steps taken = {len(xs)-1}")
    
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")   
    
    



def backward_euler_system_core(f, x0, y0, xf, n, tol=1e-8, max_iter=20):
    h = (xf - x0) / n
    m = len(y0)

    xs = np.linspace(x0, xf, n+1)
    ys = np.zeros((n+1, m))
    ys[0] = y0

    for i in range(n):
        x_next = xs[i+1]
        y_guess = ys[i].copy()

        converged = False

        for _ in range(max_iter):
            F = y_guess - ys[i] - h * np.array(f(x_next, y_guess))

            if np.linalg.norm(F) < tol:
                converged = True
                break

            J = np.eye(m)
            eps = 1e-6

            for j in range(m):
                y_eps = y_guess.copy()
                y_eps[j] += eps
                F_eps = y_eps - ys[i] - h * np.array(f(x_next, y_eps))
                J[:, j] = (F_eps - F) / eps

            delta = np.linalg.solve(J, -F)
            y_guess += delta

        if not converged:
            raise RuntimeError(f"Newton failed at step {i}")

        ys[i+1] = y_guess

    return xs, ys

def backward_euler_system_cli():
    print("\n=== Backward Euler (ODE System) ===")

    f, y_syms, x = user_input_ode_system()
    if f is None:
        return

    # --- initial x ---
    while True:
        try:
            x0 = float(input("Enter initial x: "))
            break
        except ValueError:
            print("Invalid number.")

    # --- initial y ---
    y0 = []
    for yi in y_syms:
        while True:
            try:
                val = float(input(f"Enter initial {yi} at x={x0}: "))
                y0.append(val)
                break
            except ValueError:
                print("Invalid number.")

    y0 = np.array(y0)

    # --- final x ---
    while True:
        try:
            xf = float(input("Enter final x: "))
            if xf <= x0:
                print("Final x must be greater than initial x.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    # --- steps ---
    while True:
        try:
            n = int(input("Enter number of steps: "))
            if n <= 0:
                print("Must be positive.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    try:
        xs, ys = backward_euler_system_core(f, x0, y0, xf, n)
    except Exception as e:
        print("Solver error:", e)
        return

    print("\n--- Solution ---")
    for i in range(len(xs)):
        vals = ", ".join(f"{y_syms[j]}={ys[i,j]:.6f}" for j in range(len(y_syms)))
        print(f"x={xs[i]:.4f} | {vals}")
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")       



def trapezoidal_system_core(f, x0, y0, xf, n, tol=1e-8, max_iter=20):
    h = (xf - x0) / n
    m = len(y0)

    xs = np.linspace(x0, xf, n+1)
    ys = np.zeros((n+1, m))
    ys[0] = y0

    for i in range(n):
        x_n = xs[i]
        x_np1 = xs[i+1]

        y_n = ys[i]
        y_guess = y_n.copy()

        f_n = np.array(f(x_n, y_n))

        for _ in range(max_iter):
            f_np1 = np.array(f(x_np1, y_guess))

            F = y_guess - y_n - (h/2)*(f_n + f_np1)

            if np.linalg.norm(F) < tol:
                break

            # Numerical Jacobian
            J = np.eye(m)
            eps = 1e-6

            for j in range(m):
                y_eps = y_guess.copy()
                y_eps[j] += eps
                f_eps = np.array(f(x_np1, y_eps))
                F_eps = y_eps - y_n - (h/2)*(f_n + f_eps)
                J[:, j] = (F_eps - F) / eps

            delta = np.linalg.solve(J, -F)
            y_guess += delta

        ys[i+1] = y_guess

    return xs, ys

def trapezoidal_system_cli():
    print("\n=== Trapezoidal Method (ODE System) ===")

    f, y_syms, x = user_input_ode_system()
    if f is None:
        return

    while True:
        try:
            x0 = float(input("Enter initial x: "))
            break
        except ValueError:
            print("Invalid number.")

    y0 = []
    for yi in y_syms:
        while True:
            try:
                val = float(input(f"Enter initial value {yi}(x0): "))
                y0.append(val)
                break
            except ValueError:
                print("Invalid number.")
    y0 = np.array(y0)

    while True:
        try:
            xf = float(input("Enter final x: "))
            break
        except ValueError:
            print("Invalid number.")

    while True:
        try:
            n = int(input("Enter number of steps: "))
            if n <= 0:
                print("Steps must be positive.")
                continue
            break
        except ValueError:
            print("Invalid integer.")

    xs, ys = trapezoidal_system_core(f, x0, y0, xf, n)

    print("\n--- Solution ---")
    for i in range(len(xs)):
        row = ", ".join(
            f"{y_syms[j]}={ys[i,j]:.6f}" for j in range(len(y_syms))
        )
        print(f"x={xs[i]:.4f} | {row}")    
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")   
    
    
    
def explicit_euler_system_core(f, x0, y0, xf, n):
    
    try:
        h = (xf - x0) / n
        m = len(y0)

        xs = np.linspace(x0, xf, n + 1)
        ys = np.zeros((n + 1, m))
        ys[0] = y0

        for i in range(n):
            ys[i + 1] = ys[i] + h * np.array(f(xs[i], ys[i]))

        return xs, ys

    except Exception as e:
        print("Error during Explicit Euler computation:", e)
        return None, None


def explicit_euler_system_cli():
    print("\n=== Explicit Euler (ODE System) ===")

    f, y_syms, x = user_input_ode_system()
    if f is None:
        return

    # --- Initial x ---
    while True:
        try:
            x0 = float(input("Enter initial x: "))
            break
        except ValueError:
            print("Invalid number.")

    # --- Initial y vector ---
    y0 = []
    for yi in y_syms:
        while True:
            try:
                y0.append(float(input(f"Enter initial value {yi}(x0): ")))
                break
            except ValueError:
                print("Invalid number.")
    y0 = np.array(y0)

    # --- Final x ---
    while True:
        try:
            xf = float(input("Enter final x: "))
            break
        except ValueError:
            print("Invalid number.")

    # --- Steps ---
    while True:
        try:
            n = int(input("Enter number of steps: "))
            if n <= 0:
                print("Number of steps must be positive.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    xs, ys = explicit_euler_system_core(f, x0, y0, xf, n)
    if xs is None:
        return

    # --- Output ---
    print("\n--- Solution ---")
    for i in range(len(xs)):
        row = ", ".join(
            f"{y_syms[j]}={ys[i, j]:.6f}" for j in range(len(y_syms))
        )
        print(f"x={xs[i]:.4f} | {row}")    
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")    
    
    

def rk4_system_core(f, x0, y0, xf, n):
    try:
        h = (xf - x0) / n
        m = len(y0)

        xs = np.linspace(x0, xf, n+1)
        ys = np.zeros((n+1, m))
        ys[0] = y0

        for i in range(n):
            x = xs[i]
            y = ys[i]

            k1 = np.array(f(x, y))
            k2 = np.array(f(x + h/2, y + h*k1/2))
            k3 = np.array(f(x + h/2, y + h*k2/2))
            k4 = np.array(f(x + h,   y + h*k3))

            ys[i+1] = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

        return xs, ys

    except Exception as e:
        print("Error during RK4 computation:", e)
        return None, None


def rk4_system_cli():
    print("\n=== Runge–Kutta 4 (ODE System) ===")

    f, y_syms, x = user_input_ode_system()
    if f is None:
        return

    while True:
        try:
            x0 = float(input("Enter initial x: "))
            break
        except:
            print("Invalid number.")

    y0 = []
    for yi in y_syms:
        while True:
            try:
                y0.append(float(input(f"Enter initial value {yi}(x0): ")))
                break
            except:
                print("Invalid number.")
    y0 = np.array(y0)

    while True:
        try:
            xf = float(input("Enter final x: "))
            break
        except:
            print("Invalid number.")

    while True:
        try:
            n = int(input("Enter number of steps: "))
            if n <= 0:
                print("Must be positive.")
                continue
            break
        except:
            print("Invalid number.")

    xs, ys = rk4_system_core(f, x0, y0, xf, n)
    if xs is None:
        return

    print("\n--- Solution ---")
    for i in range(len(xs)):
        row = ", ".join(
            f"{y_syms[j]}={ys[i, j]:.6f}" for j in range(len(y_syms))
        )
        print(f"x={xs[i]:.4f} | {row}")
        
    while True:
        choice = input("Do you want to perform more calculations? (y/n): ").strip().lower()

        if choice == "y":
            break
        elif choice == "n":
            print("Returning to Intermediate Menu...")
            return
        else:
            print("Invalid input. Enter 'y' or 'n' only.")         
    
    
    
menu()