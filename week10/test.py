import tkinter as tk
def submit_data():
    """Get input from entry widgets"""
    name = name_entry.get()
    email = email_entry.get()
    result_label.config( text=f"Name: {name}\nEmail: {email}" )
    # Clear entries
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    
root = tk.Tk()
root.title("Entry Demo")
root.geometry("450x300")
# Name input
tk.Label(root, text="Name:", font=("Arial", 11)).pack(pady=5)
name_entry = tk.Entry(
    root,
    font=("Arial", 11),
    width=30,
    bd=2, # Border width
    relief=tk.SUNKEN # Border style
)
name_entry.pack(pady=5)
tk.Label(root, text="Email:", font=("Arial", 11)).pack(pady=5)
email_entry = tk.Entry(root, font=("Arial", 11), width=30)
email_entry.pack(pady=5)
# Submit button
submit_btn = tk.Button(
    root,
    text="Submit",
    command=submit_data,
    font=("Arial", 12),
    bg="#2196F3",
    fg="white",
    padx=20,
    pady=8
)
submit_btn.pack(pady=15)
# Result display
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    fg="green"
)
result_label.pack(pady=10)
root.mainloop()