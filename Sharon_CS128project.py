from tkinter import * 
import random

class TkGUI:
	
	def __init__(self, master):
		self.master = master 
		master.title("Sharon project")
		master.geometry("400x300")
		
		self.label = Label(self.master, text = "Hello Player" )
		self.label.pack(pady=10)
		
		self.Frame = Frame(self.master)
		self.Frame.pack(fill=BOTH)

		myButton = Button(self.Frame,text="START PLAYING!",highlightbackground="blue", width=25, height=10,command= self.NewWindow)
		myButton.pack(pady=10, side=LEFT)
		
		quitButton = Button(self.Frame, text="Quit", highlightbackground="navy", width=25, height=10, command=self.Frame.quit)
		quitButton.pack(side=LEFT)
		
	def NewWindow(self):
		self.newWindow = Toplevel(self.master)
		self.newWindow.title("Rock Paper Scissors Game")
		self.newWindow.geometry("220x280")

		self.quitButton1 = Button(self.newWindow, text="Quit", highlightbackground="navy", command=self.newWindow.quit)
		self.quitButton1.grid(column=0,row=4)

		button1 = Button(self.newWindow,text="Rock",highlightbackground="pink", command=self.rock)
		button1.grid(column=0,row=1)
		button2 = Button(self.newWindow,text="Paper",highlightbackground="MediumTurquoise",command=self.paper)
		button2.grid(column=0,row=2)
		button3 = Button(self.newWindow,text="Scissor",highlightbackground="skyblue",command= self.scissor)
		button3.grid(column=0,row=3)

		self.USER_SCORE = 0 
		self.COMP_SCORE = 0 
		self.USER_CHOICE = ""
		self.COMOP_CHOICE = ""

	def choice_to_number(self, choice):
		self.rps= {"rock":0, "paper":1, "scissor": 2}
		return self.rps[choice]

	def number_to_choice(self,number):	
		self.rps = {0:"rock", 1:"paper", 2:"scissor"}
		return self.rps[number]

	def random_computer_choice(self):
		return random.choice(['rock','paper','scissor']) 

	def result(self, human_choice,comp_choice):
		global USER_SCORE
		global COMP_SCORE

		self.user=self.choice_to_number(human_choice)
		self.comp=self.choice_to_number(comp_choice)

		if(self.user==self.comp):
			self.USER_SCORE+= 0
			self.COMP_SCORE+= 0
		elif((self.user-self.comp)%3==1):
			self.USER_SCORE+=1
		else:
			self.COMP_SCORE+=1

		self.text_area = Text(self.newWindow ,height=12,width=30, bg= "MediumSlateBlue")
		self.text_area.grid(column=0,row=5)
		answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=self.USER_CHOICE,cc=self.COMP_CHOICE,u=self.USER_SCORE,c=self.COMP_SCORE)    
		self.text_area.insert(END,answer)

	def rock(self):
		global USER_CHOICE
		global COMP_CHOICE
		self.USER_CHOICE='rock'
		self.COMP_CHOICE=self.random_computer_choice()
		self.result(self.USER_CHOICE,self.COMP_CHOICE)

	def paper(self):
		global USER_CHOICE
		global COMP_CHOICE
		self.USER_CHOICE='paper'
		self.COMP_CHOICE=self.random_computer_choice()
		self.result(self.USER_CHOICE,self.COMP_CHOICE)

	def scissor(self):
		global USER_CHOICE
		global COMP_CHOICE
		self.USER_CHOICE='scissor'
		self.COMP_CHOICE = self.random_computer_choice() 
		self.result(self.USER_CHOICE,self.COMP_CHOICE)
	
root = Tk()
t = TkGUI(root)
root.mainloop()