import tkinter as tk

# import back_button as back
#import open_popup as pop

list_page = tk.Tk()
list_page.geometry("1440x1024")
list_page.title("list page")


user_list = tk.Label(list_page, 
                     text="List 1 Name", 
                     font=("times new roman", 69, "bold"))
user_list.pack(side="left",anchor="nw",padx=(100,0), pady=(75,0))



edit_button = tk.Button(user_list, 
                        text="E", 
                        relief="sunken" ,
                        font=("times new roman", 30))
#edit_button.pack(side="right", anchor = "ne", padx = 50, pady=100)

add_button = tk.Button(user_list, 
                       text="A", 
                       relief="sunken" ,
                       font=("times new roman", 30))

#create back button
list_back_button = tk.Button(list_page, text="Back", relief="sunken" ,font=("times new roman", 30)) # command=back.go_back)
#list_back_button.grid(column=0, row=0, sticky= "wens")

checkbox_var1 = tk.StringVar()
checkbox1 = tk.Checkbutton(list_page,
                text='<checkbox_label_1>',
                #command=check_changed,
                variable=checkbox_var1,
                font=("times new roman", 30),
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
# https://www.pythontutorial.net/tkinter/tkinter-checkbox/
checkbox1.pack(side="left",anchor="nw",padx=(100,0), pady=(100,0))

#description1 = tk.Label(list_page, text="List 1 Name", font=("times new roman", 69, "bold"))


checkbox_var2 = tk.StringVar()
checkbox2 = tk.Checkbutton(list_page,
                text='<checkbox_label_2>',
                #command=check_changed,
                variable=checkbox_var1,
                font=("times new roman", 30),
                onvalue='<value_when_checked>',
                offvalue='<value_when_unchecked>')
# https://www.pythontutorial.net/tkinter/tkinter-checkbox/
checkbox2.pack(side="left",anchor="w",padx=(10,0), pady=(10,0))



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