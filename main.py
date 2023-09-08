import os
import customtkinter as ctk
import tkinter.messagebox as messagebox

login = ctk.CTk()
login.geometry("200x185")
login.eval('tk::PlaceWindow . center')
login.title("login page")

mainname = ctk.CTkEntry(login, placeholder_text="Username")
mainname.place(x=33, y=30)

mainpwd = ctk.CTkEntry(login, placeholder_text="Password")
mainpwd.place(x=33, y=70)

def loginfn():
    username = mainname.get()
    password = mainpwd.get()

        # Check if username or password is empty
    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    # Check if the user file exists
    if not os.path.exists(f"{username}.txt"):
        messagebox.showerror("Error", "User not found. Please register.")
        return
    
    # Check the password
    with open(f"{username}.txt", "r") as file:
        stored_password = file.read()

    if password == stored_password:
        messagebox.showinfo("Success", "Login successful.")
        
    else:
        messagebox.showerror("Error", "Invalid password.")

loginbtn = ctk.CTkButton(login, text="login", command=loginfn)
loginbtn.place(x=33, y=150)

def regfn():
    login.withdraw()

    def center_window(width=200, height=185):
        # get screen width and height
        screen_width = register.winfo_screenwidth()
        screen_height = register.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        register.geometry('%dx%d+%d+%d' % (width, height, x, y))

    register = ctk.CTkToplevel(login)
    center_window(200, 175)
    register.geometry("200x185")
    register.title("register page")

    mainname = ctk.CTkEntry(register, placeholder_text="Username")
    mainname.place(x=33, y=30)

    mainpwd = ctk.CTkEntry(register, placeholder_text="Password")
    mainpwd.place(x=33, y=70)

    def registerfn():
        username = mainname.get()
        password = mainpwd.get()

        # Check if username or password is empty
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
    
        # Check if the username already exists
        if os.path.exists(f"{username}.txt"):
            messagebox.showerror("Error", "Username already exists.")
            return
    
        # Create a new user file
        with open(f"{username}.txt", "w") as file:
            file.write(password)
    
        messagebox.showinfo("Success", "Registration successful. You can now log in.")
        clear_register_fields()

        def clear_register_fields():
            mainname.delete(0, ctk.END)
            mainpwd.delete(0, ctk.END)

    def loginfn():
        register.destroy()
        login.deiconify()

    loginbtn = ctk.CTkButton(register, text="login", command=loginfn)
    loginbtn.place(x=33, y=150)

    letsreg = ctk.CTkButton(register, text="Register", command=registerfn)
    letsreg.place(x=33, y=110)

    titlelbl = ctk.CTkLabel(register, text="Register")
    titlelbl.place(x=79.5, y=0)

    def logindest():
        login.destroy()
    
    register.protocol("WM_DELETE_WINDOW", logindest)

    register.mainloop()


letsreg = ctk.CTkButton(login, text="Register", command=regfn)
letsreg.place(x=33, y=110)

titlelbl = ctk.CTkLabel(login, text="Login")
titlelbl.place(x=87.5, y=0)

login.mainloop()