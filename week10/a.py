# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import font

def calculate_bmi():
    try:
        h = float(entry_height.get())
        w = float(entry_weight.get())

        if h <= 0 or w <= 0:
            raise ValueError

        h_m = h / 100
        bmi = w / (h_m ** 2)

        bmi_min = 18.5
        bmi_max = 24.0
        weight_min = bmi_min * (h_m ** 2)
        weight_max = bmi_max * (h_m ** 2)

        result_bmi.set(f"您的 BMI：{bmi:.2f}")
        result_range.set(f"健康體重範圍：{weight_min:.1f} kg ～ {weight_max:.1f} kg")

    except:
        messagebox.showerror("輸入錯誤", "請輸入正確的數字格式（身高、體重需為正值）。")

window = tk.Tk()
window.title("BMI 計算器")
window.geometry("360x240")



tk.Label(window, text="身高（公分）：").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_height = tk.Entry(window)
entry_height.grid(row=0, column=1, sticky="w", padx=10, pady=5)

tk.Label(window, text="體重（公斤）：").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_weight = tk.Entry(window)
entry_weight.grid(row=1, column=1, sticky="w", padx=10, pady=5)

tk.Button(window, text="計算 BMI", command=calculate_bmi).grid(row=2, column=0, sticky="w", padx=10, pady=10)

result_bmi = tk.StringVar()
tk.Label(window, textvariable=result_bmi).grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

result_range = tk.StringVar()
tk.Label(window, textvariable=result_range).grid(row=4, column=0, columnspan=2, sticky="w", padx=10)

window.mainloop()