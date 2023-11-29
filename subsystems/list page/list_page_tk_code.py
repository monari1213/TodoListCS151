import tkinter as tk

list_page = tk.Tk()
list_page.geometry("1440x1024")
list_page.title("list page")


user_list = tk.Label(list_page, text="List 1 Name", font=("times new roman", 69, "bold")).place(x=25, y=25)

edit_button = tk.Button(user_page, text="E", relief="sunken" ,font=("times new roman", 30))
# need to place this somewhere
add_button = tk.Button(user_page, text="A", relief="sunken" ,font=("times new roman", 30))
# place to right of edit button

back_button = tk.Button(user_page, text="Back", relief="sunken" ,font=("times new roman", 30))
# place all the way to the left
# also need an arrow

arrow = tk.Canvas(root, width = 400, height = 400)
arrow.pack()
# draw an arrow from (50,50) to (200,200)
arrow.create_line(50,50,200,200, arrow=tk.LAST)
# code creds for the arrow: https://www.codeease.net/programming/python/drawing-arrows-in-tkinter
# NONE OF THESE NUMBER PLACEMENTS ARE RIGHT BECAUSE I CANT RUN MY CODE
# THEY ARE PLACEHOLDERS
list_page.mainloop()

# code it so that it is a bool, either complete or not
# below the goal is just to make a circle
# intentionally not putting in details
# also need to make sure they are **buttons***
task_1_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
task_2_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
task_3_checkbox = tk.Canvas.create_circle(x, y, r, options...) 
task_4_checkbox = tk.Canvas.create_circle(x, y, r, options...) 

# now for the task descriptions
# make sure the y coordinate of these is the same as the corresponding textbox
# the x coordinates for all of these should be the same so they are vertically aligned
# should we delineate task_1_title from task_1_description and place one under the other?
# also think about aligning here, want to make sure its on the left of the label
task_1_description = tk.Label(list_page, text="{text_1_description}", font=("times new roman", 20))
# need to properly place
task_2_description = tk.Label(list_page, text="{text_2_description}", font=("times new roman", 20))
# need to properly place
task_3_description = tk.Label(list_page, text="{text_3_description}", font=("times new roman", 20))
# need to properly place
task_4_description = tk.Label(list_page, text="{text_4_description}", font=("times new roman", 20))
# need to properly place
