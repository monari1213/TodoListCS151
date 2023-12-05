import tkinter as tk
#import home_popup as homepop
#import read_lists as read

#create the page
home_page = tk.Tk()

user_label_list = []
user_checkbox_list = []
checkbox = []

#set size of the page and title it
home_page.geometry("1440x1024")
home_page.title("home page")

#create title label
home_page_title = tk.Label(home_page, text="To-do List Application", font=("times new roman", 50, "bold"))

#creates the new user button and places it
new_user_button = tk.Button(home_page, text="+", relief="sunken" ,font=("times new roman", 50, "bold"))#, command=homepop.open_user_pop_up)

#create subtitle label
home_user_label = tk.Label(home_page, text="Users", font=("times new roman", 30))

#will for each user named and will display their name
user_names = ["Kristina", "Megan", "Cynthia", "Mr. John"]#read.read_user_lists("placebo_users")
    
for i in range(len(user_names)):
    user_label_list.append(f"user_label{i}")
    user_checkbox_list.append(f"checkbox_var{i}")
    checkbox.append(f"checkbox{i}")
    user_label_list[-1] = tk.Label(home_page, text=user_names[i], relief="ridge", font=("times new roman", 25))
    #checkbox button
    user_checkbox_list[-1] = tk.StringVar()
    checkbox[-1] = tk.Checkbutton(home_page,
                text='<checkbox_label_1>',
                #command=check_changed,
                variable=user_checkbox_list[-1],
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
    # https://www.pythontutorial.net/tkinter/tkinter-checkbox/
    checkbox[-1].pack(side="left",anchor="nw",padx=(2,0))
    #needs to be next row but that is a not right now problem
    

#opens the window
home_page.mainloop()    