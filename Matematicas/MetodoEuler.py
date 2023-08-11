import tkinter as tk
from tkinter import ttk
import numpy as np
import sympy as sp

def euler_modificado(f, y0, t0, h, num_steps):
    t = t0
    y = y0

    results = []

    for _ in range(num_steps):
        y_temp = y + h * f(t, y)
        y = y + (h / 2) * (f(t, y) + f(t + h, y_temp))
        t += h
        results.append((t, y))

    return results

def calculate():
    t0 = float(t0_entry.get())
    y0 = float(y0_entry.get())
    h = float(h_entry.get())
    num_steps = int(num_steps_entry.get())
    equation = equation_entry.get()

    t, y = sp.symbols('t y')
    f_expr = sp.sympify(equation.replace('^', '**'))
    
    def f(t_val, y_val):
        return f_expr.subs([(t, t_val), (y, y_val)])
    
    results = euler_modificado(f, y0, t0, h, num_steps)

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    for t, y in results:
        result_text.insert(tk.END, f"t = {t:.2f}, y = {y:.6f}\n")
    result_text.config(state=tk.DISABLED)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Método de Euler Modificado")

frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Valor inicial t0:").grid(column=0, row=0, sticky=tk.W)
ttk.Label(frame, text="Valor inicial y0:").grid(column=0, row=1, sticky=tk.W)
ttk.Label(frame, text="Tamaño del paso h:").grid(column=0, row=2, sticky=tk.W)
ttk.Label(frame, text="Número de pasos:").grid(column=0, row=3, sticky=tk.W)
ttk.Label(frame, text="Ecuación diferencial (t, y):").grid(column=0, row=4, sticky=tk.W)

t0_entry = ttk.Entry(frame)
t0_entry.grid(column=1, row=0)

y0_entry = ttk.Entry(frame)
y0_entry.grid(column=1, row=1)

h_entry = ttk.Entry(frame)
h_entry.grid(column=1, row=2)

num_steps_entry = ttk.Entry(frame)
num_steps_entry.grid(column=1, row=3)

equation_entry = ttk.Entry(frame)
equation_entry.grid(column=1, row=4)

calculate_button = ttk.Button(frame, text="Calcular", command=calculate)
calculate_button.grid(column=0, row=5, columnspan=2)

result_text = tk.Text(root, state=tk.DISABLED, height=10, width=40)
result_text.grid(column=0, row=1, columnspan=2)

root.mainloop()








