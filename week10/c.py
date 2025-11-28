import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("生活健康問卷")
root.geometry("500x400")

header = tk.Label(root, text="生活健康調查問卷", font=("Arial", 20))
header.pack(pady=15)

q1 = tk.IntVar(value=-1)
q2 = tk.IntVar(value=-1)
q3 = tk.IntVar(value=-1)
q4 = tk.IntVar(value=-1)

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="1. 是否有抽菸習慣？", font=("Arial", 12)).grid(row=0, column=0, sticky="w")

tk.Radiobutton(frame, text="是", variable=q1, value=0).grid(row=0, column=1, sticky="w")
tk.Radiobutton(frame, text="否", variable=q1, value=1).grid(row=0, column=2, sticky="w")

tk.Label(frame, text="2. 是否有飲酒習慣？", font=("Arial", 12)).grid(row=1, column=0, sticky="w")

tk.Radiobutton(frame, text="是", variable=q2, value=0).grid(row=1, column=1, sticky="w")
tk.Radiobutton(frame, text="否", variable=q2, value=1).grid(row=1, column=2, sticky="w")


tk.Label(frame, text="3. 每天睡眠時間是否超過六小時？", font=("Arial", 12)).grid(row=2, column=0, sticky="w")

tk.Radiobutton(frame, text="是", variable=q3, value=1).grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame, text="否 ", variable=q3, value=0).grid(row=2, column=2, sticky="w")


tk.Label(frame, text="4. 是否有均衡飲食？", font=("Arial", 12)).grid(row=3, column=0, sticky="w")

tk.Radiobutton(frame, text="是", variable=q4, value=1).grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame, text="否", variable=q4, value=0).grid(row=3, column=2, sticky="w")


def calculate_score():
    answers = [q1.get(), q2.get(), q3.get(), q4.get()]

    if -1 in answers:
        messagebox.showwarning("提示", "請回答所有題目後再提交。")
        return

    total = sum(answers)

    if total >= 3:
        result_label.config(text=f"您的總分為：{total} 分\n健康狀態：健康狀況良好")
    else:
        result_label.config(text=f"您的總分為：{total} 分\n健康狀態：健康狀況不好")


submit_btn = tk.Button(
    root,
    text="送出問卷並顯示結果",
    font=("Arial", 13),
    padx=20,
    pady=6,
    command=calculate_score
)
submit_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=15)

root.mainloop()
