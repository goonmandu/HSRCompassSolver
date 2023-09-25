import tkinter as tk
import math

def update_selected_hour(event):
    x = event.x - center_x
    y = event.y - center_y
    angle = math.degrees(math.atan2(y, x))
    if angle < 0:
        angle += 360
    hour = math.ceil(angle / 30)
    selected_hour.set(hour)
    hour_var.set(str(hour))

root = tk.Tk()
root.title("Selectable Clock Face")

selected_hour = tk.IntVar()
selected_hour.set(12)

hour_var = tk.StringVar()

canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

center_x = 150
center_y = 150
radius = 120

for hour in range(1, 13):
    angle = math.radians(360 * (hour / 12))
    x = center_x + radius * math.cos(angle)
    y = center_y - radius * math.sin(angle)
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="black")
    canvas.create_text(x, y, text=str(hour), font=("Helvetica", 12, "bold"))

canvas.bind("<Button-1>", update_selected_hour)

selected_hour_label = tk.Label(root, textvariable=selected_hour)
selected_hour_label.grid(row=1, columnspan=2, pady=10)

root.mainloop()
