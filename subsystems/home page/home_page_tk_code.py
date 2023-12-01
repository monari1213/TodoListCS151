import tkinter as tk

#create the page
home_page = tk.Tk()

#set size of the page and title it
home_page.geometry("1440x1024")
home_page.title("home page")

#formats the grid
home_page.grid_columnconfigure(0, pad=25)
home_page.grid_columnconfigure(9, pad=25)
home_page.grid_rowconfigure(0, pad=10)

#create title label
home_page_title = tk.Label(home_page, text="To-do List Application", font=("times new roman", 50, "bold"))
home_page_title.grid(column=1, columnspan=4, row=1)

#create back button
home_back_button = tk.Button(home_page, text="Back", relief="sunken" ,font=("times new roman", 30))
home_back_button.grid(column=0, row=0, sticky= "wens")

#creates the new user button and places it
new_user_button = tk.Button(home_page, text="+", relief="sunken" ,font=("times new roman", 50, "bold"))
new_user_button.grid(column=9, row=0, sticky="wens")

#create subtitle label
home_user_label = tk.Label(home_page, text="Users", font=("times new roman", 30))
home_user_label.grid(column=1, columnspan=2,row=2, padx= 10, pady = 25)

#will for each user named and will display their name
# with open("placebo_user.txt", "r") as users:
#     user_names = users.readlines()
    
# for i in range(len(user_names)):

placebo_user_label = tk.Label(home_page, text="Placebo User", relief="ridge", font=("times new roman", 25)).grid(column=1, row=3, padx=10)

#opens the window
#home_page.mainloop()    
