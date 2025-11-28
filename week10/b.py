# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

rates = {
    "TWD": 1,
    "USD": 31,
    "JPY": 0.22,
    "EUR": 34
}

def convert():
    try:
        amount = float(entry_amount.get())
        if amount < 0:
            raise ValueError

        from_currency = combo_from.get()
        to_currency = combo_to.get()

        twd_value = amount * rates[from_currency]
        result = twd_value / rates[to_currency]

        result_var.set(f"結果: {amount:.2f} {from_currency} = {result:.2f} {to_currency}")

    except:
        messagebox.showerror("輸入錯誤", "請輸入正確的金額。")


window = tk.Tk()
window.title("貨幣兌換工具")
window.geometry("380x200")

tk.Label(window, text="金額：").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Label(window, text="原始貨幣：").grid(row=1, column=0, padx=10, pady=10, sticky="w")
combo_from = ttk.Combobox(window, values=list(rates.keys()), state="readonly")
combo_from.current(0)
combo_from.grid(row=1, column=1, padx=10, pady=10, sticky="w")

tk.Label(window, text="目標貨幣：").grid(row=2, column=0, padx=10, pady=10, sticky="w")
combo_to = ttk.Combobox(window, values=list(rates.keys()), state="readonly")
combo_to.current(1)
combo_to.grid(row=2, column=1, padx=10, pady=10, sticky="w")

tk.Button(window, text="開始兌換", command=convert).grid(row=3, column=0, padx=10, pady=10, sticky="w")

# tk.Label(window, text="結果：").grid(row=4, column=0, padx=10, pady=10, sticky="w")
result_var = tk.StringVar()
tk.Label(window, textvariable=result_var).grid(row=4, column=0, columnspan=2, padx=10 ,pady=10, sticky="w")

window.mainloop()
