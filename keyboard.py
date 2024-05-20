#Main PyRhythm KeyBoard:-
from tkinter import *
import winsound as ws
import mysql.connector as sql
import pygame

source = sql.connect(host = "localhost", user = "root", passwd = "root")
mycursor = source.cursor()

root = Tk()
root.title('PyRhythm')

def showdb():
    mycursor.execute("use sakaar")
    mycursor.execute("Select * from pyrhythm_db")
    data = mycursor.fetchall()
    print("The database of users and their passwords are as follows:-")
    print("User", "\tPassword")
    for i in data:
        print(i[0],'\t',i[1])
#NEW SOUND
pygame.init()
def play():
    pygame.mixer.music.load(r"b.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
    source.commit()
    for i in range(1000):
        print()
    root.destroy()

    
header1=Label(root, text="PyRhythm", fg='purple', font=("bradley hand itc", 15, 'bold'))
header1.grid(row = 4, column = 4)
header2=Label(root, text="KeyBoard", fg='purple', font=("bradley hand itc", 15, 'bold'))
header2.grid(row = 4, column = 5)

btn=Button(root, text="Show DataBase",bd=2 ,fg='purple', font=("bradley hand itc",10, 'bold'),command=showdb)
btn.grid(row = 4, column = 1)
btn=Button(root, text="Exit PyRhythm",bd=2 ,fg='purple', font=("bradley hand itc",10, 'bold'),command=play)
btn.grid(row = 4, column = 8)


def key(event=''):
    ws.PlaySound("Keys 1.wav",ws.SND_ASYNC)
def key2(event=''):
    ws.PlaySound("Keys 2.wav",ws.SND_ASYNC)
def key3(event=''):
    ws.PlaySound("Keys 3.wav",ws.SND_ASYNC)
def key4(event=''):
    ws.PlaySound("Keys 4.wav",ws.SND_ASYNC)
def key5(event=''):
    ws.PlaySound("Keys 5.wav",ws.SND_ASYNC)
def key6(event=''):
    ws.PlaySound("Keys 6.wav",ws.SND_ASYNC)
def guitar1(event=''):
    ws.PlaySound("Guitar 1.wav",ws.SND_ASYNC)
def guitar2(event=''):
    ws.PlaySound("Guitar 2.wav",ws.SND_ASYNC)   
def guitar3(event=''):
    ws.PlaySound("Guitar 3.wav",ws.SND_ASYNC)
def guitar4(event=''):
    ws.PlaySound("Guitar 4.wav",ws.SND_ASYNC)
def guitar5(event=''):
    ws.PlaySound("Guitar 5.wav",ws.SND_ASYNC)
def conga(event=''):
    ws.PlaySound("Conga.wav",ws.SND_ASYNC)
def conga2(event=''):
    ws.PlaySound("Conga 2.wav",ws.SND_ASYNC)
def claves(event=''):
    ws.PlaySound("claves.wav",ws.SND_ASYNC)
def clap(event=''):
    ws.PlaySound("clap.wav",ws.SND_ASYNC)
def aweyeah(event=''):
    ws.PlaySound("Aweywah.wav",ws.SND_ASYNC)   
def bob1(event=''):
    ws.PlaySound("808 1.wav",ws.SND_ASYNC)
def bob2(event=''):
    ws.PlaySound("808 2.wav",ws.SND_ASYNC)
def bob3(event=''):
    ws.PlaySound("808 3.wav",ws.SND_ASYNC)
def bob4(event=''):
    ws.PlaySound("808 4.wav",ws.SND_ASYNC)
def bob5(event=''):
    ws.PlaySound("808 5.wav",ws.SND_ASYNC)
def gun(event=''):
    ws.PlaySound("Gun.wav",ws.SND_ASYNC)
def ha(event=''):
    ws.PlaySound("Ha.wav",ws.SND_ASYNC)
def hat1(event=''):
    ws.PlaySound("Hat 1.wav",ws.SND_ASYNC)   
def hat2(event=''):
    ws.PlaySound("Hat 2.wav",ws.SND_ASYNC)
def hey(event=''):
    ws.PlaySound("Hey.wav",ws.SND_ASYNC)
def holdup(event=''):
    ws.PlaySound("Holdup.wav",ws.SND_ASYNC)
def huh(event=''):
    ws.PlaySound("Huh.wav",ws.SND_ASYNC)
def jyea(event=''):
    ws.PlaySound("jyea.wav",ws.SND_ASYNC)
def khaled(event=''):
    ws.PlaySound("Khaled.wav",ws.SND_ASYNC)
def kick(event=''):
    ws.PlaySound("kick.wav",ws.SND_ASYNC)
def kick2(event=''):
    ws.PlaySound("kick 2.wav",ws.SND_ASYNC)
def rim(event=''):
    ws.PlaySound("rim.wav",ws.SND_ASYNC)
def shaker(event=''):
    ws.PlaySound("Shaker.wav",ws.SND_ASYNC)
def snap(event=''):
    ws.PlaySound("snap.wav",ws.SND_ASYNC)
def snare(event=''):
    ws.PlaySound("snare.wav",ws.SND_ASYNC)
def snare2(event=''):
    ws.PlaySound("snare 2.wav",ws.SND_ASYNC)
def stick(event=''):
    ws.PlaySound("Stick.wav",ws.SND_ASYNC)
def tom(event=''):
    ws.PlaySound("Tom.wav",ws.SND_ASYNC)
def tom2(event=''):
    ws.PlaySound("Tom 2.wav",ws.SND_ASYNC)   
def triangle(event=''):
    ws.PlaySound("Triangle.wav",ws.SND_ASYNC)
def uah(event=''):
    ws.PlaySound("uah.wav",ws.SND_ASYNC)
def ugh(event=''):
    ws.PlaySound("Ugh.wav",ws.SND_ASYNC)
def yeauh(event=''):
    ws.PlaySound("yeauh.wav",ws.SND_ASYNC)
def crash(event=''):
    ws.PlaySound("Crash.wav",ws.SND_ASYNC)


Bob1 = Button(root, text = "   Bob1  ", width = 16, height = 7, command = bob1, bg = "#F4ECF7",borderwidth=0)
Bob1.grid(row = 0, column = 0)
Bob1.bind_all("1", bob1)

Bob2 = Button(root, text = "    Bob2   ", width = 16, height = 7, command = bob2, bg = "#E8DAEF",borderwidth=0)
Bob2.grid(row = 0, column = 1)
Bob2.bind_all("2", bob2)

Bob3 = Button(root, text = "     Bob3   ", width = 16, height = 7, command = bob3, bg = "#D2B4DE",borderwidth=0)
Bob3.grid(row = 0, column = 2)
Bob3.bind_all("3", bob3)

Bob4 = Button(root, text = "      Bob4   ", width = 16, height = 7, command = bob4, bg = "#BB8FCE",borderwidth=0)
Bob4.grid(row = 0, column = 3)
Bob4.bind_all("4", bob4)

Bob5 = Button(root, text = "    Bob5     ", width = 16, height = 7, command = bob5, bg = "#A569BD",borderwidth=0)
Bob5.grid(row = 0, column = 4)
Bob5.bind_all("5", bob5)

Gun = Button(root, text = "      Gun     ", width = 16, height = 7, command = gun, bg = "#8E44AD",borderwidth=0)
Gun.grid(row = 0, column = 5)
Gun.bind_all("6", gun)

Ha = Button(root, text = "     Ha       ", width = 16, height = 7, command = ha, bg = "#7D3C98",borderwidth=0)
Ha.grid(row = 0, column = 6)
Ha.bind_all("7", ha)

Hat1 = Button(root, text = "     Hat1     ", width = 16, height = 7, command = hat1, bg = "#6C3483",borderwidth=0)
Hat1.grid(row = 0, column = 7)
Hat1.bind_all("8", hat1)

Hat2 = Button(root, text = "    Hat2        ", width = 16, height = 7, command = hat2, bg = "#5B2C6F",borderwidth=0)
Hat2.grid(row = 0, column = 8)
Hat2.bind_all("9", hat2)

Hey = Button(root, text = "       Hey      ", width = 16, height = 7, command = hey, bg = "#4A235A",borderwidth=0)
Hey.grid(row = 0, column = 9)
Hey.bind_all("0", hey)

Jyea = Button(root, text = "    Jyea   ", width = 16, height = 7, command = jyea, bg = "#EBF5FB",borderwidth=0)
Jyea.grid(row = 1, column = 0)
Jyea.bind_all("q", jyea)

Khaled = Button(root, text = "  Khaled  ", width = 16, height = 7, command = khaled, bg = "#D6EAF8",borderwidth=0)
Khaled.grid(row = 1, column = 1)
Khaled.bind_all("w", khaled)

Kick = Button(root, text = "     Kick     ", width = 16, height = 7, command = kick, bg = "#AED6F1",borderwidth=0)
Kick.grid(row = 1, column = 2)
Kick.bind_all("e", kick)

Kick2 = Button(root, text = "     Kick2    ", width = 16, height = 7, command = kick2, bg = "#85C1E9",borderwidth=0)
Kick2.grid(row = 1, column = 3)
Kick2.bind_all("r", kick2)

Rim = Button(root, text = "     Rim      ", width = 16, height = 7, command = rim, bg = "#5DADE2",borderwidth=0)
Rim.grid(row = 1, column = 4)
Rim.bind_all("t", rim)

Shaker = Button(root, text = "  Shaker     ", width = 16, height = 7, command = shaker, bg = "#3498DB",borderwidth=0)
Shaker.grid(row = 1, column = 5)
Shaker.bind_all("y", shaker)

Snap = Button(root, text = "     Snap   ", width = 16, height = 7, command = snap, bg = "#2E86C1",borderwidth=0)
Snap.grid(row = 1, column = 6)
Snap.bind_all("u", snap)

Snare = Button(root, text = "     Snare    ", width = 16, height = 7, command = snare, bg = "#2874A6",borderwidth=0)
Snare.grid(row = 1, column = 7)
Snare.bind_all("i", snare)

Snare2 = Button(root, text = "   Snare2     ", width = 16, height = 7, command = snare2, bg = "#21618C",borderwidth=0)
Snare2.grid(row = 1, column = 8)
Snare2.bind_all("o", snare2)

Stick = Button(root, text = "   Stick1       ", width = 16, height = 7, command = stick, bg = "#1B4F72",borderwidth=0)
Stick.grid(row = 1, column = 9)
Stick.bind_all("p", stick)

Triangle = Button(root, text = "Triangle ", width = 16, height = 7, command = triangle, bg = "#EAFAF1",borderwidth=0)
Triangle.grid(row = 2, column = 0)
Triangle.bind_all("a", triangle)

Tom = Button(root, text = "  Tom1     ", width = 16, height = 7, command = tom, bg = "#D5F5E3",borderwidth=0)
Tom.grid(row = 2, column = 1)
Tom.bind_all("s", tom)

Tom2 = Button(root, text = "   Tom2     ", width = 16, height = 7, command = tom2, bg = "#ABEBC6",borderwidth=0)
Tom2.grid(row = 2, column = 2)
Tom2.bind_all("d", tom2)

Yeauh = Button(root, text = "   Yeauh     ", width = 16, height = 7, command = yeauh, bg = "#82E0AA",borderwidth=0)
Yeauh.grid(row = 2, column = 3)
Yeauh.bind_all("f", yeauh)

Crash = Button(root, text = "   Crash     ", width = 16, height = 7, command = crash, bg = "#58D68D",borderwidth=0)
Crash.grid(row = 2, column = 4)
Crash.bind_all("g", crash)

Key1 = Button(root, text = "    Key1      ", width = 16, height = 7, command = key, bg = "#2ECC71",borderwidth=0)
Key1.grid(row = 2, column = 5)
Key1.bind_all("h", key)

Key2 = Button(root, text = "   Key2     ", width = 16, height = 7, command = key2, bg = "#28B463",borderwidth=0)
Key2.grid(row = 2, column = 6)
Key2.bind_all("j", key2)

Key3 = Button(root, text = "     Key3      ", width = 16, height = 7, command = key3, bg = "#239B56",borderwidth=0)
Key3.grid(row = 2, column = 7)
Key3.bind_all("k", key3)

Key4 = Button(root, text = "     Key4      ", width = 16, height = 7, command = key4, bg = "#1D8348",borderwidth=0)
Key4.grid(row = 2, column = 8)
Key4.bind_all("l", key4)

Key5 = Button(root, text = "      Key5     ", width = 16, height = 7, command = key5, bg = "#186A3B",borderwidth=0)
Key5.grid(row = 2, column = 9)
Key5.bind_all(";", key5)

Guitar1 = Button(root, text = "Guitar1  ", width = 16, height = 7, command = guitar1, bg = "#FDEDEC",borderwidth=0)
Guitar1.grid(row = 3, column = 0)
Guitar1.bind_all("z", guitar1)

Guitar2 = Button(root, text = " Guitar2  ", width = 16, height = 7, command = guitar2, bg = "#FADBD8",borderwidth=0)
Guitar2.grid(row = 3, column = 1)
Guitar2.bind_all("x", guitar2)

Guitar3 = Button(root, text = " Guitar3    ", width = 16, height = 7, command = guitar3, bg = "#F5B7B1",borderwidth=0)
Guitar3.grid(row = 3, column = 2)
Guitar3.bind_all("c", guitar3)

Guitar4 = Button(root, text = "  Guitar4    ", width = 16, height = 7, command = guitar4, bg = "#F1948A",borderwidth=0)
Guitar4.grid(row = 3, column = 3)
Guitar4.bind_all("v", guitar4)

Guitar5 = Button(root, text = "  Guitar5    ", width = 16, height = 7, command = guitar5, bg = "#EC7063",borderwidth=0)
Guitar5.grid(row = 3, column = 4)
Guitar5.bind_all("b", guitar5)

Conga = Button(root, text = "  Conga   ", width = 16, height = 7, command = conga, bg = "#E74C3C",borderwidth=0)
Conga.grid(row = 3, column = 5)
Conga.bind_all("n", conga)

Conga2 = Button(root, text = "  Conga2  ", width = 16, height = 7, command = conga2, bg = "#CB4335",borderwidth=0)
Conga2.grid(row = 3, column = 6)
Conga2.bind_all("m", conga2)

Claves = Button(root, text = "     Claves      ", width = 16, height = 7, command = claves, bg = "#B03A2E",borderwidth=0)
Claves.grid(row = 3, column = 7)
Claves.bind_all(",", claves)

Clap = Button(root, text = "     Clap    ", width = 16, height = 7, command = clap, bg = "#943126",borderwidth=0)
Clap.grid(row = 3, column = 8)
Clap.bind_all(".", clap)

Aweyeah = Button(root, text = " Aweyeah      ", width = 16, height = 7, command = aweyeah, bg = "#78281F",borderwidth=0)
Aweyeah.grid(row = 3, column = 9)
Aweyeah.bind_all("/", aweyeah)


root.mainloop()



