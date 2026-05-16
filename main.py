import tkinter as tk
from settings import Settings
import frames as fr

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


weight_entry = fr.weight_input(screen1)

height_entry = fr.height_input(screen1)

age_entry = fr.age_input(screen1)


screen2 = tk.Frame(root, bg="#1a1a2e")


def show_screen2():
    screen1.pack_forget()
    screen2.pack(fill="both", expand=True)   # show screen2


def combined():
    result = get_inputs()
    if result is None:
        return
    weight, height, age, gender = result
    bmi = weight / (height ** 2)

    if gender == "Male":
        from male import Male
        ml = Male(bmi)
        label = tk.Label(screen2, text=ml.print_gender(), font=(
            "Arial", 12), bg="#1a1a2e", fg="white")
        label.pack(anchor="w", padx=20)

    if gender == "Female":
        from female import Female
        fml = Female(bmi)
        label = tk.Label(screen2, text=fml.print_gender(), font=(
            "Arial", 12), bg="#1a1a2e", fg="white")
        label.pack(anchor="w", padx=20)

    show_screen2()


def get_inputs():
    if weight_entry.get() == '' or height_entry.get() == '' or age_entry.get() == '':
        print("Please fill all fields")
        return
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()
    return weight, height, age, gender


result = get_inputs()
if result is None:
    pass
else:
    weight, height, age, gender = result
    bmi = weight / (height ** 2)


btn = tk.Button(screen1, text="Calculate", font=("Arial", 12),
                bg="#4CAF50", fg="white", command=combined)
btn.pack(pady=20)


root.mainloop()
