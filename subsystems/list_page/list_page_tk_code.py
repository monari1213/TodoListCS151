import tkinter as tk
import sys

sys.path.insert(1, "TODOLISTCS151/commands")

from commands import back_button as back
from commands import open_popup as pop

list_page = tk.Tk()
list_page.geometry("1440x1024")
list_page.title("list page")


user_list = tk.Label(list_page, text="List 1 Name", font=("times new roman", 69, "bold"))

edit_button = tk.Button(user_list, text="E", relief="sunken" ,font=("times new roman", 30)).grid(column=8, row=0, sticky= "wens")
add_button = tk.Button(user_list, text="A", relief="sunken" ,font=("times new roman", 30)).grid(column=9, row=0, sticky= "wens")

#create back button
list_back_button = tk.Button(list_page, text="Back", relief="sunken" ,font=("times new roman", 30), command=back.go_back)
list_back_button.grid(column=0, row=0, sticky= "wens")

# place all the way to the left
# also need an arrow

#commented out arrow code cause its pissng me off - Kristina
# arrow = tk.Canvas(user_list, width = 400, height = 400)
# arrow.pack()
# # draw an arrow from (50,50) to (200,200)
# arrow.create_line(50,50,200,200, arrow=tk.LAST)
# code creds for the arrow: https://www.codeease.net/programming/python/drawing-arrows-in-tkinter
# NONE OF THESE NUMBER PLACEMENTS ARE RIGHT BECAUSE I CANT RUN MY CODE
# THEY ARE PLACEHOLDERS

# code it so that it is a bool, either complete or not
# below the goal is just to make a circle
# intentionally not putting in details
# also need to make sure they are **buttons***
#commented out to remove errors while I push - Kristina
# task_1_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
checkbox_var1 = tk.StringVar()
checkbox1 = tk.Checkbutton(list_page,
                text='<checkbox_label_1>',
                #command=check_changed,
                variable=checkbox_var1,
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
# https://www.pythontutorial.net/tkinter/tkinter-checkbox/
checkbox1.pack(side="left",anchor="nw",padx=(2,0))
# task_2_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
# task_3_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
# task_4_checkbox = tk.Canvas.create_circle(x, y, r, options...

# now for the task descriptions
# make sure the y coordinate of these is the same as the corresponding textbox
# the x coordinates for all of these should be the same so they are vertically aligned
# should we delineate task_1_title from task_1_description and place one under the other?
# also think about aligning here, want to make sure its on the left of the label
# task_1_description = tk.Label(list_page, text="{text_1_description}", font=("times new roman", 20)).grid(column=1, row=1, pady=10)
# # need to properly place
# task_2_description = tk.Label(list_page, text="{text_2_description}", font=("times new roman", 20)).grid(column=1, row=2, pady=10)
# # need to properly place
# task_3_description = tk.Label(list_page, text="{text_3_description}", font=("times new roman", 20)).grid(column=1, row=3, pady=10)
# # need to properly place
# task_4_description = tk.Label(list_page, text="{text_4_description}", font=("times new roman", 20)).grid(column=1, row=4, pady=10)
# # need to properly place

#opens the page
list_page.mainloop()