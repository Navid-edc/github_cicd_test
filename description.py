import tkinter as tk


window = tk.Tk()
window.title("Description")
window.geometry("320x120")

tk.Label(window, text="Description bar", font=("Arial", 16)).pack(pady=35)

window.mainloop()
