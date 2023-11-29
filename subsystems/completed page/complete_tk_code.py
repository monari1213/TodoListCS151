import tkinter as tk

complete_page = tk.Tk()
complete_page.geometry("1440x1024")
complete_page.title("complete page")


completed_title = tk.Label(list_page, text="Completed", font=("times new roman", 69, "bold"))
# need to place
completed_sub_title = tk.Label(list_page, text="{user}'s To-Do-List}", font=("times new roman", 69, "bold"))
# need to place


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

list_page.mainloop()