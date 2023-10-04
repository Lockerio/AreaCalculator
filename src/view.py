import tkinter as tk

from src.calculator.figures.circle import Circle
from src.calculator.figures.triangle import Triangle


def activate_figure(figure: str):
    for figures_widget in figures_widgets:
        figures_widget["state"] = tk.DISABLED

    match figure:
        case "circle":
            circle_radius_label["state"] = tk.NORMAL
            circle_radius_entry["state"] = tk.NORMAL

        case "triangle":
            triangle_side_label["state"] = tk.NORMAL
            triangle_side_a_entry["state"] = tk.NORMAL
            triangle_side_b_entry["state"] = tk.NORMAL
            triangle_side_c_entry["state"] = tk.NORMAL


def find_area(figure: str):
    match figure:
        case "circle":
            try:
                circle_radius = float(circle_radius_entry.get())
                area = Circle.calculate_area(circle_radius)
                calculated_area_label["text"] = area
            except ValueError as e:
                calculated_area_label["text"] = e
            except Exception as e:
                calculated_area_label["text"] = e

        case "triangle":
            try:
                triangle_side_a = triangle_side_a_entry.get()
                triangle_side_b = triangle_side_b_entry.get()
                triangle_side_c = triangle_side_c_entry.get()
                area = Triangle.calculate_area([triangle_side_a, triangle_side_b, triangle_side_c])
                calculated_area_label["text"] = area
            except ValueError as e:
                calculated_area_label["text"] = e
            except Exception as e:
                calculated_area_label["text"] = e

        case "not chosen":
            calculated_area_label["text"] = "You didn't choose any figure!"


win = tk.Tk()
win.geometry("600x300+500+150")
win.resizable(False, False)
win.title("Area calculator")

win.grid_columnconfigure(0, minsize=300)
win.grid_columnconfigure(1, minsize=300)

figures = {
    0: "not chosen",
    1: "circle",
    2: "triangle"
}

figure_var = tk.IntVar()
figure_var.set(0)

# Header
tk.Label(win, text="Choose a figure:").grid(row=0, column=0, columnspan=2, stick="we")

# Figures
circle_radiobutton = tk.Radiobutton(win,
                                    text="Circle",
                                    variable=figure_var,
                                    value=1,
                                    command=lambda: activate_figure("circle"))
circle_radiobutton.grid(row=1, column=0)
triangle_radiobutton = tk.Radiobutton(win,
                                      text="Triangle",
                                      variable=figure_var,
                                      value=2,
                                      command=lambda: activate_figure("triangle"))
triangle_radiobutton.grid(row=1, column=1)

# Circle
circle_radius_label = tk.Label(win,
                               text="Enter radius:",
                               state=tk.DISABLED)
circle_radius_label.grid(row=2, column=0)
circle_radius_entry = tk.Entry(win, state=tk.DISABLED)
circle_radius_entry.grid(row=3, column=0)

# Triangle
triangle_side_label = tk.Label(win,
                               text="Enter sides of the triangle:",
                               state=tk.DISABLED)
triangle_side_label.grid(row=2, column=1)
triangle_side_a_entry = tk.Entry(win, state=tk.DISABLED)
triangle_side_b_entry = tk.Entry(win, state=tk.DISABLED)
triangle_side_c_entry = tk.Entry(win, state=tk.DISABLED)
triangle_side_a_entry.grid(row=3, column=1)
triangle_side_b_entry.grid(row=4, column=1)
triangle_side_c_entry.grid(row=5, column=1)


# Footer
calculate_area_btn = tk.Button(win,
                               text="Calculate area",
                               command=lambda: find_area(figures[figure_var.get()]))
calculate_area_btn.grid(row=6, column=0, columnspan=2)

calculated_area_label = tk.Label(win, text="")
calculated_area_label.grid(row=7, column=0, columnspan=2, stick="we")

figures_widgets = [
    circle_radius_label,
    circle_radius_entry,
    triangle_side_label,
    triangle_side_a_entry,
    triangle_side_b_entry,
    triangle_side_c_entry,
]

win.mainloop()
