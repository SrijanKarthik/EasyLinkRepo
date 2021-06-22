##this is by no means a finished product and doesn\t even include formatting or text for the actual admin login page. this is simply a demo for a program that uses sql as a database for a login system

##importing tkinter which is a python addon that helps with this type of program
from tkinter import *
import tkinter.messagebox
import mysql.connector


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="logindb")
cursordb = connectiondb.cursor()

## the following commands are for things that can occur when running the program, their outputs have not been configures yet
def login():
    global root2
    global username_verification
    global password_verification
 

def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
   
def failed():
    global failed_message
    failed_message = Toplevel(root2)
    

def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from usertable where username = %s and password = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

main_display()
root.mainloop()
