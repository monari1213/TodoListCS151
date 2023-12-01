import tkinter as tk

import sys

sys.path.insert(1, "TODOLISTCS151/commands")

from commands import back_button as back

complete_page = tk.Tk()
complete_page.geometry("1440x1024")
complete_page.title("complete page")


completed_title = tk.Label(complete_page, text="Completed Items", font=("times new roman", 69, "bold")).grid(column=1, row=0, columnspan=4)
# need to place
completed_sub_title = tk.Label(complete_page, text="{user}'s To-Do-List", font=("times new roman", 40)).grid(column=1, row=1, columnspan=3, pady=10)
# need to place

#create back button
complete_back_button = tk.Button(complete_page, text="Back", relief="sunken" ,font=("times new roman", 30), command=back.go_back)
complete_back_button.grid(column=0, row=0, sticky= "wens")

# now for the task descriptions
# make sure the y coordinate of these is the same as the corresponding textbox
# the x coordinates for all of these should be the same so they are vertically aligned
# should we delineate task_1_title from task_1_description and place one under the other?
# also think about aligning here, want to make sure its on the left of the label
task_1_description = tk.Label(complete_page, text="{text_1_description}", font=("times new roman", 20)).grid(column=1, row=2, pady=10)
# need to properly place
task_2_description = tk.Label(complete_page, text="{text_2_description}", font=("times new roman", 20)).grid(column=1, row=3, pady=10)
# need to properly place
task_3_description = tk.Label(complete_page, text="{text_3_description}", font=("times new roman", 20)).grid(column=1, row=4, pady=10)
# need to properly place
task_4_description = tk.Label(complete_page, text="{text_4_description}", font=("times new roman", 20)).grid(column=1, row=5, pady=10)
# need to properly place

#creates the page
#complete_page.mainloop()