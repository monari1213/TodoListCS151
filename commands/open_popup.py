import tkinter as tk

import sys

sys.path.insert(1, "TODOLISTCS151/subsystems")

from subsystems import list_page_tk_code as list

def open_pop_up (button):
    #creates the pop_up
    pop_up = tk.Toplevel(list.list_page)
    pop_up.geometry("750x270")
    pop_up.Title("pop_up")
    
    #creates labels for entries
    task_label = tk.Label(pop_up,  text="Task", font=("times new roman", 30))
    date_label = tk.Label(pop_up,  text="Due Date", font=("times new roman", 30))
    priority_label = tk.Label(pop_up,  text="Priority", font=("times new roman", 30))
    type_label = tk.Label(pop_up,  text="Type", font=("times new roman", 30))
    
    #creates entries
    task_entry = tk.Entry(pop_up)
    date_entry = tk.Entry(pop_up)
    priority_entry = tk.Entry(pop_up)
    type_entry = tk.Entry(pop_up)
    
    #creates add button
    add_button = tk.Button(pop_up, text = "Add task" ,relief="sunken" ,font=("times new roman", 30))
    
    #makes it the add screen or the edit screen
    if button == "add_button":
        title_label = tk.Label(pop_up, text="Add a Task", font=("times new roman", 50, "bold"))
    else:
        title_label = tk.Label(pop_up, text="Edit a Task", font=("times new roman", 50, "bold"))
        completed_button = tk.Button(pop_up, text = "Mark task completed" ,relief="sunken" ,font=("times new roman", 30))
        delete_button = tk.Button(pop_up, text = "Delete task" ,relief="sunken" ,font=("times new roman", 30))