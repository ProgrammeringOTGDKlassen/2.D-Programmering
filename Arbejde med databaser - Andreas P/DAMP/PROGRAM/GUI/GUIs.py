import tkinter as tk
import tkinter.ttk as ttk

import sys, os

def nav_to_folder_w_file(folder_path: str):
    abs_file_path = os.path.abspath(__file__)                # Absolute Path of the module
    file_dir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
    parent_dir = os.path.dirname(file_dir)                   # Directory of the Module directory
    new_path = os.path.join(parent_dir, folder_path)   # Get the directory for StringFunctions
    sys.path.append(new_path)


# DATA--------------------------------------------------------
nav_to_folder_w_file('DATA')
from damp_datalayer import DAMPData
# ------------------------------------------------------------


# APP---------------------------------------------------------
nav_to_folder_w_file('APP')
import loading
# ------------------------------------------------------------


# LOCAL_FOLDER (this folder)----------------------------------
nav_to_folder_w_file('GUI')



# classes
# ----------------------------------------------------------------------

# separate GUI as the login-screen
class DampLoginGui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def launch_DAMP(self):
        self.destroy()
        loading.load_main_app()


    def launch_add_user(self):
        self.destroy()
        loading.load_add_user_app()



    def build_GUI(self):
        # defining elements of GUI
        self.username_label = tk.Label(self, text = 'Username')
        self.password_label = tk.Label(self, text = 'Password')
        self.name_entry = tk.Entry(self)
        self.pass_entry = tk.Entry(self)
        self.but_sign_in = ttk.Button(self, text = 'Sign In', command = self.launch_DAMP)
        self.create_user_label = tk.Label(self, text = "Don't have an account?")
        self.but_create_user = ttk.Button(self, text = 'Create User', command = self.launch_add_user)

        # placing elements of GUI
        self.username_label.grid(row = 0, sticky = tk.E)
        self.password_label.grid(row = 1, sticky = tk.E)
        self.name_entry.grid(row = 0, column = 1)
        self.pass_entry.grid(row = 1, column = 1)

        self.but_sign_in.grid(row = 3, column = 1)

        self.create_user_label.grid(row = 4, sticky = tk.E, pady=(20, 10))
        self.but_create_user.grid(row = 4, column = 1, pady=(20, 10))

        self.pack()


# separate GUI as the "add-user"-screen
class DampAddUserGui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def launch_DAMP(self):
        self.destroy()
        loading.load_main_app()


    def launch_signin(self):
        self.destroy()
        loading.load_login_app()


    def build_GUI(self):
        # defining elements of GUI
        self.name_label = tk.Label(self, text = 'Name')
        self.mail_label = tk.Label(self, text = 'E-mail')
        self.country_label = tk.Label(self, text = 'Country')
        self.username_label = tk.Label(self, text = 'Username')
        self.password_label = tk.Label(self, text = 'Password')
        self.re_password_label = tk.Label(self, text = 'Re-enter Password')
        
        self.name_entry = tk.Entry(self)
        self.mail_entry = tk.Entry(self)
        self.country_entry = tk.Entry(self)
        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self)
        self.re_password_entry = tk.Entry(self)

        self.but_sign_in = ttk.Button(self, text = 'Sign Up', command = self.launch_DAMP)
        self.create_user_label = tk.Label(self, text = "Already have an account?")
        self.but_create_user = ttk.Button(self, text = 'Sign In', command = self.launch_signin)

        # placing elements of GUI
        self.name_label.grid(row = 0, sticky = tk.E)
        self.mail_label.grid(row = 1, sticky = tk.E)
        self.country_label.grid(row = 2, sticky = tk.E)
        self.username_label.grid(row = 3, sticky = tk.E)
        self.password_label.grid(row = 4, sticky = tk.E)
        self.re_password_label.grid(row = 5, sticky = tk.E)

        self.name_entry.grid(row = 0, column = 1)
        self.mail_entry.grid(row = 1, column = 1)
        self.country_entry.grid(row = 2, column = 1)
        self.username_entry.grid(row = 3, column = 1)
        self.password_entry.grid(row = 4, column = 1)
        self.re_password_entry.grid(row = 5, column = 1)

        self.but_sign_in.grid(row = 6, column = 1)

        self.create_user_label.grid(row = 7, sticky = tk.E, pady=(20, 10))
        self.but_create_user.grid(row = 7, column = 1, pady=(20, 10))

        self.pack()


# main GUI
class DampGui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass

