
from Tkinter import Button
from Tkinter import Tk
from Tkinter import RAISED
from tkMessageBox import showinfo

top = Tk()

def hello_there():
    showinfo('TitleSpam', 'msg_spam')

B1 = Button(top, text='hello', command=hello_there)

B2 = Button(top, text='watch', relief=RAISED, cursor='watch')
B3 = Button(top,  relief=RAISED, bitmap="hourglass", anchor='w')

B1.pack()
B2.pack()
B3.pack()
top.mainloop()