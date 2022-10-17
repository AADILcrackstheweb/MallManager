from tkinter import *
from winsound import *
root=Tk()
play=lambda:PlaySound('"D:/Personal/sant.mp3"',SND_FILENAME)
b=Button(root,text='play',command=play)
b.pack()
root.mainloop()
