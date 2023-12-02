import tkinter as tk
import sys

sys.path.insert(1, "TODOLISTCS151/commands")

from commands import back_button as back
from commands import open_popup as pop

list_page = tk.Tk()
list_page.geometry("1440x1024")
list_page.title("list page")


user_list = tk.Label(list_page, text="List 1 Name", font=("times new roman", 69, "bold")).grid(column=1, row=0, columnspan=3, sticky= "wens")

edit_button = tk.Button(user_list, text="E", relief="sunken" ,font=("times new roman", 30), command= pop.open_pop_up).grid(column=8, row=0, sticky= "wens")
add_button = tk.Button(user_list, text="A", relief="sunken" ,font=("times new roman", 30), command= pop.open_pop_up).grid(column=9, row=0, sticky= "wens")

#create back button
list_back_button = tk.Button(list_page, text="Back", relief="sunken" ,font=("times new roman", 30), command=back.go_back)
list_back_button.grid(column=0, row=0, sticky= "wens")

# place all the way to the left
# also need an arrow

# code it so that it is a bool, either complete or not
# below the goal is just to make a circle
# intentionally not putting in details
# also need to make sure they are **buttons***
#commented out to remove errors while I push - Kristina
# task_1_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
# task_2_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
# task_3_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
# task_4_checkbox = tk.Canvas.create_circle(x, y, r, options...

# now for the task descriptions
# make sure the y coordinate of these is the same as the corresponding textbox
# the x coordinates for all of these should be the same so they are vertically aligned
# should we delineate task_1_title from task_1_description and place one under the other?
# also think about aligning here, want to make sure its on the left of the label
task_1_description = tk.Label(list_page, text="{text_1_description}", font=("times new roman", 20)).grid(column=1, row=1, pady=10)
# need to properly place
task_2_description = tk.Label(list_page, text="{text_2_description}", font=("times new roman", 20)).grid(column=1, row=2, pady=10)
# need to properly place
task_3_description = tk.Label(list_page, text="{text_3_description}", font=("times new roman", 20)).grid(column=1, row=3, pady=10)
# need to properly place
task_4_description = tk.Label(list_page, text="{text_4_description}", font=("times new roman", 20)).grid(column=1, row=4, pady=10)
# need to properly place

#opens the page
#list_page.mainloop()