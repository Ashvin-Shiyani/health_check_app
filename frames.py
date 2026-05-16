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
