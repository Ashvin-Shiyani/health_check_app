import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

dfs = pd.read_csv("male.csv")


def risk_bar_chart(file_name, bmi, screen2):
    df = pd.read_csv(file_name)

    diseases = ["diabetes_risk_percent", "heart_disease_risk_percent", "hypertension_risk_percent",  # find row and column
                "stroke_risk_percent", "gallstones_risk_percent", "heart_failure_risk_percent"]
    row = df[(df["bmi_min"] <= bmi) & (df["bmi_max"] >= bmi)]

    labels = ["Diabetes", "Heart Disease", "Hypertension",
              "Stroke", "Gallstones", "Heart Failure"]
    values = [row[disease].values[0] for disease in diseases]

    fig, ax = plt.subplots(figsize=(8, 5))

    plt.bar(labels, values)
    ax.set_title("Your health Risks  by disease")
    ax.set_xlabel("Disease")
    ax.set_ylabel("Risk %")
    ax.set_ylim(0, 100)
    plt.xticks(rotation=45)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=screen2)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", padx=20, pady=20)
