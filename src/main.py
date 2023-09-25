import tkinter as tk

from src.figures.circle import Circle


def find_area(figure: str):
    match figure:
        case "circle":
            circle_radius = int(circle_radius_entry.get())
            area = Circle.calculate_area(circle_radius)
            calculated_area_label["text"] = area

        case "triangle":
            pass



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
circle_radius_entry = tk.Entry(win)
circle_radius_entry.grid(row=3, column=0)

# Triangle
tk.Label(win, text="Enter sides of the triangle:").grid(row=2, column=1)
tk.Entry(win).grid(row=3, column=1)
tk.Entry(win).grid(row=4, column=1)
tk.Entry(win).grid(row=5, column=1)

# Footer
calculate_area_btn = tk.Button(win,
                               text="Calculate area",
                               command=lambda: find_area(figures[figure_var.get()]))
calculate_area_btn.grid(row=6, column=0, columnspan=2)

calculated_area_label = tk.Label(win, text="")
calculated_area_label.grid(row=7, column=0, columnspan=2, stick="we")



win.mainloop()
