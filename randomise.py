import random
from tkinter import *
randomApp = Tk()
randomApp.lift()
randomApp.title("Random notes")
randomApp.geometry('600x800')
frame=Frame(randomApp)
frame.grid()

note1=['1','b3','4','b5','5','b7']
note2=['1','b3','4','b5','5','b7']
note3=['1','b3','4','b5','5','b7']
note4=['1','b3','4','b5','5','b7']

def helloCallBack():
	for x in range(1,5):
		y=1
		globals()['n'+str(y)]=random.choice(globals()['note'+str(y)])
		while (y < 4):
			globals()['n'+str(y+1)]=random.choice(globals()['note'+str(y+1)])
			if globals()['n'+str(y)]!=globals()['n'+str(y+1)]:
				y=y+1
			else: 
				globals()['n'+str(y+1)]=random.choice(globals()['note'+str(y+1)])
		globals()['var'+str(x)]=StringVar()
		globals()['label'+str(x)]=Label(frame,textvariable=globals()['var'+str(x)],font=("Helvetica", 18))
		globals()["var"+str(x)].set(n1+" "+n2+" "+n3+" "+n4)
		globals()['label'+str(x)].grid()
	separator=Frame(frame,height=2,width=600,bg="black")
	separator.grid()

def ClearScreen():
	for widget in frame.winfo_children():
		widget.destroy()
	B=Button(frame, text="random", command=helloCallBack)
	B.grid(row=1,column=0, sticky=W)
	Clear=Button(frame, text="clear", command=ClearScreen)
	Clear.grid(row=2,column=0, sticky=W)
	frame.grid()
	
B=Button(frame, text="random", command=helloCallBack)
B.grid(row=1,column=0, sticky=W)
Clear=Button(frame, text="clear", command=ClearScreen)
Clear.grid(row=2,column=0, sticky=W)
randomApp.mainloop()