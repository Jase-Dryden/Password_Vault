import tkinter as tk

root = tk.Tk
frame  = tk.Frame(root)
frame.master.title("Password Vault")
frame.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

popualte_main_window(frame)





def popualte_main_window(frame):
    but_login = tk.Button(frame,text="Black")
    but_add_user = tk.Button(frame,text="Black")
    but_remove = tk.Button(frame,text="Black")

    but_login.grid(row=2, column=0, padx=3, pady=3, columnspan=5, sticky="w")
