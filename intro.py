#Intro to PyRhythm:-
from tkinter import *
import winsound as ws
import os
import mysql.connector as sql
import tkinter.messagebox
import pygame

source = sql.connect(host = "localhost", user = "root", passwd = "root")
mycursor = source.cursor()
mycursor.execute("use sakaar")

intro = Tk()
intro.configure(background="black")

intro.title('PyRhythm')    #Name 
intro.geometry("1260x950")   #SIze of Canvas

#NEW SOUND
pygame.init()
def load():             #For running Keyboard
    if name.get() != "" and password.get() != "":
        pygame.mixer.music.load(r"n.mp3") #Loading File Into Mixer
        pygame.mixer.music.play() #Playing It In The Whole Device

        mycursor.execute(f"insert into pyrhythm_db values('{name.get()}','{password.get()}')")
        source.commit()     #Commits data into database
        os.system("keyboard.py")    #Run by Computer
        intro.destroy()     #Exits from Login Page

    else:
        tkinter.messagebox.showinfo("Error","Please enter a valid username and password!")      #Error Popup Box
        
     

heading=Label(intro, text="Welcome to PyRhythm!", fg='purple', font=("bradley hand itc", 48))
heading.place(x=60, y=40)
heading.pack()
heading.configure(background="black")


user=Label(intro, text="Please enter your username:", font=("bradley hand itc",20),fg="purple",bg="black")
user.pack()
name=Entry(intro, bd=2, font=("bradley hand itc",16),bg="black",fg="yellow")
name.place(x=100, y=200)
name.pack() #Compile 

pwd=Label(intro, text="Please enter your password:", font=("bradley hand itc",20),fg="purple",bg="black")
pwd.pack()
password=Entry(intro, bd=2, font=("bradley hand itc",16),bg="black",fg="yellow",show="*")#Entry widget gives column for input by user
password.place(x=80, y=150)
password.pack()

btn=Button(intro, text="Create Music!",bd=0,bg="black" ,fg='purple', font=("bradley hand itc",28),command=load,) #For Showing Keyboard
btn.place(x=120, y=250)
btn.pack()



intro.mainloop()#Cavvas is closed(Closing module)


