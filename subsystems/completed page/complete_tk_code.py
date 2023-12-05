import tkinter as tk

import back_button as back

complete_page = tk.Tk()
complete_page.geometry("1440x1024")
complete_page.title("complete page")


completed_title = tk.Label(complete_page, text="Completed Items", font=("times new roman", 69, "bold"))
# need to place
completed_sub_title = tk.Label(complete_page, text="{user}'s To-Do-List", font=("times new roman", 40))
# need to place

#create back button
complete_back_button = tk.Button(complete_page, text="Back", relief="sunken" ,font=("times new roman", 30), command=back.go_back)

#creates the page
#complete_page.mainloop()