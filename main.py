import tkinter as tk
from settings import Settings

app_settings = Settings()
root = tk.Tk()
root.title("Workout Planner")
root.geometry("1500x1800")
root.configure(bg=app_settings.screen_bg_color)


screen1 = tk.Frame(root, bg=app_settings.screen_bg_color)
screen1.pack(fill="both", expand=True)

label = tk.Label(screen1, text="Welcome", font=("Arial", 30))
label.pack(pady=10)

gender_var = tk.StringVar()
gender_var.set("Select Gender")
dropdown = tk.OptionMenu(screen1, gender_var, "Male", "Female")
dropdown.configure(width=15, font=("Arial", 12))
dropdown["menu"].config(font=("Arial", 12))
dropdown.pack(anchor="w", padx=20)

weight_frame = tk.Frame(screen1, bg="#1a1a2e")
weight_frame.pack(anchor="w", padx=20, pady=5)
weight_label = tk.Label(weight_frame, text="Enter Weight:", font=(
    "Arial", 12), bg="#1a1a2e", fg="white")
weight_label.pack(side="left")
weight_entry = tk.Entry(weight_frame, width=15, font=("Arial", 12))
weight_entry.pack(side="left", padx=10)

height_frame = tk.Frame(screen1, bg="#1a1a2e")
height_frame.pack(anchor="w", padx=20)
height_label = tk.Label(height_frame, text="Enter height:", font=(
    "Arial", 12), bg="#1a1a2e", fg="white")
height_label.pack(side="left")
height_entry = tk.Entry(height_frame, width=15, font=("Arial", 12))
height_entry.pack(side="left", padx=10)

age_frame = tk.Frame(screen1, bg="#1a1a2e")
age_frame.pack(anchor="w", padx=20, pady=5)
age_label = tk.Label(age_frame, text="Enter Age:", font=(
    "Arial", 12), bg="#1a1a2e", fg="white")
age_label.pack(side="left")
age_entry = tk.Entry(age_frame, width=15, font=("Arial", 12))
age_entry.pack(side="left", padx=10)

# screen2
screen2 = tk.Frame(root, bg="#1a1a2e")


def show_screen2():
    screen1.pack_forget()    # hide screen1
    screen2.pack(fill="both", expand=True)   # show screen2


def combined():
    get_inputs()
    show_screen2()


def get_inputs():
    weight = weight_entry.get()
    height = height_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    return weight, height, age, gender


btn = tk.Button(screen1, text="Calculate", font=("Arial", 12),
                bg="#4CAF50", fg="white", command=combined)
btn.pack(pady=20)

root.mainloop()
