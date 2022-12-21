from tkinter import *
import os
def sign_up_b():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "a")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text= "Sign up successful", fg="green", font=("calibre", 11)).pack()
def sign_up():
    global screen1
    screen1= Toplevel(screen)
    screen1.title("Sign in")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1,text="Please put details below").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username:").pack()
    username_entry = Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password:").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Sign in", width=10, height=1, command= sign_up_b).pack()
def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def succes():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login success").pack()
    Button(screen3, text="Okay", command=delete2).pack()
def incorrect_password():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="Okay", command=delete3).pack()
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5, text="Name Error").pack()
    Button(screen5, text="Okay", command=delete4).pack()
def log_in_b():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            succes()
        else:
            incorrect_password()
    else:
        user_not_found()
def log_in():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please put details below to login").pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global password_entry1
    global username_entry1
    Label(screen2, text="Username:").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(text="")
    Label(screen2, text="Password:").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=log_in_b).pack()
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0",  bg= "gray", width="300", height= "2", font=("Calibre", 14)).pack()
    Label(text="").pack()
    Button(text= "Login", height="2", width="30", command=log_in).pack()
    Label(text="").pack()
    Button(text= "Sign up", height="2", width="30", command = sign_up).pack()
    screen.mainloop()
main_screen()
