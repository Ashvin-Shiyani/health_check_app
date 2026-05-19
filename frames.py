import tkinter as tk


def weight_input(screen1):

    weight_frame = tk.Frame(screen1, bg="#1a1a2e")
    weight_frame.pack(anchor="w", padx=20, pady=5)
    weight_label = tk.Label(weight_frame, text="Enter Weight(kg):", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    weight_label.pack(side="left")
    weight_entry = tk.Entry(weight_frame, width=15, font=("Arial", 12))
    weight_entry.pack(side="left", padx=10)
    return weight_entry


def height_input(screen1):
    height_frame = tk.Frame(screen1, bg="#1a1a2e")
    height_frame.pack(anchor="w", padx=20)
    height_label = tk.Label(height_frame, text="Enter height(m):", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    height_label.pack(side="left")
    height_entry = tk.Entry(height_frame, width=15, font=("Arial", 12))
    height_entry.pack(side="left", padx=10)
    return height_entry


def age_input(screen1):
    age_frame = tk.Frame(screen1, bg="#1a1a2e")
    age_frame.pack(anchor="w", padx=20, pady=5)
    age_label = tk.Label(age_frame, text="Enter Age:", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    age_label.pack(side="left")
    age_entry = tk.Entry(age_frame, width=15, font=("Arial", 12))
    age_entry.pack(side="left", padx=10)
    return age_entry


def message(screen1):
    msg_frame = tk.Frame(screen1, bg="#1a1a2e")
    msg_frame.pack(anchor="w", padx=20, pady=5)
    msg_label = tk.Label(msg_frame, text="Please fill all the fields:", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    msg_label.pack(side="left")


def male_frame(screen2, bmi):
    from male import Male
    ml = Male(bmi)
    label = tk.Label(screen2, text=ml.print_gender(), font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    label.pack(anchor="w", padx=20)


def female_frame(screen2, bmi):
    from female import Female
    fml = Female(bmi)
    label = tk.Label(screen2, text=fml.print_gender(), font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    label.pack(anchor="w", padx=20)


def age_screen2(screen2, age):
    age_frame = tk.Frame(screen2, bg="#1a1a2e")
    age_frame.pack(anchor="w", padx=20, pady=5)
    age_label = tk.Label(age_frame, text=f"Your age:{age}", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    age_label.pack(side="left")


def weight_screen2(screen2, weight):
    weight_frame = tk.Frame(screen2, bg="#1a1a2e")
    weight_frame.pack(anchor="w", padx=20, pady=5)
    weight_label = tk.Label(weight_frame, text=f"Your weight:{weight}", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    weight_label.pack(side="left")


def height_screen2(screen2, height):
    height_frame = tk.Frame(screen2, bg="#1a1a2e")
    height_frame.pack(anchor="w", padx=20, pady=5)
    height_label = tk.Label(height_frame, text=f"Your height:{height}", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    height_label.pack(side="left")


def error_message(screen1):
    msg_frame = tk.Frame(screen1, bg="#1a1a2e")
    msg_frame.pack(anchor="w", padx=20, pady=5)
    msg_label = tk.Label(msg_frame, text=f"Please enter valid inputs", font=(
        "Arial", 12), bg="#1a1a2e", fg="white")
    msg_label.pack(side="left")
