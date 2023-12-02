import tkinter as tk

import sys

sys.path.insert(1, "TODOLISTCS151/subsystems")

from subsystems import home_page_tk_code as home

def open_user_pop_up ():
    #creates the pop_up
    use_pop_up = tk.Toplevel(home.home_page)
    use_pop_up.geometry("750x270")
    use_pop_up.Title("pop_up")
    
    #creates labels for entries
    new_user_label = tk.Label(use_pop_up,  text="New User", font=("times new roman", 30))
    
    #creates entries
    new_user_entry = tk.Entry(use_pop_up)
    
    #creates add button
    add_button = tk.Button(use_pop_up, text = "Add user" ,relief="sunken" ,font=("times new roman", 30))
    