import tkinter as tk

import sys

sys.path.insert(1, "TODOLISTCS151/commands")

from commands import home_popup as homepop

#create the page
home_page = tk.Tk()

user_label_list = []

#set size of the page and title it
home_page.geometry("1440x1024")
home_page.title("home page")

#create title label
home_page_title = tk.Label(home_page, text="To-do List Application", font=("times new roman", 50, "bold"))

#creates the new user button and places it
new_user_button = tk.Button(home_page, text="+", relief="sunken" ,font=("times new roman", 50, "bold"), command=homepop.open_user_pop_up)

#create subtitle label
home_user_label = tk.Label(home_page, text="Users", font=("times new roman", 30))

#will for each user named and will display their name
with open("placebo_user.txt", "r") as users:
    user_names = users.readlines()
    
for i in range(len(user_names)):
    user_label_list.append(f"user_label{i}")
    user_label_list[-1] = tk.Label(home_page, text=user_names[i], relief="ridge", font=("times new roman", 25))

#opens the window
#home_page.mainloop()    
