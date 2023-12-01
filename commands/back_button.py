import sys

sys.path.insert(1, "TODOLISTCS151/subsystems")

from subsystems import list_page_tk_code as list
from subsystems import user_tk_code as user
from subsystems import home_page_tk_code as home

def go_back(current_page):
    if current_page == "completed page" or current_page == "add pop-up" or current_page == "edit pop-up":
        #set page to list page
        list.list_page.mainloop()
    elif current_page == "list page":
        #set page to user page
        user.user_page.mainloop()
    elif current_page == "user_page":
        #set page to home page
        home.home_page.mainloop()