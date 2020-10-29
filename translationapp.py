from tkinter import *
from PIL import ImageTk,Image

#frame
root = Tk()
root.title("english to french")
root.geometry("710x300")


topframe = Frame(root,bg="black",height="20")
topframe.pack(fill=X)

try:
  f = open("EngtoFR.csv")
  f.write("")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

def findme():
    input = e2.get()
    for word in Translater:
        w = word.split(",")
        if(w[0]==input):
            print("the translation is {}".format(w[1].strip()))
            l4.config(text= "The translation is "+ w[1].strip())
            return
        l4.config(text ="There is no translation for "+ e2.get())

def findme1(event):
    input = e2.get()
    for word in Translater:
        w = word.split(",")
        if(w[0]==input):
            print("the translation is {}".format(w[1].strip()))
            l4.config(text= "The translation is "+ w[1].strip())
            return
        l4.config(text ="There is no translation for "+ e2.get())


fi = open("EngtoFR.csv","r")
Translater = fi.readlines()
fi.close()

try:
    fi = open("EngtoFR.csv","r")
except:
        print("File cannot be found")


#space above boxes
spaceframe = Frame(root,height=60,width=150)
spaceframe.pack(fill=X)
#text above boxes
l1=Label(spaceframe,text="                                                         Welcome to the French to English Translater")
l1.grid(row=1,column=7)
l2 = Label(spaceframe,text="")
l2.grid(row=2,column=7)

#date
from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)
print("Date and Time :", now)
l2.config(text= now)

l2 = Label(spaceframe,text="         ")
l2.grid(row=2,column=8)





invisoframe = Frame(root,width=500,height=150)
invisoframe.pack()
#buttons
b1 = Button(invisoframe,text = "Translate to English",
                                        command=findme)
b1.grid(row=7,column=1)

#text below translate boxes
b3 = Label(invisoframe,text= "                                                                  ")
b3.grid(row=9,column=1)
b4 = Label(invisoframe,text="")
b4.grid(row=10,column=1)
#right frame
leftframe = Frame(invisoframe,borderwidth = 1.5, relief=RAISED, width=500,height=200,bg="white")
leftframe.grid(row=0,column=2)
c1 = Label(leftframe,text="English",fg="blue")
c1.grid(row=3,column = 5)
l4 = Label(leftframe,text="")
l4.grid(row=5,column=5)

#space between boxes
h_spaceframe = Frame(invisoframe,width=10)
h_spaceframe.grid(row=0,column=1)


#left frame
rightframe = Frame(invisoframe,borderwidth = 1.5, relief=RAISED, width=200,height=300,bg="white")
rightframe.grid(row=0,column=1)
l3 = Label(rightframe,text="French",fg= "blue")
l3.grid(row=3,column = 5)
e2 = Entry(rightframe)
e2.grid(row=4,column=5)
e2.bind('<Return>', findme1)

mainloop()








