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

calcualte_pressed = False


def show_screen2():
    screen1.pack_forget()
    screen2.pack(fill="both", expand=True)   # show screen2


def get_inputs():
    if (weight_entry.get() == '' or height_entry.get() == '' or age_entry.get() == '') and calcualte_pressed:
        fr.message(screen1)
        return
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()
    return weight, height, age, gender


def combined():
    global calcualte_pressed
    calcualte_pressed = True
    result = get_inputs()
    if result is None:
        return
    weight, height, age, gender = result
    bmi = weight / (height ** 2)
    if age > 110 or height > 3:
        fr.error_message(screen1)
        return
    else:
        pass

    if gender == "Male":
        fr.male_frame(screen2, bmi)

    if gender == "Female":
        fr.female_frame(screen2, bmi)

    fr.weight_screen2(screen2, weight)
    fr.height_screen2(screen2, height)
    fr.age_screen2(screen2, age)
    fr.bmi_screen2(screen2, bmi)

    show_screen2()


btn = tk.Button(screen1, text="Calculate", font=("Arial", 12),
                bg="#4CAF50", fg="white", command=combined)
btn.pack(pady=20)


root.mainloop()
