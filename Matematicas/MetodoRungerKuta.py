import tkinter as tk
from tkinter import messagebox
from functools import partial
import sympy as sp

def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0
    result = [(x, y)]

    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

        result.append((x, y))

    return result

def calculate_runge_kutta(equation, x0, y0, h, n):
    try:
        x, y = sp.symbols('x y')
        f = sp.sympify(equation)
        f_lambda = sp.lambdify((x, y), f)
        results = runge_kutta(f_lambda, x0, y0, h, n)
        return results
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return []

def calculate_button_click(equation_entry, x0_entry, y0_entry, h_entry, n_entry, result_text):
    equation = equation_entry.get()
    x0 = float(x0_entry.get())
    y0 = float(y0_entry.get())
    h = float(h_entry.get())
    n = int(n_entry.get())

    results = calculate_runge_kutta(equation, x0, y0, h, n)

    result_text.delete(1.0, tk.END)
    for result in results:
        result_text.insert(tk.END, f"x: {result[0]}, y: {result[1]}\n")

def main():
    root = tk.Tk()
    root.title("Calculadora Método de Runge-Kutta")

    equation_label = tk.Label(root, text="Ecuación:")
    equation_label.pack()

    equation_entry = tk.Entry(root)
    equation_entry.pack()

    x0_label = tk.Label(root, text="x0:")
    x0_label.pack()

    x0_entry = tk.Entry(root)
    x0_entry.pack()

    y0_label = tk.Label(root, text="y0:")
    y0_label.pack()

    y0_entry = tk.Entry(root)
    y0_entry.pack()

    h_label = tk.Label(root, text="Tamaño del Paso (h):")
    h_label.pack()

    h_entry = tk.Entry(root)
    h_entry.pack()

    n_label = tk.Label(root, text="Número de Pasos (n):")
    n_label.pack()

    n_entry = tk.Entry(root)
    n_entry.pack()

    result_text = tk.Text(root)
    result_text.pack()

    calculate_button = tk.Button(root, text="Calcular", command=partial(calculate_button_click, equation_entry, x0_entry, y0_entry, h_entry, n_entry, result_text))
    calculate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
