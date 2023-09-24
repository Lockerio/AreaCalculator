import tkinter as tk

from src.figures.circle import Circle
from src.figures.triangle import Triangle

win = tk.Tk()
win.geometry("600x600+500+150")
win.resizable(False, False)
win.title("Area calculator")

win.grid_columnconfigure(0, minsize=300)
win.grid_columnconfigure(1, minsize=300)

figures = {
    1: "circle",
    2: "triangle"
}

figure_var = tk.IntVar()

# Header
tk.Label(win, text="Choose a figure").grid(row=0, column=0, columnspan=2, stick="we")

# Figures
tk.Radiobutton(win, text="Circle", variable=figure_var, value=1).grid(row=1, column=0)
tk.Radiobutton(win, text="Triangle", variable=figure_var, value=2).grid(row=1, column=1)


# Circle
tk.Label(win, text="Enter radius:").grid(row=2, column=0)
tk.Entry(win).grid(row=3, column=0)

# Triangle
tk.Label(win, text="Enter sides of the triangle:").grid(row=2, column=1)
tk.Entry(win).grid(row=3, column=1)
tk.Entry(win).grid(row=4, column=1)
tk.Entry(win).grid(row=5, column=1)

# Footer
tk.Button(win, text="Calculate area").grid(row=6, column=0, columnspan=2)
tk.Label(win, text="").grid(row=7, column=0, columnspan=2, stick="we")



win.mainloop()
