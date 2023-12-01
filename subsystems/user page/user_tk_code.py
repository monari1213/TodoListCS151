import tkinter as tk

import sys

sys.path.insert(1, "TODOLISTCS151/commands/back_button")

from sys import back_button as back

#creates the window
user_page = tk.Tk()

pixel = tk.PhotoImage(width=1, height=1)

# #getting screen width and height of display
# #https://www.geeksforgeeks.org/how-to-create-full-screen-window-in-tkinter/#
# width= user_page.winfo_screenwidth() 
# height= user_page.winfo_screenheight()
# user_page.geometry("%dx%d" % (width, height))
user_page.geometry("1440x1024")
user_page.title("user page")

#formats the grid
user_page.grid_columnconfigure(0, pad=25)
user_page.grid_columnconfigure(9, pad=25)
user_page.grid_rowconfigure(0, pad=10)

#labels the window 
user_title = tk.Label(user_page, text="To-do List", font=("times new roman", 50, "bold"))
user_title.grid(column=1, columnspan=8,row=1, sticky= "w")

#creates the new list button and places it
new_list_button = tk.Button(user_page, text="+", relief="sunken" ,font=("times new roman", 50, "bold"))
new_list_button.grid(column=9, row=0, sticky="wens")

#create back button
user_back_button = tk.Button(user_page, text="Back", relief="sunken" ,font=("times new roman", 30), command=back.go_back)
user_back_button.grid(column=0, row=0, sticky= "wens")

# #creates arrow
# user_arrow = tk.Canvas(user_page, width = 100, height = 100)
# user_arrow.grid(column=0, row=0, sticky="wens")

# user_arrow.create_line(100,75,25,75, arrow=tk.LAST)

#the lists buttons and their corresponding tasks need to be adjusted for all the different possible files
#creates the first list 
list1_button = tk.Button(user_page, text="List 1 Name", relief="sunken", font=("times new roman", 30))
list1_button.grid(column=1, columnspan=2,row=2, padx= 10, pady = 10)

#creates the tasks 
list1_label1 = tk.Label(user_page, text=("task 1"), relief="ridge", font=("times new roman", 25)).grid(column=1, row=3, padx=10)
list1_label2 = tk.Label(user_page, text=("task 2"), relief="ridge", font=("times new roman", 25)).grid(column=2, row=3, padx=10)
list1_label3 = tk.Label(user_page, text=("task 3"), relief="ridge", font=("times new roman", 25)).grid(column=3, row=3, padx=10)

#opens the page
user_page.mainloop()