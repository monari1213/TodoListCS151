import tkinter as tk

user_page = tk.Tk()
user_page.geometry("1440x1024")
user_page.title("user page")


user_title = tk.Label(user_page, text="To-do List", font=("times new roman", 69, "bold")).place(x=25, y=25)

list1_button = tk.Button(user_page, text="List 1 Name", relief="sunken" ,font=("times new roman", 30))
list1_button.place(x=100, y=150)

new_list_button = tk.Button(user_page, text="+", relief="sunken" ,font=("times new roman", 80, "bold"))
new_list_button.place(x=1000, y=50)

list1_label1 = tk.Label(user_page, text=("task 1"), relief="ridge", font=("times new roman", 25)).place(x=150, y=275)
list1_label2 = tk.Label(user_page, text=("task 2"), relief="ridge", font=("times new roman", 25)).place(x=300, y=275)
list1_label3 = tk.Label(user_page, text=("task 3"), relief="ridge", font=("times new roman", 25)).place(x=450, y=275)


user_page.mainloop()