import tkinter as tk
from functools import partial
from commands_package.back_button import go_back
from commands_package.read_lists import read_user_lists

#import back_button as back
#import read_lists as read

#creates the window
user_page = tk.Tk()

list_num_list = []
task_num_list = []

#sets the size of the page and title
user_page.geometry("1440x1024")
user_page.title("user page")

#labels the window 
user_title = tk.Label(user_page, text="To-do List", font=("times new roman", 50, "bold"))

#creates the new list button and places it
new_list_button = tk.Button(user_page, text="+", relief="sunken" ,font=("times new roman", 50, "bold"))

#create back button
go_back_arg = partial(go_back, "user_page")
user_back_button = tk.Button(user_page, text="Back", relief="sunken" ,font=("times new roman", 30), command= go_back_arg)

#the lists buttons and their corresponding tasks need to be adjusted for all the different possible files

lists = read_user_lists()
    
for i in range(len(lists)):
    list_num_list.append(f"{lists[i]}")
    list_num_list[-1] = tk.Button(user_page, text= list_num_list[-1 ], relief="sunken", font=("times new roman", 30))
    tasks = read_user_lists(list_num_list[-1])
    for j in range(len(tasks)):
        task_num_list.append(f"{tasks[j]}")
        task_num_list[-1] = tk.Label(user_page, text=(task_num_list[-1]), relief="ridge", font=("times new roman", 25)) 
        

#opens the page
user_page.mainloop()