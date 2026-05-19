import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

dfs = pd.read_csv("male.csv")


def risk_bar_chart(file_name, bmi, screen2):
    df = pd.read_csv(file_name)

    diseases = ["diabetes_risk_percent", "heart_disease_risk_percent", "hypertension_risk_percent",  # find row and column
                "stroke_risk_percent", "gallstones_risk_percent", "heart_failure_risk_percent"]
    if bmi > df["bmi_max"].max():
        bmi = df["bmi_max"].max()
    row = df[(df["bmi_min"] <= bmi) & (df["bmi_max"] >= bmi)]

    labels = ["Diabetes", "Heart Disease", "Hypertension",
              "Stroke", "Gallstones", "Heart Failure"]
    values = [row[disease].values[0] for disease in diseases]

    fig, ax = plt.subplots(figsize=(6, 5))

    ax.bar(labels, values)
    ax.set_title("Your health Risks  by disease")
    ax.set_xlabel("Disease")
    ax.set_ylabel("Risk %")
    ax.set_ylim(0, 100)
    plt.xticks(rotation=45)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=screen2)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", padx=20, pady=20)


def hori_bar_chart(file_name, bmi, screen2):
    df = pd.read_csv(file_name)

    values = df["estimated_deaths_per_100k"].to_list()
    labels = ["Below 18.5,0", "18.5 - 24.9", "25.0 - 29.9",
              "30.0 - 34.9", "35.0 - 39.9", "40.0 and above"]

    fig, ax = plt.subplots(figsize=(6, 5))

    ax.barh(labels, values)
    ax.set_title("Death Rate")
    ax.set_xlabel("Deaths per 100k")
    ax.set_ylabel("BMI range")
    ax.set_xlim(0, 500)
    ax.set_xticks([0, 100, 200, 300, 400, 500])
    ax.set_xticklabels(["0", "100", "200", "300", "400", "500"])
    plt.xticks(rotation=45)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=screen2)
    canvas.draw()
    canvas.get_tk_widget().pack(side="right", padx=20, pady=20)
