import tkinter as tk
from tkinter import messagebox

records = []

def update_total():
    total = sum(amount for _, amount in records)
    total_value_label.config(text=f"{total:.2f} 元")

def add_record():
    item = item_entry.get().strip()
    money_text = money_entry.get().strip()

    if not item or not money_text:
        messagebox.showwarning("提醒", "請輸入品項與金額！")
        return
    try:
        money = float(money_text)
        if money < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("錯誤", "金額必須為非負數字！")
        return

    records.append((item, money))
    listbox.insert(tk.END, f"{item}　-　{money:.2f} 元")

    item_entry.delete(0, tk.END)
    money_entry.delete(0, tk.END)

    update_total()

def delete_selected():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("提醒", "請先選取要刪除的項目。")
        return

    idx = sel[0]
    listbox.delete(idx)
    records.pop(idx)
    update_total()


def clear_all():
    if not records:
        return
    if messagebox.askyesno("確認", "確定要清空所有紀錄嗎？"):
        listbox.delete(0, tk.END)
        records.clear()
        update_total()


root = tk.Tk()
root.title("記帳小工具")
root.geometry("470x420")
root.configure(bg="#e6e6e6") 

root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=0)

label_font = ("Microsoft JhengHei", 11)
btn_font = ("Microsoft JhengHei", 10)

item_label = tk.Label(root, text="品項：", font=label_font, bg="#e6e6e6")
item_label.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="e")

item_entry = tk.Entry(root, width=22, font=label_font)
item_entry.grid(row=0, column=1, pady=(15, 5), sticky="w")

add_btn = tk.Button(root, text="新增", width=10, font=btn_font, command=add_record)
add_btn.grid(row=0, column=2, padx=20, pady=(15, 5))

money_label = tk.Label(root, text="金額：", font=label_font, bg="#e6e6e6")
money_label.grid(row=1, column=0, padx=20, pady=5, sticky="e")

money_entry = tk.Entry(root, width=22, font=label_font)
money_entry.grid(row=1, column=1, pady=5, sticky="w")

del_btn = tk.Button(root, text="刪除選取", width=10, font=btn_font, command=delete_selected)
del_btn.grid(row=1, column=2, padx=20, pady=5)


listbox = tk.Listbox(root, width=45, height=12, font=("Microsoft JhengHei", 10))
listbox.grid(row=2, column=0, columnspan=2, padx=20, pady=15, sticky="w")

clear_btn = tk.Button(root, text="清空", width=10, font=btn_font, command=clear_all)
clear_btn.grid(row=2, column=2, padx=20, pady=15, sticky="W")

bottom_frame = tk.Frame(root, bg="#e6e6e6")
bottom_frame.grid(row=3, column=0, columnspan=3, sticky="w", padx=20, pady=20)

total_text_label = tk.Label(
    bottom_frame,
    text="總金額：",
    font=("Microsoft JhengHei", 11),
    bg="#e6e6e6"
)
total_text_label.pack(side=tk.LEFT)

total_value_label = tk.Label(
    bottom_frame,
    text="0.00 元",
    font=("Microsoft JhengHei", 11, "bold"),
    fg="black",
    bg="#e6e6e6"
)
total_value_label.pack(side=tk.LEFT)

root.mainloop()
