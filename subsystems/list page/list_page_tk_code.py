import tkinter as tk

list_page = tk.Tk()
list_page.geometry("1440x1024")
list_page.title("list page")


user_list = tk.Label(list_page, text="List 1 Name", font=("times new roman", 69, "bold")).place(x=25, y=25)

# list1_button = tk.Button(user_page, text="List 1 Name", relief="sunken" ,font=("times new roman", 30))


user_page.mainloop()