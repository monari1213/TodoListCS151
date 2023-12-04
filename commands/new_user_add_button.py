import tkinter as tk
import os 

import sys

sys.path.insert(1, "TODOLISTCS151/stored_files")

def new_user(entry):
    newpath = fr"TODOLISTCS151/stored_files/users/{entry}"
    if not os.path.exist(newpath):
        os.makedirs(newpath)